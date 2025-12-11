const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("PaymentAgent", function () {
  let paymentAgent;
  let mockToken;
  let owner, recipient, user;

  beforeEach(async function () {
    [owner, recipient, user] = await ethers.getSigners();

    const MockToken = await ethers.getContractFactory("MockERC20");
    mockToken = await MockToken.deploy("Mock USDC", "USDC", 6);

    const PaymentAgent = await ethers.getContractFactory("PaymentAgent");
    paymentAgent = await PaymentAgent.deploy();

    await mockToken.mint(user.address, ethers.parseUnits("1000", 6));
    await mockToken.connect(user).approve(
      await paymentAgent.getAddress(),
      ethers.parseUnits("1000", 6)
    );
  });

  it("Should create a payment rule", async function () {
    const tx = await paymentAgent.connect(user).createRule(
      await mockToken.getAddress(),
      recipient.address,
      ethers.parseUnits("10", 6),
      86400,
      "Daily payment"
    );

    await expect(tx).to.emit(paymentAgent, "RuleCreated");

    const ruleCount = await paymentAgent.ruleCount(user.address);
    expect(ruleCount).to.equal(1);
  });

  it("Should execute payment when conditions are met", async function () {
    await paymentAgent.connect(user).createRule(
      await mockToken.getAddress(),
      recipient.address,
      ethers.parseUnits("10", 6),
      0,
      "Instant payment"
    );

    const beforeBalance = await mockToken.balanceOf(recipient.address);

    await paymentAgent.executePayment(user.address, 0);

    const afterBalance = await mockToken.balanceOf(recipient.address);
    expect(afterBalance - beforeBalance).to.equal(ethers.parseUnits("10", 6));
  });

  it("Should prevent early execution", async function () {
    await paymentAgent.connect(user).createRule(
      await mockToken.getAddress(),
      recipient.address,
      ethers.parseUnits("10", 6),
      86400,
      "Daily payment"
    );

    await paymentAgent.executePayment(user.address, 0);

    await expect(
      paymentAgent.executePayment(user.address, 0)
    ).to.be.revertedWith("Too early");
  });

  it("Should deactivate rule", async function () {
    await paymentAgent.connect(user).createRule(
      await mockToken.getAddress(),
      recipient.address,
      ethers.parseUnits("10", 6),
      86400,
      "Daily payment"
    );

    await paymentAgent.connect(user).deactivateRule(0);

    const rule = await paymentAgent.getRule(user.address, 0);
    expect(rule.active).to.be.false;
  });
});
