import React, { useState, useEffect } from 'react';
import styles from './styles.module.css';

interface PersonalizationParams {
  software_level: string;
  hardware_level: string;
  software_background: string;
  hardware_background: string;
}

interface PersonalizeResponse {
  personalized_content: string;
  personalization_params: PersonalizationParams;
  chapter_id: string;
  user_id?: string;
  tokens_used?: number;
  processing_time_ms?: number;
}

interface PersonalizeButtonProps {
  chapterId: string;
  onPersonalized?: (content: string, params: PersonalizationParams) => void;
  className?: string;
}

const API_URL = process.env.NODE_ENV === 'production'
  ? 'https://your-backend-url.com/api/personalize'
  : 'http://localhost:8000/api/personalize';

export default function PersonalizeButton({
  chapterId,
  onPersonalized,
  className
}: PersonalizeButtonProps): JSX.Element {
  const [isOpen, setIsOpen] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [softwareBackground, setSoftwareBackground] = useState('');
  const [hardwareBackground, setHardwareBackground] = useState('');
  const [result, setResult] = useState<PersonalizeResponse | null>(null);
  const [showResult, setShowResult] = useState(false);

  // Load saved backgrounds from localStorage
  useEffect(() => {
    const saved = localStorage.getItem('user_backgrounds');
    if (saved) {
      try {
        const { software, hardware } = JSON.parse(saved);
        setSoftwareBackground(software || '');
        setHardwareBackground(hardware || '');
      } catch (e) {
        console.error('Failed to load saved backgrounds:', e);
      }
    }
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);

    if (!softwareBackground && !hardwareBackground) {
      setError('Please provide at least one background description');
      return;
    }

    setLoading(true);

    try {
      const response = await fetch(`${API_URL}/${chapterId}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          software_background: softwareBackground,
          hardware_background: hardwareBackground,
          user_id: localStorage.getItem('user_id') || null
        })
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to personalize content');
      }

      const data: PersonalizeResponse = await response.json();

      // Save backgrounds for future use
      localStorage.setItem('user_backgrounds', JSON.stringify({
        software: softwareBackground,
        hardware: hardwareBackground
      }));

      setResult(data);
      setShowResult(true);
      setIsOpen(false);

      // Call parent callback if provided
      if (onPersonalized) {
        onPersonalized(data.personalized_content, data.personalization_params);
      }

    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  const closeModal = () => {
    setIsOpen(false);
    setError(null);
  };

  const closeResult = () => {
    setShowResult(false);
  };

  return (
    <div className={`${styles.container} ${className || ''}`}>
      {/* Personalize Button */}
      <button
        className={styles.personalizeButton}
        onClick={() => setIsOpen(true)}
        title="Personalize this chapter to your background"
      >
        <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20">
          <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z"/>
        </svg>
        <span>Personalize</span>
      </button>

      {/* Input Modal */}
      {isOpen && (
        <div className={styles.modal} onClick={closeModal}>
          <div className={styles.modalContent} onClick={(e) => e.stopPropagation()}>
            <div className={styles.modalHeader}>
              <h3>Personalize Content</h3>
              <button onClick={closeModal} className={styles.closeButton}>
                <svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24">
                  <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
                </svg>
              </button>
            </div>

            <form onSubmit={handleSubmit} className={styles.form}>
              <div className={styles.formGroup}>
                <label htmlFor="software">
                  Software/Programming Background
                  <span className={styles.hint}>
                    (e.g., "Beginner in Python, no ML experience" or "Senior engineer with deep learning expertise")
                  </span>
                </label>
                <textarea
                  id="software"
                  value={softwareBackground}
                  onChange={(e) => setSoftwareBackground(e.target.value)}
                  placeholder="Describe your software and programming experience..."
                  rows={3}
                  className={styles.textarea}
                />
              </div>

              <div className={styles.formGroup}>
                <label htmlFor="hardware">
                  Hardware/Robotics Background
                  <span className={styles.hint}>
                    (e.g., "No robotics experience" or "Built several Arduino projects")
                  </span>
                </label>
                <textarea
                  id="hardware"
                  value={hardwareBackground}
                  onChange={(e) => setHardwareBackground(e.target.value)}
                  placeholder="Describe your hardware and robotics experience..."
                  rows={3}
                  className={styles.textarea}
                />
              </div>

              {error && (
                <div className={styles.error}>
                  {error}
                </div>
              )}

              <div className={styles.modalFooter}>
                <button
                  type="button"
                  onClick={closeModal}
                  className={styles.cancelButton}
                  disabled={loading}
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className={styles.submitButton}
                  disabled={loading}
                >
                  {loading ? (
                    <>
                      <span className={styles.spinner}></span>
                      Personalizing...
                    </>
                  ) : (
                    'Personalize Content'
                  )}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Result Modal */}
      {showResult && result && (
        <div className={styles.modal} onClick={closeResult}>
          <div className={styles.resultContent} onClick={(e) => e.stopPropagation()}>
            <div className={styles.modalHeader}>
              <h3>Personalized Content</h3>
              <button onClick={closeResult} className={styles.closeButton}>
                <svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24">
                  <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
                </svg>
              </button>
            </div>

            <div className={styles.resultBody}>
              {/* Personalization Info */}
              <div className={styles.infoCard}>
                <h4>Adapted for Your Background</h4>
                <div className={styles.levels}>
                  <div className={styles.level}>
                    <span className={styles.levelLabel}>Software:</span>
                    <span className={`${styles.levelBadge} ${styles[result.personalization_params.software_level]}`}>
                      {result.personalization_params.software_level}
                    </span>
                  </div>
                  <div className={styles.level}>
                    <span className={styles.levelLabel}>Hardware:</span>
                    <span className={`${styles.levelBadge} ${styles[result.personalization_params.hardware_level]}`}>
                      {result.personalization_params.hardware_level}
                    </span>
                  </div>
                </div>
                {result.processing_time_ms && (
                  <div className={styles.stats}>
                    Processed in {Math.round(result.processing_time_ms)}ms
                    {result.tokens_used && ` • ${result.tokens_used} tokens`}
                  </div>
                )}
              </div>

              {/* Personalized Content */}
              <div className={styles.content}>
                <div className={styles.contentLabel}>Personalized Content:</div>
                <div className={styles.contentText}>
                  {result.personalized_content.split('\n').map((paragraph, idx) => (
                    <p key={idx}>{paragraph}</p>
                  ))}
                </div>
              </div>
            </div>

            <div className={styles.modalFooter}>
              <button onClick={closeResult} className={styles.submitButton}>
                Close
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
