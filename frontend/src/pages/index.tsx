import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './index.module.css';

// Module data for the command center grid
const modules = [
  { id: 1, title: 'ROS2 Nervous System', icon: '🧠', status: 'online', path: '/docs/module1-ros2-nervous-system' },
  { id: 2, title: 'Sensing & Perception', icon: '👁️', status: 'online', path: '/docs/module2-robot-sensing-and-perception' },
  { id: 3, title: 'Kinematics & Dynamics', icon: '⚙️', status: 'online', path: '/docs/module3-robot-kinematics-and-dynamics' },
  { id: 4, title: 'Motion Planning', icon: '🛤️', status: 'online', path: '/docs/module4-robot-motion-planning-and-control' },
  { id: 5, title: 'Robot Learning', icon: '📚', status: 'online', path: '/docs/module5-robot-learning-and-adaptation' },
  { id: 6, title: 'Humanoid Locomotion', icon: '🚶', status: 'online', path: '/docs/module6-humanoid-robot-design-and-locomotion' },
  { id: 7, title: 'Manipulation', icon: '🤖', status: 'online', path: '/docs/module7-humanoid-robot-manipulation-and-interaction' },
  { id: 8, title: 'Reinforcement Learning', icon: '🎯', status: 'online', path: '/docs/module8-reinforcement-learning-for-robotics' },
  { id: 9, title: 'SLAM', icon: '🗺️', status: 'online', path: '/docs/module9-simultaneous-localization-and-mapping-slam' },
  { id: 10, title: 'Human-Robot Interaction', icon: '🤝', status: 'online', path: '/docs/module10-robot-human-interaction' },
  { id: 11, title: 'Ethics & Safety', icon: '⚖️', status: 'online', path: '/docs/module11-robot-ethics-and-safety' },
  { id: 12, title: 'Advanced Topics', icon: '🔬', status: 'online', path: '/docs/module12-advanced-topics-in-physical-ai' },
  { id: 13, title: 'Future of Robotics', icon: '🚀', status: 'online', path: '/docs/module13-future-of-humanoid-robotics-and-ai' },
];

const stats = [
  { label: 'Modules', value: '13', icon: '📦' },
  { label: 'Topics', value: '100+', icon: '📑' },
  { label: 'Code Examples', value: '50+', icon: '💻' },
  { label: 'Glossary Terms', value: '400+', icon: '📖' },
];

function CommandCenterHero() {
  const {siteConfig} = useDocusaurusContext();

  return (
    <header className={styles.heroSection}>
      {/* Animated background */}
      <div className={styles.gridBackground}></div>
      <div className={styles.particles}></div>

      {/* Glowing orbs */}
      <div className={styles.orbCyan}></div>
      <div className={styles.orbPurple}></div>

      <div className={styles.heroContent}>
        {/* Status bar */}
        <div className={styles.statusBar}>
          <span className={styles.statusIndicator}>
            <span className={styles.statusDot}></span>
            SYSTEM ONLINE
          </span>
          <span className={styles.timestamp}>
            {new Date().toLocaleDateString('en-US', {
              weekday: 'short',
              year: 'numeric',
              month: 'short',
              day: 'numeric'
            })}
          </span>
        </div>

        {/* Main title */}
        <div className={styles.titleContainer}>
          <div className={styles.titleGlitch} data-text="PHYSICAL AI">
            PHYSICAL AI
          </div>
          <div className={styles.subtitleGlitch}>
            & HUMANOID ROBOTICS
          </div>
        </div>

        <p className={styles.tagline}>
          {siteConfig.tagline}
        </p>

        {/* CTA Buttons */}
        <div className={styles.ctaContainer}>
          <Link to="/docs/intro" className={styles.ctaPrimary}>
            <span className={styles.ctaIcon}>▶</span>
            INITIALIZE LEARNING SEQUENCE
          </Link>
          <Link to="/docs/module1-ros2-nervous-system" className={styles.ctaSecondary}>
            <span className={styles.ctaIcon}>◉</span>
            MODULE 01: ROS2
          </Link>
        </div>

        {/* Stats */}
        <div className={styles.statsContainer}>
          {stats.map((stat, idx) => (
            <div key={idx} className={styles.statCard}>
              <span className={styles.statIcon}>{stat.icon}</span>
              <span className={styles.statValue}>{stat.value}</span>
              <span className={styles.statLabel}>{stat.label}</span>
            </div>
          ))}
        </div>
      </div>
    </header>
  );
}

