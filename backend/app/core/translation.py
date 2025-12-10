"""Content translation service for multilingual support."""

import logging
from typing import Dict, Any, Optional
from datetime import datetime
import re

logger = logging.getLogger(__name__)


class TranslationService:
    """Service for translating educational content to Urdu and other languages."""

    def __init__(self):
        self.chat_model = "gpt-4-turbo-preview"
        self._openai_client = None

    @property
    def openai_client(self):
        if self._openai_client is None:
            from openai import OpenAI
            from app.core.config import settings
            self._openai_client = OpenAI(api_key=settings.openai_api_key)
        return self._openai_client

    def create_translation_prompt(
        self,
        content: str,
        target_language: str,
        language_name: str
    ) -> str:
        """
        Create a prompt for content translation.

        Args:
            content: Original chapter content in English
            target_language: ISO 639-1 language code (e.g., "ur" for Urdu)
            language_name: Full name of target language (e.g., "Urdu")

        Returns:
            Formatted prompt for OpenAI
        """
        return f"""You are an expert technical translator specializing in educational content about Physical AI, Robotics, and Machine Learning.

TASK:
Translate the following English content into {language_name} while maintaining technical accuracy and educational clarity.

ORIGINAL CONTENT (ENGLISH):
{content}

TRANSLATION GUIDELINES:

1. **Technical Terms and Jargon:**
   - Keep core technical terms in English (e.g., "neural networks", "LIDAR", "CNN", "PyTorch", "ROS 2")
   - Add {language_name} translation in parentheses on first occurrence
   - Example: "Neural Networks (نیورل نیٹ ورکس)" or "LIDAR (لیڈار)"

2. **Code Blocks and Examples:**
   - Keep ALL code blocks, function names, variable names, and programming syntax in English
   - Translate only code comments to {language_name}
   - Preserve markdown code fence formatting (```python, etc.)

3. **Markdown Formatting:**
   - Preserve ALL markdown syntax (headings #, lists -, bold **, italic *, code `)
   - Maintain document structure exactly as in original
   - Keep URLs and links in their original form

4. **Mathematical Notation:**
   - Keep mathematical equations and formulas in their original form
   - Use English variable names in equations
   - Translate only the explanatory text around equations

5. **Technical Accuracy:**
   - Ensure translations maintain the precise technical meaning
   - Use standard {language_name} technical vocabulary when available
   - If no standard term exists, use English term with transliteration

6. **Readability:**
   - Use natural, flowing {language_name} language
   - Adapt sentence structure to {language_name} grammar while preserving meaning
   - Maintain the educational tone and accessibility of the original

7. **Special Handling for {language_name}:**
   {"- Use proper Urdu/Arabic script (Nastaliq style)" if target_language == "ur" else ""}
   {"- Ensure right-to-left (RTL) text flow compatibility" if target_language == "ur" else ""}
   {"- Use appropriate Urdu technical terminology from standard educational sources" if target_language == "ur" else ""}

OUTPUT:
Return ONLY the translated content. Do not add meta-commentary, explanations, or notes about the translation process.
Maintain the exact same structure and formatting as the original.
"""

    def translate_content(
        self,
        chapter_content: str,
        target_language: str = "ur"
    ) -> Dict[str, Any]:
        """
        Translate chapter content to target language.

        Args:
            chapter_content: Original chapter text in English
            target_language: ISO 639-1 language code (default: "ur" for Urdu)

        Returns:
            Dictionary containing translated content and metadata
        """
        start_time = datetime.utcnow()

        # Map language codes to names
        language_names = {
            "ur": "Urdu",
            "ar": "Arabic",
            "hi": "Hindi",
            "es": "Spanish",
            "fr": "French",
            "de": "German",
            "zh": "Chinese",
            "ja": "Japanese"
        }

        language_name = language_names.get(target_language, "Unknown")

        if language_name == "Unknown":
            raise ValueError(f"Unsupported language code: {target_language}")

        logger.info(
            f"Translating content to {language_name} ({target_language})"
        )

        try:
            # Create translation prompt
            prompt = self.create_translation_prompt(
                content=chapter_content,
                target_language=target_language,
                language_name=language_name
            )

            # Generate translation
            response = self.openai_client.chat.completions.create(
                model=self.chat_model,
                messages=[
                    {
                        "role": "system",
                        "content": f"You are an expert technical translator specializing in educational content about AI and Robotics. You translate content to {language_name} while preserving technical accuracy."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,  # Lower temperature for more accurate translation
                max_tokens=4000
            )

            translated_text = response.choices[0].message.content
            tokens_used = response.usage.total_tokens
            processing_time = (datetime.utcnow() - start_time).total_seconds() * 1000

            logger.info(
                f"Translation complete: {tokens_used} tokens, "
                f"{processing_time:.0f}ms"
            )

            return {
                "translated_content": translated_text,
                "target_language": target_language,
                "language_name": language_name,
                "tokens_used": tokens_used,
                "processing_time_ms": processing_time,
                "original_length": len(chapter_content),
                "translated_length": len(translated_text)
            }

        except Exception as e:
            logger.error(f"Translation failed: {e}", exc_info=True)
            raise RuntimeError(f"Content translation failed: {e}")

    def get_sample_content(self, chapter_id: str) -> str:
        """
        Get sample content for a chapter (placeholder).

        In production, this would fetch from a database or content store.

        Args:
            chapter_id: Chapter identifier

        Returns:
            Chapter content as string
        """
        # Sample content for demonstration
        sample_chapters = {
            "module1": """# Introduction to Physical AI

Physical AI represents the convergence of artificial intelligence with physical systems, particularly robotics. This field combines machine learning algorithms with mechanical systems to create intelligent machines that can perceive, reason, and act in the physical world.

## Key Concepts

**Embodied Intelligence**: Unlike pure software AI, Physical AI systems must deal with the constraints and opportunities of having a physical form. This includes sensor noise, actuator limitations, and real-time processing requirements.

**Sensor Fusion**: Robots use multiple sensors (cameras, LIDAR, IMUs) to build a comprehensive understanding of their environment. Machine learning algorithms process this data to create actionable insights.

**Control Systems**: Physical AI integrates classical control theory with modern learning-based approaches. PID controllers work alongside neural networks to achieve precise, adaptive motion.

## Applications

- Autonomous vehicles navigating complex environments
- Manufacturing robots learning to manipulate diverse objects
- Humanoid robots performing tasks in human-designed spaces
- Agricultural robots adapting to varying field conditions

## Technical Stack

Modern Physical AI systems typically combine:
- Deep learning frameworks (PyTorch, TensorFlow)
- Robotics middleware (ROS 2)
- Simulation environments (Gazebo, Isaac Sim)
- Embedded systems (Jetson, Raspberry Pi)
- Real-time operating systems for critical control loops
""",
            "module2": """# Sensors and Perception

Perception is the foundation of Physical AI - robots must sense their environment before they can act intelligently within it. This module covers the primary sensor modalities and perception algorithms.

## Vision Systems

**Cameras**: RGB cameras provide rich visual information but require sophisticated processing to extract meaning. Depth cameras (stereo, structured light, ToF) add 3D understanding.

**Computer Vision Pipeline**:
1. Image acquisition and preprocessing
2. Feature extraction (edges, corners, descriptors)
3. Object detection and recognition
4. Scene understanding and segmentation

**Deep Learning for Vision**: Convolutional Neural Networks (CNNs) have revolutionized robot vision. Key architectures include ResNet for classification, YOLO for detection, and U-Net for segmentation.

## LIDAR and Range Sensors

LIDAR provides precise 3D point clouds of the environment, essential for navigation and mapping. Processing pipeline includes:
- Point cloud filtering and downsampling
- Ground plane removal
- Object clustering and classification
- Occupancy grid generation

## Inertial Measurement Units (IMUs)

IMUs measure acceleration and angular velocity, providing crucial data for:
- Orientation estimation (sensor fusion with Kalman filters)
- Motion tracking and odometry
- Vibration detection for fault diagnosis

## Sensor Fusion Strategies

Combining multiple sensors provides robustness. Extended Kalman Filters (EKF) and particle filters merge sensor streams to estimate robot state with uncertainty quantification.
"""
        }

        return sample_chapters.get(
            chapter_id,
            "# Chapter Not Found\n\nThis is placeholder content for demonstration."
        )


# Global translation service instance
translation_service = TranslationService()
