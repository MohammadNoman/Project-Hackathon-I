import React, { useState } from 'react';
import styles from './styles.module.css';

interface User {
  id: string;
  email: string;
  software_background: string;
  hardware_background: string;
  created_at: string;
}

interface AuthState {
  user: User | null;
  token: string | null;
}

const API_URL = process.env.NODE_ENV === 'production'
  ? 'https://your-backend-url.com/api/auth'
  : 'http://localhost:8000/api/auth';

export default function AuthForms(): JSX.Element {
  const [mode, setMode] = useState<'signin' | 'signup'>('signin');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [auth, setAuth] = useState<AuthState>(() => {
    const saved = localStorage.getItem('auth_state');
    return saved ? JSON.parse(saved) : { user: null, token: null };
  });

  // Form fields
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [softwareBackground, setSoftwareBackground] = useState('');
  const [hardwareBackground, setHardwareBackground] = useState('');

  const saveAuth = (user: User, token: string) => {
    const state = { user, token };
    localStorage.setItem('auth_state', JSON.stringify(state));
    setAuth(state);
  };

  const handleSignout = () => {
    localStorage.removeItem('auth_state');
    setAuth({ user: null, token: null });
    setEmail('');
    setPassword('');
    setSoftwareBackground('');
    setHardwareBackground('');
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      const endpoint = mode === 'signup' ? '/signup' : '/signin';
      const body = mode === 'signup'
        ? { email, password, software_background: softwareBackground, hardware_background: hardwareBackground }
        : { email, password };

      const response = await fetch(`${API_URL}${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
      });

      if (!response.ok) {
        const data = await response.json();
        throw new Error(data.detail || 'Authentication failed');
      }

      const data = await response.json();
      saveAuth(data.user, data.access_token);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  // Show user profile if authenticated
  if (auth.user) {
    return (
      <div className={styles.container}>
        <div className={styles.profileCard}>
          <div className={styles.avatar}>
            {auth.user.email.charAt(0).toUpperCase()}
          </div>
          <h3 className={styles.profileEmail}>{auth.user.email}</h3>

          {auth.user.software_background && (
            <div className={styles.backgroundInfo}>
              <strong>Software:</strong> {auth.user.software_background}
            </div>
          )}
          {auth.user.hardware_background && (
            <div className={styles.backgroundInfo}>
              <strong>Hardware:</strong> {auth.user.hardware_background}
            </div>
          )}

          <button onClick={handleSignout} className={styles.signoutButton}>
            Sign Out
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className={styles.container}>
      <div className={styles.formCard}>
        {/* Tabs */}
        <div className={styles.tabs}>
          <button
            className={`${styles.tab} ${mode === 'signin' ? styles.activeTab : ''}`}
            onClick={() => { setMode('signin'); setError(null); }}
          >
            Sign In
          </button>
          <button
            className={`${styles.tab} ${mode === 'signup' ? styles.activeTab : ''}`}
            onClick={() => { setMode('signup'); setError(null); }}
          >
            Sign Up
          </button>
        </div>

        {/* Error Message */}
        {error && (
          <div className={styles.error}>
            {error}
          </div>
        )}

        {/* Form */}
        <form onSubmit={handleSubmit} className={styles.form}>
          <div className={styles.field}>
            <label htmlFor="email">Email</label>
            <input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="your@email.com"
              required
              disabled={loading}
            />
          </div>

          <div className={styles.field}>
            <label htmlFor="password">Password</label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="••••••••"
              required
              minLength={8}
              disabled={loading}
            />
          </div>

          {/* Background questions for signup */}
          {mode === 'signup' && (
            <>
              <div className={styles.field}>
                <label htmlFor="software">Software Background</label>
                <select
                  id="software"
                  value={softwareBackground}
                  onChange={(e) => setSoftwareBackground(e.target.value)}
                  disabled={loading}
                >
                  <option value="">Select your level...</option>
                  <option value="beginner">Beginner - New to programming</option>
                  <option value="intermediate">Intermediate - Some experience</option>
                  <option value="advanced">Advanced - Professional developer</option>
                  <option value="expert">Expert - Senior/Lead developer</option>
                </select>
              </div>

              <div className={styles.field}>
                <label htmlFor="hardware">Hardware/Robotics Background</label>
                <select
                  id="hardware"
                  value={hardwareBackground}
                  onChange={(e) => setHardwareBackground(e.target.value)}
                  disabled={loading}
                >
                  <option value="">Select your level...</option>
                  <option value="none">None - Completely new</option>
                  <option value="hobbyist">Hobbyist - Built some projects</option>
                  <option value="academic">Academic - Studied robotics</option>
                  <option value="professional">Professional - Work in robotics</option>
                </select>
              </div>
            </>
          )}

          <button
            type="submit"
            className={styles.submitButton}
            disabled={loading}
          >
            {loading ? 'Please wait...' : (mode === 'signup' ? 'Create Account' : 'Sign In')}
          </button>
        </form>

        {mode === 'signup' && (
          <p className={styles.hint}>
            Your background helps us personalize your learning experience.
          </p>
        )}
      </div>
    </div>
  );
}
