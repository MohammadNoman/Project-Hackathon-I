import React from 'react';
import ChatbotWidget from '@site/src/components/ChatbotWidget';

// Wraps the entire Docusaurus app to add global components
export default function Root({ children }: { children: React.ReactNode }): JSX.Element {
  return (
    <>
      {children}
      <ChatbotWidget />
    </>
  );
}
