# Module 2: Robot Sensing and Perception - Assessments

## Quizzes/Short Answer Questions:

1.  **Sensor Categorization:**
    *   **Question:** Describe the key differences between active and passive sensors, providing one example of each commonly used in robotics. Explain a scenario where one type would be preferred over the other.
    *   **Learning Outcome:** Understand different classifications of robot sensors.

2.  **Depth Perception:**
    *   **Question:** Compare and contrast how stereo cameras and Time-of-Flight (ToF) cameras achieve depth perception. Discuss their respective advantages and limitations in a robotic manipulation task involving delicate objects.
    *   **Learning Outcome:** Differentiate between various vision systems and their depth perception mechanisms.

3.  **Lidar vs. Radar:**
    *   **Question:** An autonomous vehicle needs to detect obstacles accurately in heavy fog and at long distances. Which sensing technology, Lidar or Radar, would be more suitable for this specific challenge and why? Elaborate on their complementary nature for robust perception.
    *   **Learning Outcome:** Analyze the strengths and weaknesses of Lidar and Radar in different environmental conditions.

4.  **Proprioceptive vs. Exteroceptive:**
    *   **Question:** Explain the role of proprioceptive sensors (e.g., encoders, IMUs) in maintaining a robot's internal state knowledge, and how this data is distinct from information gathered by exteroceptive sensors (e.g., cameras, lidar). Provide an example where both types of sensors are crucial for a robot's task.
    *   **Learning Outcome:** Understand the function and importance of proprioceptive and exteroceptive sensors.

5.  **Image Processing Fundamentals:**
    *   **Question:** You have a grayscale image from a robot's camera. Describe how edge detection (e.g., Canny) and morphological operations (e.g., erosion, dilation) could be used sequentially to identify and isolate a specific rectangular object with noisy boundaries.
    *   **Learning Outcome:** Apply basic image processing techniques for feature extraction.

## Project Prompts:

1.  **Object Recognition and Grasping with a Simulated Robot Arm (Intermediate):**
    *   **Scenario:** Develop a perception pipeline for a simulated robotic arm to identify and grasp specific objects (e.g., cubes, cylinders, spheres) placed on a table.
    *   **Requirements:**
        *   Utilize a simulated camera (monocular or depth camera) to acquire image/depth data.
        *   Implement an object detection algorithm (e.g., using a pre-trained YOLO model or a simpler feature-based approach like SIFT/SURF if deep learning is out of scope) to locate objects.
        *   Estimate the 6D pose of the target object.
        *   Use the estimated pose to plan and execute a grasping motion with the robot arm.
    *   **Deliverables:** Codebase, video demonstration of the robot successfully grasping objects, a brief report explaining the perception pipeline and challenges faced.
    *   **Learning Outcomes:** Implement vision systems for object detection and pose estimation, apply feature extraction, and integrate perception with robotic manipulation.

2.  **Sensor Fusion for Mobile Robot Localization (Advanced):**
    *   **Scenario:** Design and implement a sensor fusion system for a mobile robot operating in an indoor environment, aiming for accurate localization.
    *   **Requirements:**
        *   Simulate or use provided datasets for IMU data (accelerometer, gyroscope), wheel encoders (odometry), and a simulated 2D Lidar.
        *   Implement a Kalman Filter (EKF or UKF) or a Particle Filter to combine these sensor readings to estimate the robot's 2D position and orientation.
        *   Visually represent the robot's estimated path and the uncertainty ellipse/particle distribution.
    *   **Deliverables:** Codebase, plots/visualizations of localization performance, a technical report detailing the chosen sensor fusion technique, its implementation, and performance analysis (e.g., comparing with individual sensor estimates).
    *   **Learning Outcomes:** Apply sensor fusion techniques (Kalman Filters, Particle Filters), understand trade-offs between different fusion methods, and evaluate localization accuracy.

3.  **Dynamic Obstacle Avoidance with Lidar and Object Tracking (Advanced):**
    *   **Scenario:** Develop a perception and path planning system for an autonomous mobile robot to navigate an environment with both static and dynamic obstacles.
    *   **Requirements:**
        *   Utilize simulated Lidar data to detect obstacles and build a local map.
        *   Implement an object tracking algorithm (e.g., SORT or Deep SORT) to track the movement of dynamic obstacles (e.g., other robots, pedestrians).
        *   Integrate the tracking information into a path planning algorithm that avoids both static and dynamic obstacles.
        *   Demonstrate the robot successfully navigating a cluttered environment while avoiding moving objects.
    *   **Deliverables:** Codebase, video demonstration of the robot's navigation, a report discussing the chosen tracking and path planning algorithms, and the challenges of dynamic environments.
    *   **Learning Outcomes:** Process Lidar point cloud data, implement object tracking, understand challenges in dynamic environments, and integrate perception with navigation.

4.  **AI-Driven Active Sensing Challenge (Advanced Research Project):**
    *   **Scenario:** Explore how reinforcement learning could be used to enable a robot to actively control its sensor placement or movement to improve perception for a specific task (e.g., better identifying a partially occluded object, optimizing view for 3D reconstruction).
    *   **Requirements:**
        *   Define a task and a simulated environment where active sensing would be beneficial.
        *   Design an RL agent that can choose sensor actions (e.g., move camera, change focus) based on its current perception.
        *   Train the RL agent and demonstrate its ability to improve perception compared to a static sensing strategy.
    *   **Deliverables:** Research paper outlining the problem, methodology, experimental setup, results, and discussion; codebase and simulation environment.
    *   **Learning Outcomes:** Apply reinforcement learning to active sensing, understand the concept of end-to-end learning for perception, and address challenges in computational constraints and uncertainty.
