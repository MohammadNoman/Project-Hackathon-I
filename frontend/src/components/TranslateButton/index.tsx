import React, { useState, useEffect } from 'react';
import styles from './styles.module.css';

interface TranslateResponse {
  translated_content: string;
  target_language: string;
  language_name: string;
  chapter_id: string;
  user_id?: string;
  tokens_used?: number;
  processing_time_ms?: number;
  original_length?: number;
  translated_length?: number;
}

interface TranslateButtonProps {
  chapterId: string;
  content?: string;
  onTranslated?: (translatedContent: string, language: string) => void;
  className?: string;
}

const API_URL = process.env.NODE_ENV === 'production'
  ? 'https://your-backend-url.com/api/translate'
  : 'http://localhost:8000/api/translate';

export default function TranslateButton({
  chapterId,
  content,
  onTranslated,
  className
}: TranslateButtonProps): JSX.Element {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<TranslateResponse | null>(null);
  const [showResult, setShowResult] = useState(false);
  const [targetLanguage, setTargetLanguage] = useState<string>('ur');

  const handleTranslate = async () => {
    setError(null);
    setLoading(true);

    try {
      const response = await fetch(`${API_URL}/${chapterId}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          target_language: targetLanguage,
          content: content || null,
          user_id: localStorage.getItem('user_id') || null
        })
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to translate content');
      }

      const data: TranslateResponse = await response.json();
      setResult(data);
      setShowResult(true);

      // Call parent callback if provided
      if (onTranslated) {
        onTranslated(data.translated_content, data.target_language);
      }

    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  const closeResult = () => {
    setShowResult(false);
  };

  // Get display text for Urdu button
  const getButtonText = () => {
    if (targetLanguage === 'ur') {
      return 'اردو میں پڑھیں';  // "Read in Urdu"
    }
    return 'Translate';
  };

  return (
    <div className={`${styles.container} ${className || ''}`}>
      {/* Translate Button */}
      <button
        className={styles.translateButton}
        onClick={handleTranslate}
        disabled={loading}
        title="Translate this chapter to Urdu"
      >
        <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20">
          <path d="M12.87 15.07l-2.54-2.51.03-.03c1.74-1.94 2.98-4.17 3.71-6.53H17V4h-7V2H8v2H1v1.99h11.17C11.5 7.92 10.44 9.75 9 11.35 8.07 10.32 7.3 9.19 6.69 8h-2c.73 1.63 1.73 3.17 2.98 4.56l-5.09 5.02L4 19l5-5 3.11 3.11.76-2.04zM18.5 10h-2L12 22h2l1.12-3h4.75L21 22h2l-4.5-12zm-2.62 7l1.62-4.33L19.12 17h-3.24z"/>
        </svg>
        <span className={targetLanguage === 'ur' ? styles.urduText : ''}>
          {loading ? 'Translating...' : getButtonText()}
        </span>
      </button>

      {/* Error Message */}
      {error && (
        <div className={styles.errorBanner}>
          <span>{error}</span>
          <button onClick={() => setError(null)} className={styles.closeError}>×</button>
        </div>
      )}

      {/* Result Modal */}
      {showResult && result && (
        <div className={styles.modal} onClick={closeResult}>
          <div className={styles.resultContent} onClick={(e) => e.stopPropagation()}>
            <div className={styles.modalHeader}>
              <h3>Translated Content</h3>
              <button onClick={closeResult} className={styles.closeButton}>
                <svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24">
                  <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
                </svg>
              </button>
            </div>

            <div className={styles.resultBody}>
              {/* Translation Info */}
              <div className={styles.infoCard}>
                <h4>Translated to {result.language_name}</h4>
                <div className={styles.languageInfo}>
                  <div className={styles.infoItem}>
                    <span className={styles.infoLabel}>Language:</span>
                    <span className={styles.languageBadge}>
                      {result.language_name} ({result.target_language.toUpperCase()})
                    </span>
                  </div>
                </div>
                {result.processing_time_ms && (
                  <div className={styles.stats}>
                    Translated in {Math.round(result.processing_time_ms)}ms
                    {result.tokens_used && ` • ${result.tokens_used} tokens`}
                    {result.original_length && result.translated_length &&
                      ` • ${result.original_length} → ${result.translated_length} chars`
                    }
                  </div>
                )}
              </div>

              {/* Translated Content with RTL Support */}
              <div className={styles.content}>
                <div className={styles.contentLabel}>
                  {result.target_language === 'ur' || result.target_language === 'ar'
                    ? <span className={styles.urduText}>ترجمہ شدہ مواد:</span>
                    : 'Translated Content:'}
                </div>
                <div
                  className={`${styles.contentText} ${
                    (result.target_language === 'ur' || result.target_language === 'ar')
                      ? styles.rtlText
                      : ''
                  }`}
                >
                  {/* Render markdown-style content */}
                  {result.translated_content.split('\n\n').map((section, idx) => {
                    // Handle headings
                    if (section.startsWith('# ')) {
                      return <h1 key={idx} className={styles.heading1}>{section.substring(2)}</h1>;
                    } else if (section.startsWith('## ')) {
                      return <h2 key={idx} className={styles.heading2}>{section.substring(3)}</h2>;
                    } else if (section.startsWith('### ')) {
                      return <h3 key={idx} className={styles.heading3}>{section.substring(4)}</h3>;
                    }

                    // Handle code blocks
                    if (section.startsWith('```')) {
                      const codeContent = section.substring(section.indexOf('\n') + 1, section.lastIndexOf('```'));
                      return (
                        <pre key={idx} className={styles.codeBlock}>
                          <code>{codeContent}</code>
                        </pre>
                      );
                    }

                    // Handle bullet lists
                    if (section.includes('\n- ')) {
                      const items = section.split('\n').filter(line => line.startsWith('- '));
                      return (
                        <ul key={idx} className={styles.list}>
                          {items.map((item, itemIdx) => (
                            <li key={itemIdx}>{item.substring(2)}</li>
                          ))}
                        </ul>
                      );
                    }

                    // Regular paragraphs
                    return section.trim() ? (
                      <p key={idx} className={styles.paragraph}>
                        {section.split('\n').map((line, lineIdx) => (
                          <React.Fragment key={lineIdx}>
                            {line}
                            {lineIdx < section.split('\n').length - 1 && <br />}
                          </React.Fragment>
                        ))}
                      </p>
                    ) : null;
                  })}
                </div>
              </div>
            </div>

            <div className={styles.modalFooter}>
              <button onClick={closeResult} className={styles.closeButtonFooter}>
                Close
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
