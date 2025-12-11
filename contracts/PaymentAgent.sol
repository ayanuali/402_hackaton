// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IERC20 {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract PaymentAgent {
    struct PaymentRule {
        address token;
        address recipient;
        uint256 amount;
        uint256 interval;
        uint256 lastExecution;
        bool active;
        string condition;
    }

    mapping(address => mapping(uint256 => PaymentRule)) public userRules;
    mapping(address => uint256) public ruleCount;

    event RuleCreated(address indexed user, uint256 indexed ruleId, address recipient, uint256 amount);
    event PaymentExecuted(address indexed user, uint256 indexed ruleId, address recipient, uint256 amount);
    event RuleDeactivated(address indexed user, uint256 indexed ruleId);

    function createRule(
        address token,
        address recipient,
        uint256 amount,
        uint256 interval,
        string memory condition
    ) external returns (uint256) {
        uint256 ruleId = ruleCount[msg.sender]++;

        userRules[msg.sender][ruleId] = PaymentRule({
            token: token,
            recipient: recipient,
            amount: amount,
            interval: interval,
            lastExecution: 0,
            active: true,
            condition: condition
        });

        emit RuleCreated(msg.sender, ruleId, recipient, amount);
        return ruleId;
    }

    function executePayment(address user, uint256 ruleId) external {
        PaymentRule storage rule = userRules[user][ruleId];
        require(rule.active, "Rule not active");
        require(block.timestamp >= rule.lastExecution + rule.interval, "Too early");

        IERC20 token = IERC20(rule.token);
        require(token.balanceOf(user) >= rule.amount, "Insufficient balance");

        rule.lastExecution = block.timestamp;

        require(token.transferFrom(user, rule.recipient, rule.amount), "Transfer failed");

        emit PaymentExecuted(user, ruleId, rule.recipient, rule.amount);
    }

    function deactivateRule(uint256 ruleId) external {
        require(userRules[msg.sender][ruleId].active, "Already inactive");
        userRules[msg.sender][ruleId].active = false;
        emit RuleDeactivated(msg.sender, ruleId);
    }

    function getRule(address user, uint256 ruleId) external view returns (PaymentRule memory) {
        return userRules[user][ruleId];
    }

    function isExecutable(address user, uint256 ruleId) external view returns (bool) {
        PaymentRule memory rule = userRules[user][ruleId];
        if (!rule.active) return false;
        if (block.timestamp < rule.lastExecution + rule.interval) return false;

        IERC20 token = IERC20(rule.token);
        if (token.balanceOf(user) < rule.amount) return false;

        return true;
    }
}
