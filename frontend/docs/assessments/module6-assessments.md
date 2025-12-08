## Module 6: Humanoid Robot Design and Locomotion - Assessments

### Quizzes/Conceptual Checks

1.  **Humanoid Robot Fundamentals:**
    *   **Question Type:** Multiple Choice
    *   **Prompt:** Which of the following is NOT a primary advantage of humanoid robots operating in human environments?
        a) Navigating stairs
        b) Opening doors
        c) Mimicking human tasks requiring dexterity
        d) High energy efficiency compared to wheeled robots
    *   **Learning Outcome Assessed:** Understanding advantages and applications of humanoid robots.

2.  **Degrees of Freedom and Kinematics:**
    *   **Question Type:** Fill-in-the-blank
    *   **Prompt:** The number of independent parameters that define the configuration of a robotic system is known as \_\_\_\_\_\_\_\_\_\_\_\_.
    *   **Learning Outcome Assessed:** Understanding key anatomical concepts like DoF.

3.  **Sensor Matching:**
    *   **Question Type:** Matching
    *   **Prompt:** Match the sensor type to its primary function in a humanoid robot:
        1.  IMU
        2.  Force/Torque Sensor
        3.  Proprioceptive Sensor
        4.  Vision System
        a) Measures joint angles/positions
        b) Provides orientation and angular velocity data for balance
        c) Detects objects and maps surroundings
        d) Measures ground contact forces
    *   **Learning Outcome Assessed:** Identifying and understanding the function of various humanoid robot sensors.

4.  **Actuator Characteristics:**
    *   **Question Type:** True/False
    *   **Prompt:** Hydraulic actuators offer high power density but are generally less complex and cleaner than electric motors. (True/False)
    *   **Learning Outcome Assessed:** Comparing and contrasting different actuation systems.

5.  **Balance and Stability Concepts:**
    *   **Question Type:** Short Answer
    *   **Prompt:** Explain the relationship between the Center of Mass (CoM), Zero Moment Point (ZMP), and the Support Polygon in maintaining a humanoid robot's stability during locomotion.
    *   **Learning Outcome Assessed:** Understanding fundamental balance and stability metrics.

### Project Prompts

1.  **Humanoid Gait Design and Simulation:**
    *   **Prompt:** Design a simple static walking gait for a 2D humanoid robot model (e.g., a stick figure with 2-3 joints per leg). Define the sequence of CoM and ZMP movements relative to the support polygon. You can use a simulation environment (e.g., PyBullet, Gazebo) or describe the kinematic and dynamic considerations in detail with diagrams. Discuss the trade-offs between static and dynamic walking for this gait.
    *   **Learning Outcomes Assessed:** Applying concepts of CoM, ZMP, support polygon, and walking gaits; understanding kinematic and dynamic constraints.

2.  **Actuator Selection and Justification:**
    *   **Prompt:** You are tasked with designing a humanoid robot for elder care assistance in a home environment. Based on the requirements (e.g., safety, quiet operation, ability to manipulate delicate objects, extended battery life), propose the most suitable actuation system (electric, hydraulic, pneumatic, or SEAs) for the robot's major joints (hips, knees, ankles, shoulders, elbows). Justify your choices by discussing the advantages and disadvantages of each system in the context of the application.
    *   **Learning Outcomes Assessed:** Analyzing and applying knowledge of actuation systems; considering design considerations like safety, power management, and energy efficiency.

3.  **Balance Control Strategy Implementation (Conceptual or Pseudocode):**
    *   **Prompt:** Develop a conceptual design or pseudocode for a basic ZMP-based balance control strategy for a humanoid robot. Your design should outline how sensor inputs (e.g., IMU, force/torque sensors) would be used to estimate CoM and ZMP, and how joint torques or positions would be adjusted to keep the ZMP within the support polygon during a single-support phase of walking.
    *   **Learning Outcomes Assessed:** Understanding balance control strategies; integrating sensor data and control objectives.

4.  **Future Trends Research and Presentation:**
    *   **Prompt:** Research one of the "Future Trends" topics discussed in the module (e.g., Soft Robotics for Humanoids, Advanced Perception for Navigation, Dexterous Manipulation). Prepare a short report or presentation (5-7 slides) that:
        *   Explains the current state of research in that area.
        *   Identifies key challenges and recent breakthroughs.
        *   Discusses the potential impact of this trend on the future capabilities and applications of humanoid robots.
        *   Suggests a novel application or improvement that this trend could enable.
    *   **Learning Outcomes Assessed:** Exploring advanced topics in humanoid robotics; critical analysis and synthesis of information; envisioning future applications.