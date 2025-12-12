import { useState, useEffect } from 'react';
import Head from 'next/head';
import { ethers } from 'ethers';

const PAYMENT_AGENT_ADDRESS = '0x938C237a5A1F753fc1770960c31f1FD26D548bAc';
const CRONOS_RPC = 'https://evm-t3.cronos.org';
const DEMO_USER = '0xF1c4528A415792c12862CccB8FFfBF4003F8cD5c';

const PAYMENT_AGENT_ABI = [
  {"inputs":[{"name":"user","type":"address"}],"name":"ruleCount","outputs":[{"name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
  {"inputs":[{"name":"user","type":"address"},{"name":"ruleId","type":"uint256"}],"name":"getRule","outputs":[{"components":[{"name":"token","type":"address"},{"name":"recipient","type":"address"},{"name":"amount","type":"uint256"},{"name":"interval","type":"uint256"},{"name":"lastExecution","type":"uint256"},{"name":"active","type":"bool"},{"name":"condition","type":"string"}],"name":"","type":"tuple"}],"stateMutability":"view","type":"function"}
];

export default function Home() {
  const [rules, setRules] = useState([]);
  const [stats, setStats] = useState({ total: 0, active: 0, executed: 0 });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadStats();
  }, []);

  async function loadStats() {
    try {
      const provider = new ethers.JsonRpcProvider(CRONOS_RPC);
      const contract = new ethers.Contract(PAYMENT_AGENT_ADDRESS, PAYMENT_AGENT_ABI, provider);

      const count = await contract.ruleCount(DEMO_USER);
      const total = Number(count);
      let active = 0;
      let executed = 0;

      for (let i = 0; i < total; i++) {
        const rule = await contract.getRule(DEMO_USER, i);
        if (rule.active) active++;
        if (rule.lastExecution > 0) executed++;
      }

      setStats({ total, active, executed });
      setLoading(false);
    } catch (error) {
      console.error('Error loading stats:', error);
      setLoading(false);
    }
  }

  return (
    <div style={styles.container}>
      <Head>
        <title>Autonomous Payment Agent</title>
      </Head>

      <main style={styles.main}>
        <h1>Autonomous Payment Agent</h1>
        <p>AI-powered recurring and conditional payments on Cronos x402</p>

        <div style={styles.grid}>
          <div style={styles.card}>
            <h3>Total Rules</h3>
            <p style={styles.stat}>{loading ? '...' : stats.total}</p>
            <p style={styles.sublabel}>On-chain payment rules</p>
          </div>

          <div style={styles.card}>
            <h3>Active</h3>
            <p style={styles.stat}>{loading ? '...' : stats.active}</p>
            <p style={styles.sublabel}>Currently monitoring</p>
          </div>

          <div style={styles.card}>
            <h3>Executed</h3>
            <p style={styles.stat}>{loading ? '...' : stats.executed}</p>
            <p style={styles.sublabel}>Payments completed</p>
          </div>
        </div>

        {!loading && stats.total > 0 && (
          <div style={styles.liveIndicator}>
            <span style={styles.pulse}></span>
            Agent monitoring live on Railway
          </div>
        )}

        <div style={styles.section}>
          <h2>How It Works</h2>
          <ol style={styles.list}>
            <li>Create payment rule (recipient, amount, interval)</li>
            <li>Agent monitors on-chain conditions</li>
            <li>When conditions met, agent executes via x402</li>
            <li>User pays no gas fees</li>
          </ol>
        </div>

        <div style={styles.section}>
          <h2>Use Cases</h2>
          <div style={styles.useCases}>
            <div style={styles.useCase}>
              <h4>Recurring Payments</h4>
              <p>Subscriptions, rent, salaries</p>
            </div>
            <div style={styles.useCase}>
              <h4>Conditional Payments</h4>
              <p>Milestone payouts, DCA strategies</p>
            </div>
            <div style={styles.useCase}>
              <h4>Team Operations</h4>
              <p>Automated treasury management</p>
            </div>
          </div>
        </div>

        <div style={styles.footer}>
          <p>Built for Cronos x402 PayTech Hackathon</p>
          <a href="https://github.com/ayanuali/402_hackaton" target="_blank">
            View on GitHub
          </a>
        </div>
      </main>
    </div>
  );
}

const styles = {
  container: {
    minHeight: '100vh',
    padding: '0 0.5rem',
    fontFamily: 'system-ui, -apple-system, sans-serif',
    background: '#0a0a0a',
    color: '#fff'
  },
  main: {
    maxWidth: '900px',
    margin: '0 auto',
    padding: '4rem 1rem'
  },
  grid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
    gap: '2rem',
    margin: '3rem 0'
  },
  card: {
    padding: '2rem',
    background: '#1a1a1a',
    borderRadius: '8px',
    border: '1px solid #333'
  },
  stat: {
    fontSize: '3rem',
    fontWeight: 'bold',
    margin: '0.5rem 0'
  },
  section: {
    margin: '3rem 0',
    padding: '2rem',
    background: '#1a1a1a',
    borderRadius: '8px'
  },
  list: {
    lineHeight: '2'
  },
  useCases: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
    gap: '1rem',
    marginTop: '1rem'
  },
  useCase: {
    padding: '1rem',
    background: '#0a0a0a',
    borderRadius: '4px'
  },
  footer: {
    marginTop: '4rem',
    textAlign: 'center',
    opacity: 0.7
  },
  sublabel: {
    fontSize: '0.875rem',
    opacity: 0.6,
    marginTop: '0.5rem'
  },
  liveIndicator: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '0.5rem',
    padding: '1rem',
    background: '#1a1a1a',
    borderRadius: '8px',
    border: '1px solid #2a2',
    marginTop: '2rem',
    fontSize: '0.9rem',
    color: '#2a2'
  },
  pulse: {
    width: '8px',
    height: '8px',
    borderRadius: '50%',
    background: '#2a2',
    animation: 'pulse 2s ease-in-out infinite'
  }
};
