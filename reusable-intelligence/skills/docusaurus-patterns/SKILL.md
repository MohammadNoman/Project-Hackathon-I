# Docusaurus Patterns Skill

Common Docusaurus component patterns, configuration, and React component templates for interactive book features.

## Custom React Component Template

```tsx
import React from 'react';
import styles from './styles.module.css';

interface MyComponentProps {
  title: string;
  children: React.ReactNode;
}

export default function MyComponent({ title, children }: MyComponentProps): JSX.Element {
  return (
    <div className={styles.container}>
      <h3>{title}</h3>
      <div className={styles.content}>
        {children}
      </div>
    </div>
  );
}
```

## Module CSS Pattern

```css
/* src/components/MyComponent/styles.module.css */
.container {
  border: 1px solid var(--ifm-color-emphasis-300);
  border-radius: var(--ifm-border-radius);
  padding: 1rem;
  margin: 1rem 0;
}

.content {
  margin-top: 0.5rem;
}
```

## Interactive Chatbot Widget Pattern

```tsx
import React, { useState } from 'react';

export default function ChatbotWidget(): JSX.Element {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      const res = await fetch('http://localhost:8000/api/chatbot/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query_text: query })
      });
      
      const data = await res.json();
      setResponse(data.response_text);
    } catch (error) {
      setResponse('Error: Unable to get response');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chatbot-widget">
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask a question..."
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Loading...' : 'Ask'}
        </button>
      </form>
      {response && <div className="response">{response}</div>}
    </div>
  );
}
```

## MDX Integration Pattern

```mdx
---
sidebar_position: 1
---

# Module 1: Introduction

import MyComponent from '@site/src/components/MyComponent';

<MyComponent title="Learning Objectives">
  - Understand ROS2 fundamentals
  - Set up ROS2 environment
  - Create basic nodes
</MyComponent>

Regular markdown content here...
```

## Sidebar Configuration

```js
// sidebars.js
module.exports = {
  tutorialSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Module 1: ROS2',
      items: [
        'module1/introduction',
        'module1/setup',
        'module1/nodes',
      ],
    },
  ],
};
```

## Custom Theme Colors

```css
/* src/css/custom.css */
:root {
  --ifm-color-primary: #2e8555;
  --ifm-color-primary-dark: #29784c;
  --ifm-color-primary-darker: #277148;
  --ifm-code-font-size: 95%;
}

[data-theme='dark'] {
  --ifm-color-primary: #25c2a0;
  --ifm-color-primary-dark: #21af90;
}
```

## Use These Patterns

When building Docusaurus components and pages, reference these patterns for consistency and best practices.
