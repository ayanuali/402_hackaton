# Hackathon Submission Checklist

## Required Deliverables

### 1. Project Overview (1-2 paragraphs)

**Draft:**

The Autonomous Payment Agent is an AI-powered system for managing recurring and conditional payments on Cronos EVM using the x402 protocol. Users define payment rules once (recipient, amount, interval), and the agent automatically executes payments when conditions are met. The system uses x402 for gasless settlement, meaning users never pay gas fees for automated payments.

This solves real problems in crypto payments: recurring subscriptions, automated DCA strategies, team payroll, and milestone-based payouts. Instead of manually executing transactions or writing custom scripts, users interact with an AI agent that handles everything automatically. The agent monitors on-chain state, verifies conditions, and executes transfers via x402's gasless infrastructure.

### 2. GitHub Repository

- Repository: https://github.com/ayanuali/402_hackaton
- Status: Public
- License: MIT (need to add)

### 3. Demo Video

**What to show:**

1. Quick intro (30 sec)
   - What problem we're solving
   - Who it's for

2. Live demo (2-3 min)
   - Create payment rule via CLI
   - Show agent monitoring
   - Execute automated payment
   - Show transaction on explorer

3. Technical highlights (1 min)
   - Smart contract architecture
   - x402 integration
   - Agent monitoring system

4. Use cases (30 sec)
   - Subscriptions
   - Team payments
   - DCA strategies

**Tools:**
- Record with Loom or OBS
- Max length: 5 minutes
- Upload to YouTube (unlisted)

### 4. Functional Prototype

**Deployment checklist:**

- [ ] Deploy to Cronos testnet
- [ ] Verify contracts on explorer
- [ ] Test end-to-end flow
- [ ] Document contract addresses
- [ ] Prepare demo accounts

**Contract addresses (testnet):**
- PaymentAgent: TBD
- X402Executor: TBD
- Test USDC: TBD

### 5. On-Chain Component

**x402 Integration:**
- X402Executor.sol handles gasless transfers
- Uses EIP-3009 transferWithAuthorization
- User signs once, agent pays gas

**Cronos EVM:**
- Deployed on testnet (chain ID 338)
- Will deploy to mainnet before submission
- Uses Cronos RPC endpoints

## Tracks to Submit

### Primary: Main Track - x402 Applications

**Why we fit:**
- Novel use of x402 for autonomous agents
- Combines AI decision-making with gasless payments
- Practical application (recurring payments)
- Shows technical depth

**Pitch:**
First autonomous payment agent using x402. Users set rules once, agent handles everything. No manual transactions, no gas fees.

### Secondary: Best x402 AI Agentic Finance Solution

**Why we fit:**
- AI agent that makes payment decisions
- Automated execution based on conditions
- Financial use cases (DCA, payroll, subscriptions)
- x402 integration for settlement

**Pitch:**
Agentic finance where AI handles your recurring payments intelligently. Set constraints, agent executes within them.

## Submission Timeline

**Week 1 (Dec 12-18):**
- [x] Core smart contracts
- [x] Agent backend
- [x] Basic CLI
- [ ] Deploy to testnet

**Week 2 (Dec 19-25):**
- [ ] Test end-to-end
- [ ] Fix bugs
- [ ] Improve UX
- [ ] Add more use cases

**Week 3 (Dec 26 - Jan 1):**
- [ ] Polish everything
- [ ] Write better docs
- [ ] Prepare demo accounts
- [ ] Test demo flow

**Week 4 (Jan 2-8):**
- [ ] Record demo video
- [ ] Deploy to mainnet
- [ ] Final testing
- [ ] Write submission text

**Week 5 (Jan 9-15):**
- [ ] Submit to DoraHacks
- [ ] Buffer for issues

**Week 6 (Jan 16-23):**
- [ ] Final improvements
- [ ] Respond to feedback

**Submission Deadline:** Jan 23, 2026

## Evaluation Criteria

**Innovation:**
- First x402 autonomous payment agent
- Novel approach to recurring payments
- Combines AI + gasless settlement

**Agentic Functionality:**
- AI monitors conditions
- Makes execution decisions
- Handles edge cases automatically

**Execution Quality:**
- Clean, tested code
- Good documentation
- Working prototype
- Professional demo

**Ecosystem Value:**
- Solves real problems
- Enables new use cases
- Easy to integrate
- Production-ready architecture

## Next Steps

1. Test everything locally
2. Deploy to Cronos testnet
3. Get testnet tokens
4. Run end-to-end demo
5. Fix any issues
6. Record demo video
7. Submit on DoraHacks

## Resources

- Cronos Docs: https://docs.cronos.org
- x402 Guide: https://docs.cronos.org/cronos-x402-facilitator/introduction
- DoraHacks Platform: https://dorahacks.io
- Cronos Discord: x402-hackathon channel
