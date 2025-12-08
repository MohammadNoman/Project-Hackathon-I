# Module 1: The Robotic Nervous System (ROS 2) - Assessments

## Quizzes / Short Answer Questions

### Section 1: Introduction to ROS 2

1.  **Question:** Explain the primary purpose of ROS 2 in the context of robotics development. How does it simplify the creation of complex robot behaviors?
    *   **Learning Outcome Alignment:** Understanding the foundational role and benefits of ROS 2.
    *   **Expected Answer Elements:** Hardware abstraction, inter-process communication, tooling, ecosystem, managing complexity in modular/distributed architectures.

2.  **Question:** Why is ROS 2 particularly indispensable for physical AI and humanoid robotics? Provide at least two reasons, referencing the unique challenges of such systems.
    *   **Learning Outcome Alignment:** Connecting ROS 2's features to specific needs of humanoid robotics.
    *   **Expected Answer Elements:** Managing complexity (numerous sensors/actuators), modularity, distributed architecture for real-time processing, motion planning, HRI, AI integration.

### Section 2: Key Concepts

1.  **Question:** Differentiate between ROS 2 Topics and Services. When would you choose to use one over the other in a robotic application? Provide a clear example for each.
    *   **Learning Outcome Alignment:** Distinguishing between core communication mechanisms.
    *   **Expected Answer Elements:**
        *   Topics: Publish-subscribe, asynchronous, continuous data (e.g., sensor readings, joint states).
        *   Services: Request-reply, synchronous, immediate results (e.g., querying a sensor once, triggering a specific action).

2.  **Question:** Describe the role of a ROS 2 Node and a Message within the ROS 2 ecosystem. How do these two concepts work together to achieve robot functionality?
    *   **Learning Outcome Alignment:** Understanding the fundamental building blocks.
    *   **Expected Answer Elements:**
        *   Node: Executable process, performs specific task.
        *   Message: Structured data for communication.
        *   Together: Nodes communicate via topics/services using structured messages.

3.  **Question:** Explain what ROS 2 Actions are designed for and how they differ from Services. Give an example of a robotic task that would be best implemented using an Action.
    *   **Learning Outcome Alignment:** Comprehending long-running, goal-oriented communication.
    *   **Expected Answer Elements:** Long-running, goal-oriented, feedback, result vs. immediate request-reply. Example: navigating to a location, complex manipulation.

4.  **Question:** How do ROS 2 Parameters and Launch files contribute to the flexibility and deployment of a robotic system?
    *   **Learning Outcome Alignment:** Understanding configuration and system orchestration.
    *   **Expected Answer Elements:**
        *   Parameters: Dynamic configuration without recompilation.
        *   Launch files: Starting/managing multiple nodes, defining system architecture, simplifying deployment.

### Section 3: Core Components

1.  **Question:** Compare `rclpy` and `rclcpp` client libraries. In what scenarios would a developer choose one over the other?
    *   **Learning Outcome Alignment:** Understanding the primary programming interfaces.
    *   **Expected Answer Elements:**
        *   `rclpy`: Python, rapid prototyping, less computationally intensive.
        *   `rclcpp`: C++, high performance, low latency, real-time/critical control.

2.  **Question:** What is the purpose of the `ament` build system in ROS 2? How does it support diverse programming languages and build tools?
    *   **Learning Outcome Alignment:** Understanding the build process.
    *   **Expected Answer Elements:** Manages compilation/linking/installation, supports C++/Python, CMake/setuptools, independent package building.

### Section 4: Hands-on Example (Conceptual)

1.  **Question:** Based on the "Simple Robot Control" conceptual example, outline the sequence of events (nodes, topics, messages) that would occur to make a virtual robot move forward and then turn using `geometry_msgs/Twist`.
    *   **Learning Outcome Alignment:** Applying core concepts to a practical scenario.
    *   **Expected Answer Elements:** Command Publisher node publishes Twist messages to `/cmd_vel` topic, Robot Driver node subscribes to `/cmd_vel` and interprets commands, specific `linear.x` and `angular.z` values for moving forward and turning.