function ModuleGrid() {
  return (
    <section className={styles.modulesSection}>
      <div className={styles.sectionHeader}>
        <h2 className={styles.sectionTitle}>
          <span className={styles.titleAccent}>◆</span> COURSE MODULES
        </h2>
        <p className={styles.sectionSubtitle}>
          13 comprehensive modules covering the full spectrum of Physical AI
        </p>
      </div>

      <div className={styles.moduleGrid}>
        {modules.map((module) => (
          <Link
            key={module.id}
            to={module.path}
            className={styles.moduleCard}
          >
            <div className={styles.moduleHeader}>
              <span className={styles.moduleId}>
                {String(module.id).padStart(2, '0')}
              </span>
              <span className={clsx(styles.moduleStatus, styles[module.status])}>
                {module.status.toUpperCase()}
              </span>
            </div>
            <div className={styles.moduleIcon}>{module.icon}</div>
            <h3 className={styles.moduleTitle}>{module.title}</h3>
            <div className={styles.moduleArrow}>→</div>
          </Link>
        ))}
      </div>
    </section>
  );
}

function FeaturesSection() {
  return (
    <section className={styles.featuresSection}>
      <div className={styles.sectionHeader}>
        <h2 className={styles.sectionTitle}>
          <span className={styles.titleAccent}>◆</span> AI-NATIVE FEATURES
        </h2>
      </div>

      <div className={styles.featuresGrid}>
        <div className={styles.featureCard}>
          <div className={styles.featureIcon}>🤖</div>
          <h3>RAG-Powered Chatbot</h3>
          <p>Ask questions about any topic and get instant, contextual answers powered by AI.</p>
        </div>

        <div className={styles.featureCard}>
          <div className={styles.featureIcon}>📝</div>
          <h3>Contextual Queries</h3>
          <p>Select any text and ask specific questions about that content for deeper understanding.</p>
        </div>

        <div className={styles.featureCard}>
          <div className={styles.featureIcon}>🔐</div>
          <h3>Personalized Learning</h3>
          <p>Sign up to track your progress and get content tailored to your background.</p>
        </div>

        <div className={styles.featureCard}>
          <div className={styles.featureIcon}>📊</div>
          <h3>Interactive Diagrams</h3>
          <p>Visual explanations with Mermaid diagrams for complex robotics concepts.</p>
        </div>
      </div>
    </section>
  );
}

function TechStack() {
  return (
    <section className={styles.techSection}>
      <div className={styles.sectionHeader}>
        <h2 className={styles.sectionTitle}>
          <span className={styles.titleAccent}>◆</span> POWERED BY
        </h2>
      </div>

      <div className={styles.techGrid}>
        <div className={styles.techBadge}>Docusaurus</div>
        <div className={styles.techBadge}>FastAPI</div>
        <div className={styles.techBadge}>OpenAI</div>
        <div className={styles.techBadge}>Qdrant</div>
        <div className={styles.techBadge}>React</div>
        <div className={styles.techBadge}>TypeScript</div>
      </div>
    </section>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title="Command Center"
      description="AI-Native Interactive Textbook for Physical AI & Humanoid Robotics">
      <CommandCenterHero />
      <main className={styles.mainContent}>
        <ModuleGrid />
        <FeaturesSection />
        <TechStack />
      </main>
    </Layout>
  );
}
