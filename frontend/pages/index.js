import { useState, useEffect } from 'react';
import Head from 'next/head';

export default function Home() {
  const [rules, setRules] = useState([]);
  const [stats, setStats] = useState({ total: 0, active: 0, executed: 0 });

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
            <p style={styles.stat}>{stats.total}</p>
          </div>

          <div style={styles.card}>
            <h3>Active</h3>
            <p style={styles.stat}>{stats.active}</p>
          </div>

          <div style={styles.card}>
            <h3>Executed</h3>
            <p style={styles.stat}>{stats.executed}</p>
          </div>
        </div>

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
  }
};