## Project Prompts

### Project 1: Basic ROS 2 Talker-Listener Implementation

**Objective:** Implement a basic talker-listener system in ROS 2 that demonstrates communication between two nodes using a custom message type.

**Requirements:**
1.  **Define a Custom Message:** Create a `.msg` file for a custom message (e.g., `MyString.msg` containing a single `string data` field or `MyInt.msg` with `int32 value`).
2.  **Implement a Talker Node:**
    *   Create a Python or C++ ROS 2 node that publishes instances of your custom message type to a topic (e.g., `/my_topic`).
    *   The talker should publish a new message every 1-2 seconds, with unique content (e.g., an incrementing counter or a changing string).
3.  **Implement a Listener Node:**
    *   Create a Python or C++ ROS 2 node that subscribes to the same topic (`/my_topic`).
    *   The listener should print the received message content to the console.
4.  **Create a Launch File:** Develop a Python launch file that starts both the talker and listener nodes simultaneously.
5.  **Testing:** Demonstrate that the listener node correctly receives and prints messages from the talker node when launched.

**Learning Outcomes Assessed:**
*   Defining and using custom ROS 2 messages.
*   Implementing publisher and subscriber nodes.
*   Understanding and using ROS 2 topics for inter-node communication.
*   Creating and utilizing ROS 2 launch files for system orchestration.

### Project 2: ROS 2 Service for Robot State Query

**Objective:** Develop a ROS 2 service that allows a client to query a simulated robot's "status" (e.g., battery level, current mode).

**Requirements:**
1.  **Define a Custom Service:** Create a `.srv` file for a custom service (e.g., `GetRobotStatus.srv` with a request field like `string query` and a response field like `string status_info` and `float32 battery_level`).
2.  **Implement a Service Server Node:**
    *   Create a Python or C++ ROS 2 node that implements the service server.
    *   The server should respond to client requests with simulated robot status information (e.g., randomly generated battery level, a fixed mode string).
3.  **Implement a Service Client Node:**
    *   Create a Python or C++ ROS 2 node that acts as a service client.
    *   The client should send a request to the server and print the received response.
    *   The client should ideally be callable from the command line with an argument for the query (e.g., `ros2 run my_pkg my_client "battery"`).
4.  **Create a Launch File:** Develop a Python launch file to start the service server node.
5.  **Testing:** Verify that the client can successfully call the service and receive the expected information.

**Learning Outcomes Assessed:**
*   Defining and using custom ROS 2 services.
*   Implementing service server and client nodes.
*   Understanding and using synchronous communication in ROS 2.
*   Integrating service calls into a robotic application context.

### Project 3: ROS 2 Action for Simple Navigation Goal

**Objective:** Implement a ROS 2 action that simulates a robot moving to a target location, providing feedback during the "navigation" process.

**Requirements:**
1.  **Define a Custom Action:** Create a `.action` file for a simple navigation action (e.g., `NavigateToPose.action` with a goal for `float32 x, y`, feedback for `float32 distance_remaining`, and a result for `bool success`).
2.  **Implement an Action Server Node:**
    *   Create a Python or C++ ROS 2 node that implements the action server.
    *   When a goal is received, simulate navigation by continuously publishing feedback (e.g., decreasing `distance_remaining`) over a few seconds.
    *   Upon "reaching" the goal, publish a result indicating success.
    *   Handle preemption/cancellation if applicable (bonus).
3.  **Implement an Action Client Node:**
    *   Create a Python or C++ ROS 2 node that acts as an action client.
    *   The client should send a navigation goal to the server.
    *   It should process and print the feedback received from the server.
    *   Finally, it should print the result once the action is complete.
4.  **Create a Launch File:** Develop a Python launch file to start the action server node.
5.  **Testing:** Demonstrate the client sending a goal, receiving continuous feedback, and obtaining a final result.

**Learning Outcomes Assessed:**
*   Defining and using custom ROS 2 actions.
*   Implementing action server and client nodes.
*   Understanding long-running, goal-oriented communication with feedback.
*   Simulating a complex robotic task using the action framework.
