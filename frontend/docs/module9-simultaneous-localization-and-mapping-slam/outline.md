# Module 9: Simultaneous Localization and Mapping (SLAM)

## 1. Introduction to SLAM
*   Definition of SLAM
*   The "SLAM Problem" explained
*   Importance and applications in robotics (autonomous navigation, AR/VR, drones)
*   Brief history and evolution of SLAM

## 2. Localization
*   **Kinematic Models:**
    *   Differential drive, Ackerman, omnidirectional robots
    *   State representation (pose: x, y, orientation)
    *   Motion commands and odometry
*   **Sensor Models:**
    *   Types of sensors: Encoders, IMUs (accelerometers, gyroscopes), cameras, LiDAR
    *   Sensor noise and uncertainty
    *   Measurement models
*   **Probabilistic Localization:**
    *   Belief representation
    *   **Kalman Filters (KF/EKF):**
        *   Assumptions and limitations
        *   Prediction and update steps
        *   Extended Kalman Filter (EKF) for non-linear systems
    *   **Particle Filters (Monte Carlo Localization - MCL):**
        *   Sampling and resampling
        *   Weighting based on sensor observations
        *   Advantages and disadvantages

## 3. Mapping
*   **Occupancy Grid Maps:**
    *   Representing environment as a grid of occupancy probabilities
    *   Updating cell probabilities with sensor data
    *   Resolution and computational cost
*   **Feature-Based Maps:**
    *   Identifying and tracking distinct landmarks (features)
    *   Representing features (e.g., points, lines)
    *   Feature descriptors
*   **Topological Maps:**
    *   Representing environment as a graph of nodes (places) and edges (paths)
    *   Abstract representation, useful for high-level navigation

## 4. The Joint State Problem
*   The "chicken-and-egg" dilemma: Can't localize without a map, can't map without localization
*   The need for simultaneous estimation

## 5. SLAM Algorithms
*   **Extended Kalman Filter (EKF-SLAM):**
    *   Simultaneous estimation of robot pose and landmark positions
    *   Linearization and Jacobian matrices
    *   Computational complexity (O(N^2) for N landmarks)
    *   Limitations: data association challenges, consistency issues
*   **Particle Filter (FastSLAM):**
    *   Factored approach: particles represent possible robot trajectories, each with its own map
    *   Rao-Blackwellized Particle Filter
    *   Improved scalability for mapping
*   **Graph-based SLAM (Optimization-based SLAM):**
    *   Representing robot poses and observations as a graph
    *   Nodes: robot poses and landmark positions
    *   Edges: odometry measurements and loop closures
    *   Optimization techniques: pose graph optimization, bundle adjustment
    *   Solving for the most consistent global map

## 6. Visual SLAM (V-SLAM)
*   **Feature-Based V-SLAM:**
    *   Detecting and matching visual features (e.g., SIFT, SURF, ORB)
    *   Estimating camera pose and feature locations
    *   Example: ORB-SLAM
*   **Direct V-SLAM:**
    *   Minimizing photometric error directly on image pixel intensities
    *   No explicit feature extraction
    *   Examples: LSD-SLAM, SVO

## 7. Lidar SLAM
*   **Scan Matching:**
    *   Aligning successive LiDAR scans to estimate robot motion
    *   Iterative Closest Point (ICP) algorithm
    *   Normal Distributions Transform (NDT)
*   **LOAM (LiDAR Odometry and Mapping):n*   **LOAM (LiDAR Odometry and Mapping):**
    *   Leveraging feature points from LiDAR scans
    *   Combining high-frequency odometry and low-frequency mapping
*   **LeGO-LOAM:**
    *   Lightweight and Ground-Optimized LOAM
    *   Segmentation of ground and non-ground points for efficiency

## 8. Data Association
*   The correspondence problem: Determining which sensor observation corresponds to which feature in the map
*   Nearest Neighbor, Joint Probabilistic Data Association (JPDA), Maximum Likelihood Data Association (MLDA)
*   Impact of incorrect data associations

## 9. Loop Closure
*   Recognizing previously visited locations
*   Correcting accumulated drift and improving map consistency
*   Techniques: Bag-of-Words, appearance-based matching (e.g., FAB-MAP)
*   Role in global consistency and drift reduction

## 10. Challenges in SLAM
*   **Computational Complexity:** Real-time requirements, large-scale environments
*   **Dynamic Environments:** Dealing with moving objects and changes in the environment
*   **Perceptual Aliasing:** Distinguishing similar-looking places
*   **Long-Term Autonomy:** Maintaining map consistency over extended periods
*   Sensor limitations (noise, limited range, occlusions)

## 11. Future Trends
*   **Semantic SLAM:** Integrating object recognition and understanding into SLAM
*   **Learning-based SLAM:** Using deep learning for feature extraction, visual odometry, and loop closure
*   **Multi-Robot SLAM:** Collaborative mapping and localization with multiple robots
*   Event-based cameras for high-speed, low-latency sensing
*   Robustness to adversarial attacks and sensor spoofing
