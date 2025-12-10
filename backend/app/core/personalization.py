"""Content personalization service for adaptive learning."""

import logging
from typing import Dict, Any, Optional, List
from datetime import datetime

logger = logging.getLogger(__name__)


class PersonalizationService:
    """Service for personalizing educational content based on user background."""

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

    def get_background_level(self, background: str) -> str:
        """
        Determine expertise level from background description.

        Args:
            background: User's background description

        Returns:
            One of: 'beginner', 'intermediate', 'advanced'
        """
        background_lower = background.lower()

        # Advanced indicators
        advanced_keywords = [
            'expert', 'professional', 'senior', 'lead', 'architect',
            'phd', 'research', 'extensive', 'years of experience',
            'advanced', 'master', 'specialist'
        ]

        # Beginner indicators
        beginner_keywords = [
            'new', 'beginner', 'learning', 'student', 'no experience',
            'starting', 'basic', 'fundamental', 'introductory'
        ]

        # Check for advanced
        if any(keyword in background_lower for keyword in advanced_keywords):
            return 'advanced'

        # Check for beginner
        if any(keyword in background_lower for keyword in beginner_keywords):
            return 'beginner'

        # Default to intermediate
        return 'intermediate'

    def create_personalization_prompt(
        self,
        content: str,
        software_level: str,
        hardware_level: str,
        software_background: str,
        hardware_background: str
    ) -> str:
        """
        Create a prompt for content personalization.

        Args:
            content: Original chapter content
            software_level: beginner/intermediate/advanced
            hardware_level: beginner/intermediate/advanced
            software_background: User's software background description
            hardware_background: User's hardware background description

        Returns:
            Formatted prompt for OpenAI
        """
        return f"""You are an expert educator personalizing content for a Physical AI and Robotics textbook.

USER PROFILE:
- Software Background ({software_level}): {software_background or 'Not specified'}
- Hardware Background ({hardware_level}): {hardware_background or 'Not specified'}

ORIGINAL CONTENT:
{content}

TASK:
Adapt the above content for this specific learner while maintaining accuracy and depth.

GUIDELINES:

For SOFTWARE ({software_level}):
- Beginner: Explain programming concepts clearly, provide code examples with detailed comments, compare to familiar concepts
- Intermediate: Reference relevant frameworks/patterns, moderate technical detail, focus on practical implementation
- Advanced: Use technical terminology freely, discuss architectural decisions, highlight optimization opportunities

For HARDWARE ({hardware_level}):
- Beginner: Explain physical components simply, use analogies, define technical terms, visual descriptions
- Intermediate: Reference common hardware platforms, balance theory and practice, discuss trade-offs
- Advanced: Deep dive into specifications, discuss design considerations, reference advanced topics

PERSONALIZATION STRATEGIES:
1. Adjust technical terminology density based on expertise
2. Add relevant examples from user's background when applicable
3. Emphasize areas where user may need more support
4. Leverage user's strengths to explain new concepts
5. Maintain same core information but adjust presentation style

OUTPUT:
Return ONLY the personalized content. Do not add meta-commentary or explanations about the personalization itself.
Keep the same structure and ensure all key concepts are covered.
"""

    def personalize_content(
        self,
        chapter_content: str,
        software_background: str,
        hardware_background: str
    ) -> Dict[str, Any]:
        """
        Personalize chapter content based on user's background.

        Args:
            chapter_content: Original chapter text
            software_background: User's software background
            hardware_background: User's hardware background

        Returns:
            Dictionary containing personalized content and metadata
        """
        start_time = datetime.utcnow()

        try:
            # Determine expertise levels
            software_level = self.get_background_level(software_background)
            hardware_level = self.get_background_level(hardware_background)

            logger.info(
                f"Personalizing content: SW={software_level}, HW={hardware_level}"
            )

            # Create personalization prompt
            prompt = self.create_personalization_prompt(
                content=chapter_content,
                software_level=software_level,
                hardware_level=hardware_level,
                software_background=software_background,
                hardware_background=hardware_background
            )

            # Generate personalized content
            response = self.openai_client.chat.completions.create(
                model=self.chat_model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert educational content adapter specializing in robotics and AI."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=3000
            )

            personalized_text = response.choices[0].message.content
            tokens_used = response.usage.total_tokens
            processing_time = (datetime.utcnow() - start_time).total_seconds() * 1000

            logger.info(
                f"Personalization complete: {tokens_used} tokens, "
                f"{processing_time:.0f}ms"
            )

            return {
                "personalized_content": personalized_text,
                "personalization_params": {
                    "software_level": software_level,
                    "hardware_level": hardware_level,
                    "software_background": software_background,
                    "hardware_background": hardware_background
                },
                "tokens_used": tokens_used,
                "processing_time_ms": processing_time
            }

        except Exception as e:
            logger.error(f"Personalization failed: {e}", exc_info=True)
            raise RuntimeError(f"Content personalization failed: {e}")

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


# Global personalization service instance
personalization_service = PersonalizationService()
