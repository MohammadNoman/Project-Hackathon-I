# Module 8: Reinforcement Learning for Robotics - Assessments

## Quizzes/Formative Assessments

### Quiz 8.1: Introduction to RL in Robotics
1.  **Multiple Choice:** Which of the following is NOT a primary reason why Reinforcement Learning (RL) is suitable for robotics?
    a) Handling complex control problems with non-linear dynamics.
    b) Learning directly from explicit programming instructions.
    c) Adaptability to new and changing environments.
    d) Continuous improvement through interaction with the environment.

2.  **Short Answer:** Briefly explain two significant challenges when applying RL to real-world robotics.

### Quiz 8.2: Foundations of Reinforcement Learning
1.  **Fill in the Blanks:** In a Markov Decision Process (MDP), the agent is in a **[State]**, takes an **[Action]**, receives a **[Reward]**, and transitions to a new state based on **[Transition Probability]**.

2.  **True/False:** A deterministic policy outputs a probability distribution over actions for each state.

3.  **Concept Matching:** Match the following terms with their descriptions:
    a) Q-function
    b) V-function
    c) Advantage Function

    i) Estimates the expected return starting from a state, taking an action, and then following a policy.
    ii) Measures how much better it is to take a specific action compared to the average action.
    iii) Estimates the expected return starting from a state and following a policy thereafter.

### Quiz 8.3: Model-Free RL for Control
1.  **Compare/Contrast:** Differentiate between Q-learning and SARSA in terms of their on-policy/off-policy nature.

2.  **Short Answer:** Explain the purpose of "Experience Replay" and "Target Networks" in Deep Q-Networks (DQN).

3.  **Multiple Choice:** Which of the following policy gradient methods is known for its stability and uses a clipped surrogate objective function to limit policy updates?
    a) REINFORCE
    b) A3C
    c) PPO
    d) DDPG

### Quiz 8.4: Model-Based RL for Robotics
1.  **Short Answer:** Describe the difference between a "forward model" and an "inverse model" in the context of learning dynamics models for robotics.

2.  **Explanation:** How does Model Predictive Control (MPC) utilize a learned dynamics model to control a robot?

### Quiz 8.5: Sim-to-Real Transfer & Reward Function Design
1.  **Definition:** What is the "simulation gap" in RL for robotics, and what are two common causes?

2.  **True/False:** Domain randomization aims to perfectly match the simulation environment to the real world.

3.  **Short Answer:** Explain the core idea behind Inverse Reinforcement Learning (IRL) and why it's useful for reward design.

## Project Prompts/Summative Assessments

### Project 8.1: Implementing and Analyzing a Basic RL Algorithm for a Robotic Task
**Objective:** Implement a foundational model-free RL algorithm (e.g., Q-learning or a basic Policy Gradient method) for a simplified robotic control task in a simulated environment.

**Task:**
1.  **Choose a Task:** Select a simple robotic task (e.g., a pendulum swing-up, a mobile robot navigation in a grid world, or a simple arm reaching task) that can be simulated.
2.  **Environment Setup:** Define the state space, action space, and reward function for your chosen task. Consider if sparse or dense rewards are more appropriate and justify your choice.
3.  **Algorithm Implementation:** Implement either Q-learning (for discrete spaces) or a basic Policy Gradient method (e.g., REINFORCE) using a suitable function approximator (e.g., a small neural network if using policy gradients).
4.  **Training and Evaluation:** Train your agent in the simulated environment. Plot the learning curve (e.g., reward per episode) and evaluate the learned policy's performance.
5.  **Analysis and Discussion:**
    *   Discuss the challenges encountered during implementation and training.
    *   Analyze the impact of hyperparameter choices (e.g., learning rate, discount factor, exploration strategy) on convergence and final policy performance.
    *   Propose potential improvements to your chosen algorithm or reward function for this task.

### Project 8.2: Exploring Sim-to-Real Transfer Techniques
**Objective:** Investigate and demonstrate the impact of domain randomization on sim-to-real transfer for a robot learning task.

**Task:**
1.  **Choose a Task & Simulation:** Select a simple manipulation or locomotion task. Create a basic simulation of this task (e.g., using PyBullet, MuJoCo, or a simpler custom environment). Introduce a "reality gap" by having slightly different physical parameters for your "real-world" target vs. initial simulation parameters (e.g., different friction, mass, sensor noise).
2.  **Baseline Training:** Train an RL policy (e.g., DDPG or PPO) in your *initial*, non-randomized simulation. Evaluate its performance on both the initial simulation and the "real-world" target simulation.
3.  **Domain Randomization Implementation:** Implement domain randomization. Randomize several key physical or visual parameters (e.g., object mass, friction coefficients, joint damping, lighting, textures) within a defined range during training.
4.  **Randomized Training & Evaluation:** Train a new RL policy with domain randomization. Evaluate its performance on both the randomized simulation range and the "real-world" target simulation.
5.  **Comparative Analysis:**
    *   Compare the performance and robustness of the baseline policy versus the domain-randomized policy on the "real-world" target simulation.
    *   Discuss how different randomization ranges or types of parameters affect the transferability.
    *   Suggest other sim-to-real techniques (e.g., adversarial training, policy adaptation) that could further improve the transfer and explain why.

### Project 8.3: Reward Engineering or Inverse Reinforcement Learning
**Objective:** Design and evaluate different reward functions for a robotic task, or implement a basic Inverse Reinforcement Learning (IRL) approach.

**Option A: Reward Engineering**
1.  **Choose a Task:** Select a robotic task (e.g., reaching, grasping, balancing) where reward design is non-trivial.
2.  **Design Multiple Rewards:** Create at least two different reward functions for the same task: one sparse and one dense (or a shaped reward). Justify your design choices.
3.  **Train and Compare:** Train the same RL algorithm (e.g., DQN, PPO) with each of your designed reward functions. Compare the learning speed, final policy performance, and any observed "reward hacking" behaviors.
4.  **Analysis:** Discuss the trade-offs between sparse and dense/shaped rewards, and the challenges of aligning the reward with the true objective.

**Option B: Basic Inverse Reinforcement Learning (IRL)**
1.  **Choose a Simple Task:** Select a very simple grid-world or continuous robotic task where expert demonstrations can be easily generated.
2.  **Generate Expert Demonstrations:** Record a few optimal (or near-optimal) trajectories for the task.
3.  **Implement Basic IRL:** Implement a simple IRL algorithm (e.g., a basic feature matching or maximum entropy IRL variant, even a simplified version focusing on matching state visitation frequencies). You might need to approximate the reward function with a linear combination of features.
4.  **Infer Reward and Evaluate:** Use your IRL implementation to infer a reward function from the expert demonstrations. Then, train an RL agent with the *inferred* reward function and evaluate its performance against the expert demonstrations or a known optimal policy.
5.  **Discussion:** Discuss the challenges of IRL, such as the ambiguity of the reward function and the need for good feature representations.