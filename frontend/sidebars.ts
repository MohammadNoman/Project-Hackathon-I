import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  // By default, Docusaurus generates a sidebar from the docs folder structure
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Course Modules',
      items: [
        'module1-ros2-nervous-system/index',
        'module2-robot-sensing-and-perception/index',
        'module3-robot-kinematics-and-dynamics/index',
        'module4-robot-motion-planning-and-control/index',
        'module5-robot-learning-and-adaptation/index',
        'module6-humanoid-robot-design-and-locomotion/index',
        'module7-humanoid-robot-manipulation-and-interaction/index',
        'module8-reinforcement-learning-for-robotics/index',
        'module9-simultaneous-localization-and-mapping-slam/index',
        'module10-robot-human-interaction/index',
        'module11-robot-ethics-and-safety/index',
        'module12-advanced-topics-in-physical-ai/index',
        'module13-future-of-humanoid-robotics-and-ai/index',
      ],
    },
  ],

  // But you can create a sidebar manually
  /*
  tutorialSidebar: [
    'intro',
    'hello',
    {
      type: 'category',
      label: 'Tutorial',
      items: ['tutorial-basics/create-a-document'],
    },
  ],
   */
};

export default sidebars;
