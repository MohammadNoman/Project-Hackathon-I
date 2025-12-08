import React, { useState, useRef, useEffect } from 'react';
import styles from './styles.module.css';

interface Source {
  file: string;
  section: string;
  score: number;
  text_preview?: string;
}

interface Message {
  role: 'user' | 'assistant';
  content: string;
  sources?: Source[];
  timestamp: Date;
}

const API_URL = process.env.NODE_ENV === 'production'
  ? 'https://your-backend-url.com/api/chatbot/query'
  : 'http://localhost:8000/api/chatbot/query';

export default function ChatbotWidget(): JSX.Element {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [sessionId, setSessionId] = useState<string | null>(null);
  const [selectedText, setSelectedText] = useState<string | null>(null);
  const [expandedSources, setExpandedSources] = useState<number | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Load session from localStorage
  useEffect(() => {
    const saved = localStorage.getItem('chatbot_session');
    if (saved) {
      const { sessionId: savedId, messages: savedMsgs } = JSON.parse(saved);
      setSessionId(savedId);
      setMessages(savedMsgs.map((m: any) => ({ ...m, timestamp: new Date(m.timestamp) })));
    }
  }, []);

  // Save session to localStorage
  useEffect(() => {
    if (sessionId && messages.length > 0) {
      localStorage.setItem('chatbot_session', JSON.stringify({ sessionId, messages }));
    }
  }, [sessionId, messages]);

  // Scroll to bottom on new messages
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  // Listen for text selection
  useEffect(() => {
    const handleSelection = () => {
      const selection = window.getSelection()?.toString().trim();
      if (selection && selection.length > 10 && selection.length < 5000) {
        setSelectedText(selection);
      }
    };
    document.addEventListener('mouseup', handleSelection);
    return () => document.removeEventListener('mouseup', handleSelection);
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || loading) return;

    const userMessage: Message = {
      role: 'user',
      content: input + (selectedText ? `\n\n[About selected text: "${selectedText.slice(0, 100)}..."]` : ''),
      timestamp: new Date()
    };

    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          query: input,
          selected_text: selectedText,
          session_id: sessionId
        })
      });

      if (!response.ok) throw new Error('Failed to get response');

      const data = await response.json();

      setSessionId(data.session_id);
      setSelectedText(null);

      const assistantMessage: Message = {
        role: 'assistant',
        content: data.answer,
        sources: data.sources,
        timestamp: new Date()
      };

      setMessages(prev => [...prev, assistantMessage]);
    } catch (error) {
      const errorMessage: Message = {
        role: 'assistant',
        content: 'Sorry, I encountered an error. Please try again.',
        timestamp: new Date()
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  const clearChat = () => {
    setMessages([]);
    setSessionId(null);
    localStorage.removeItem('chatbot_session');
  };

  const toggleSources = (index: number) => {
    setExpandedSources(expandedSources === index ? null : index);
  };

  return (
    <div className={styles.container}>
      {/* Floating Button */}
      <button
        className={`${styles.floatingButton} ${isOpen ? styles.hidden : ''}`}
        onClick={() => setIsOpen(true)}
        aria-label="Open chat"
      >
        <svg viewBox="0 0 24 24" fill="currentColor" width="28" height="28">
          <path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H6l-2 2V4h16v12z"/>
        </svg>
      </button>

      {/* Chat Panel */}
      {isOpen && (
        <div className={styles.chatPanel}>
          {/* Header */}
          <div className={styles.header}>
            <h3>AI Assistant</h3>
            <div className={styles.headerActions}>
              <button onClick={clearChat} title="Clear chat" className={styles.iconButton}>
                <svg viewBox="0 0 24 24" fill="currentColor" width="18" height="18">
                  <path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"/>
                </svg>
              </button>
              <button onClick={() => setIsOpen(false)} className={styles.iconButton}>
                <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20">
                  <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
                </svg>
              </button>
            </div>
          </div>

          {/* Messages */}
          <div className={styles.messages}>
            {messages.length === 0 && (
              <div className={styles.welcome}>
                <p>Hi! I'm your AI assistant for the Physical AI Textbook.</p>
                <p>Ask me anything about robotics, AI, or the course content.</p>
                {selectedText && (
                  <div className={styles.selectedTextHint}>
                    <strong>Tip:</strong> I noticed you selected some text. Ask a question and I'll use it as context!
                  </div>
                )}
              </div>
            )}

            {messages.map((msg, idx) => (
              <div key={idx} className={`${styles.message} ${styles[msg.role]}`}>
                <div className={styles.messageContent}>
                  {msg.content}
                </div>

                {/* Sources */}
                {msg.sources && msg.sources.length > 0 && (
                  <div className={styles.sources}>
                    <button
                      className={styles.sourcesToggle}
                      onClick={() => toggleSources(idx)}
                    >
                      {expandedSources === idx ? '▼' : '▶'} {msg.sources.length} sources
                    </button>
                    {expandedSources === idx && (
                      <ul className={styles.sourcesList}>
                        {msg.sources.map((src, srcIdx) => (
                          <li key={srcIdx} className={styles.sourceItem}>
                            <span className={styles.sourceFile}>{src.file}</span>
                            <span className={styles.sourceScore}>
                              {Math.round(src.score * 100)}% match
                            </span>
                          </li>
                        ))}
                      </ul>
                    )}
                  </div>
                )}
              </div>
            ))}

            {loading && (
              <div className={`${styles.message} ${styles.assistant}`}>
                <div className={styles.typing}>
                  <span></span><span></span><span></span>
                </div>
              </div>
            )}

            <div ref={messagesEndRef} />
          </div>

          {/* Selected Text Indicator */}
          {selectedText && (
            <div className={styles.selectedTextBar}>
              <span>Using selected text as context</span>
              <button onClick={() => setSelectedText(null)}>✕</button>
            </div>
          )}

          {/* Input */}
          <form onSubmit={handleSubmit} className={styles.inputForm}>
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask a question..."
              disabled={loading}
              className={styles.input}
            />
            <button type="submit" disabled={loading || !input.trim()} className={styles.sendButton}>
              <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20">
                <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/>
              </svg>
            </button>
          </form>
        </div>
      )}
    </div>
  );
}
