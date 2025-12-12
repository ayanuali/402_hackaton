# Hackathon Submission - Autonomous Payment Agent

## Project Information

**Name**: Autonomous Payment Agent
**Category**: Main Track - x402 Applications
**Additional Categories**: Best x402 AI Agentic Finance Solution

**Live Demo**: https://402-hackaton.vercel.app/
**GitHub**: https://github.com/ayanuali/402_hackaton
**Video Demo**: [To be added]

## Project Summary

An autonomous agent system that executes recurring and conditional payments on Cronos EVM without user intervention. Users create payment rules once, and the AI agent monitors blockchain state to execute payments automatically when conditions are met. The x402 protocol enables gasless execution, eliminating transaction fees for users.

The system consists of smart contracts storing payment rules, a Python agent monitoring the blockchain, and x402 integration for gasless settlement. This enables practical use cases like subscription payments, automated payroll, DCA strategies, and milestone-based payouts.

## Technical Implementation

**Smart Contracts**: PaymentAgent contract manages payment rules with enforcement of execution conditions. Each rule specifies token, recipient, amount, and interval. The contract validates balance, timing, and approval before allowing execution.

**Autonomous Agent**: Python application running on Railway that continuously monitors the blockchain. The agent queries the contract for executable rules and submits transactions when conditions are met. Implements error handling and reliable deployment for continuous operation.

**x402 Integration**: Enables gasless transactions by allowing the agent to pay gas on behalf of users. Users approve token spending once, then all subsequent automated payments execute without gas fees.

**Frontend**: Next.js application that reads live statistics directly from the blockchain. Displays total rules, active monitoring, and execution count using ethers.js to query contract state.

## Key Features

- Set-and-forget payment automation with one-time rule creation
- Gasless execution via x402 protocol
- Real-time blockchain monitoring with 60-second check intervals
- On-chain verification of all payment conditions
- Support for recurring and conditional payment logic
- Live statistics dashboard showing system activity

## Deployed Components

**Cronos Testnet Contracts**:
- PaymentAgent: 0x938C237a5A1F753fc1770960c31f1FD26D548bAc
- X402Executor: 0x93d296EE43EEB00A7DE563d35B2c84283DEA47f6
- Mock USDC: 0xc21223249CA28397B4B6541dfFaEcC539BfF0c59

**Agent**: Running continuously on Railway, monitoring testnet

**Frontend**: Deployed on Vercel with live blockchain data

## Use Cases

**Recurring Subscriptions**: Monthly or weekly payments for services without manual execution each period.

**Team Payroll**: Automated contributor compensation on defined schedules.

**Dollar-Cost Averaging**: Regular token purchases at fixed intervals regardless of price.

**Milestone Payments**: Automatic execution when on-chain conditions are satisfied.

**Treasury Management**: Scheduled transfers and automated organizational finance.

## Innovation

This project demonstrates how autonomous agents can enhance blockchain functionality. Rather than requiring constant user interaction, the agent monitors and acts on behalf of users while maintaining on-chain security guarantees.

The combination of AI agents with gasless transaction protocols creates new possibilities for blockchain applications. Complex workflows become accessible without technical expertise or constant user attention.

## x402 Protocol Usage

The x402 protocol is central to this implementation. Users approve the PaymentAgent contract once during setup. The autonomous agent then executes payments via transferFrom, with the agent wallet covering gas costs. This creates a seamless experience where users never worry about gas fees or transaction execution.

The gasless execution model enables practical recurring payments that would be cost-prohibitive with traditional blockchain transactions. Users pay only the payment amount itself, not gas fees for each execution.

## Agentic Functionality

The monitoring agent makes autonomous decisions about payment execution. It continuously checks blockchain state, evaluates rule conditions, and determines when to submit transactions. The agent handles errors gracefully, retries failed operations, and maintains reliable operation without human intervention.

This demonstrates practical AI agent capabilities in blockchain systems - the agent understands on-chain state, applies rule logic, and takes appropriate actions automatically.

## Production Readiness

The system is deployed and operational on Cronos testnet. The agent runs continuously on Railway with proper error handling and logging. Smart contracts are deployed and verified. The frontend provides real-time visibility into system state.

Documentation includes setup guides, architecture descriptions, and usage examples. The repository contains all source code with clear organization and comments.

## Future Development

The architecture supports expansion to:
- Oracle integration for external data-driven conditions
- Cross-chain execution via bridges
- Natural language rule creation interfaces
- Complex conditional logic beyond simple intervals
- Multi-signature workflows for organizational use

## Testing

To test the system:

1. Visit the frontend to see current statistics
2. View deployed contracts on Cronos explorer
3. Create a payment rule using the CLI
4. Observe the agent detecting and executing the payment in Railway logs
5. Verify execution transaction on Cronos testnet

The repository includes test tokens that can be minted for testing payment execution.

## Team

This project was developed as a solo submission for the Cronos x402 PayTech Hackathon, demonstrating full-stack blockchain development capabilities including smart contracts, backend infrastructure, frontend development, and deployment operations.

## Conclusion

The Autonomous Payment Agent shows practical application of x402 protocol for real-world payment automation. By combining smart contracts, autonomous agents, and gasless transactions, the system provides seamless automation while maintaining blockchain's security and transparency benefits.

This implementation serves as both a functional application and a demonstration of how agentic systems can enhance blockchain usability. The architecture is extensible, well-documented, and ready for further development.
