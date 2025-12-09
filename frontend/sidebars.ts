import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Course Modules',
      collapsed: false,
      items: [
        {
          type: 'category',
          label: 'Module 1: ROS2 Nervous System',
          items: ['module1-ros2-nervous-system/index', 'module1-ros2-nervous-system/outline'],
        },
        {
          type: 'category',
          label: 'Module 2: Robot Sensing & Perception',
          items: ['module2-robot-sensing-and-perception/index', 'module2-robot-sensing-and-perception/outline'],
        },
        {
          type: 'category',
          label: 'Module 3: Kinematics & Dynamics',
          items: ['module3-robot-kinematics-and-dynamics/index', 'module3-robot-kinematics-and-dynamics/outline'],
        },
        {
          type: 'category',
          label: 'Module 4: Motion Planning & Control',
          items: ['module4-robot-motion-planning-and-control/index', 'module4-robot-motion-planning-and-control/outline'],
        },
        {
          type: 'category',
          label: 'Module 5: Robot Learning & Adaptation',
          items: ['module5-robot-learning-and-adaptation/index', 'module5-robot-learning-and-adaptation/outline'],
        },
        {
          type: 'category',
          label: 'Module 6: Humanoid Design & Locomotion',
          items: ['module6-humanoid-robot-design-and-locomotion/index', 'module6-humanoid-robot-design-and-locomotion/outline'],
        },
        {
          type: 'category',
          label: 'Module 7: Manipulation & Interaction',
          items: ['module7-humanoid-robot-manipulation-and-interaction/index', 'module7-humanoid-robot-manipulation-and-interaction/outline'],
        },
        {
          type: 'category',
          label: 'Module 8: Reinforcement Learning',
          items: ['module8-reinforcement-learning-for-robotics/index', 'module8-reinforcement-learning-for-robotics/outline'],
        },
        {
          type: 'category',
          label: 'Module 9: SLAM',
          items: ['module9-simultaneous-localization-and-mapping-slam/index', 'module9-simultaneous-localization-and-mapping-slam/outline'],
        },
        {
          type: 'category',
          label: 'Module 10: Human-Robot Interaction',
          items: ['module10-robot-human-interaction/index', 'module10-robot-human-interaction/outline'],
        },
        {
          type: 'category',
          label: 'Module 11: Ethics & Safety',
          items: ['module11-robot-ethics-and-safety/index', 'module11-robot-ethics-and-safety/outline'],
        },
        {
          type: 'category',
          label: 'Module 12: Advanced Topics',
          items: ['module12-advanced-topics-in-physical-ai/index', 'module12-advanced-topics-in-physical-ai/outline'],
        },
        {
          type: 'category',
          label: 'Module 13: Future of Robotics',
          items: ['module13-future-of-humanoid-robotics-and-ai/index', 'module13-future-of-humanoid-robotics-and-ai/outline'],
        },
      ],
    },
    {
      type: 'category',
      label: 'Assessments',
      items: [
        'assessments/module1-assessments',
        'assessments/module2-assessments',
        'assessments/module3-assessments',
        'assessments/module4-assessments',
        'assessments/module5-assessments',
        'assessments/module6-assessments',
        'assessments/module8-assessments',
        'assessments/module9-assessments',
        'assessments/module10-assessments',
        'assessments/module11-assessments',
        'assessments/module12-assessments',
        'assessments/module13-assessments',
      ],
    },
    'glossary',
  ],
};

export default sidebars;
