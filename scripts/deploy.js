const hre = require("hardhat");

async function main() {
  const [deployer] = await hre.ethers.getSigners();
  console.log("Deploying contracts with:", deployer.address);

  const usdcAddress = process.env.USDC_ADDRESS || "0x0000000000000000000000000000000000000000";

  const X402Executor = await hre.ethers.getContractFactory("X402Executor");
  const x402Executor = await X402Executor.deploy(usdcAddress);
  await x402Executor.waitForDeployment();
  console.log("X402Executor deployed to:", await x402Executor.getAddress());

  const PaymentAgent = await hre.ethers.getContractFactory("PaymentAgent");
  const paymentAgent = await PaymentAgent.deploy();
  await paymentAgent.waitForDeployment();
  console.log("PaymentAgent deployed to:", await paymentAgent.getAddress());

  console.log("\nDeployment complete!");
  console.log("Save these addresses to your .env file");
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
