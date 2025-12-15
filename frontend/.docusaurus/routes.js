import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/Project-Hackathon-I/markdown-page',
    component: ComponentCreator('/Project-Hackathon-I/markdown-page', '920'),
    exact: true
  },
  {
    path: '/Project-Hackathon-I/docs',
    component: ComponentCreator('/Project-Hackathon-I/docs', 'ce5'),
    routes: [
      {
        path: '/Project-Hackathon-I/docs',
        component: ComponentCreator('/Project-Hackathon-I/docs', '07e'),
        routes: [
          {
            path: '/Project-Hackathon-I/docs',
            component: ComponentCreator('/Project-Hackathon-I/docs', '775'),
            routes: [
              {
                path: '/Project-Hackathon-I/docs/assessments/module1-assessments',
                component: ComponentCreator('/Project-Hackathon-I/docs/assessments/module1-assessments', '2b2'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/assessments/module10-assessments',
                component: ComponentCreator('/Project-Hackathon-I/docs/assessments/module10-assessments', '39d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/assessments/module11-assessments',
                component: ComponentCreator('/Project-Hackathon-I/docs/assessments/module11-assessments', '1de'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/assessments/module12-assessments',
                component: ComponentCreator('/Project-Hackathon-I/docs/assessments/module12-assessments', '7cd'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/assessments/module13-assessments',
                component: ComponentCreator('/Project-Hackathon-I/docs/assessments/module13-assessments', '4f1'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/assessments/module2-assessments',
                component: ComponentCreator('/Project-Hackathon-I/docs/assessments/module2-assessments', 'c4a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/assessments/module3-assessments',
                component: ComponentCreator('/Project-Hackathon-I/docs/assessments/module3-assessments', '69c'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/assessments/module4-assessments',
                component: ComponentCreator('/Project-Hackathon-I/docs/assessments/module4-assessments', 'a77'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/assessments/module5-assessments',
                component: ComponentCreator('/Project-Hackathon-I/docs/assessments/module5-assessments', '902'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/assessments/module6-assessments',
                component: ComponentCreator('/Project-Hackathon-I/docs/assessments/module6-assessments', 'e61'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/assessments/module8-assessments',
                component: ComponentCreator('/Project-Hackathon-I/docs/assessments/module8-assessments', '88a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/assessments/module9-assessments',
                component: ComponentCreator('/Project-Hackathon-I/docs/assessments/module9-assessments', '4ab'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/glossary',
                component: ComponentCreator('/Project-Hackathon-I/docs/glossary', 'c46'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/intro',
                component: ComponentCreator('/Project-Hackathon-I/docs/intro', '551'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module1-ros2-nervous-system/',
                component: ComponentCreator('/Project-Hackathon-I/docs/module1-ros2-nervous-system/', 'b8e'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module1-ros2-nervous-system/outline',
                component: ComponentCreator('/Project-Hackathon-I/docs/module1-ros2-nervous-system/outline', '87a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module10-robot-human-interaction/',
                component: ComponentCreator('/Project-Hackathon-I/docs/module10-robot-human-interaction/', '04f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module10-robot-human-interaction/outline',
                component: ComponentCreator('/Project-Hackathon-I/docs/module10-robot-human-interaction/outline', '40a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module11-robot-ethics-and-safety/',
                component: ComponentCreator('/Project-Hackathon-I/docs/module11-robot-ethics-and-safety/', '80f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module11-robot-ethics-and-safety/outline',
                component: ComponentCreator('/Project-Hackathon-I/docs/module11-robot-ethics-and-safety/outline', 'f6e'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module12-advanced-topics-in-physical-ai/',
                component: ComponentCreator('/Project-Hackathon-I/docs/module12-advanced-topics-in-physical-ai/', '1ac'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module12-advanced-topics-in-physical-ai/outline',
                component: ComponentCreator('/Project-Hackathon-I/docs/module12-advanced-topics-in-physical-ai/outline', '958'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module13-future-of-humanoid-robotics-and-ai/',
                component: ComponentCreator('/Project-Hackathon-I/docs/module13-future-of-humanoid-robotics-and-ai/', '052'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module13-future-of-humanoid-robotics-and-ai/outline',
                component: ComponentCreator('/Project-Hackathon-I/docs/module13-future-of-humanoid-robotics-and-ai/outline', '140'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module2-robot-sensing-and-perception/',
                component: ComponentCreator('/Project-Hackathon-I/docs/module2-robot-sensing-and-perception/', '714'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module2-robot-sensing-and-perception/outline',
                component: ComponentCreator('/Project-Hackathon-I/docs/module2-robot-sensing-and-perception/outline', 'd12'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module3-robot-kinematics-and-dynamics/',
                component: ComponentCreator('/Project-Hackathon-I/docs/module3-robot-kinematics-and-dynamics/', '763'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module3-robot-kinematics-and-dynamics/outline',
                component: ComponentCreator('/Project-Hackathon-I/docs/module3-robot-kinematics-and-dynamics/outline', 'e8f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module4-robot-motion-planning-and-control/',
                component: ComponentCreator('/Project-Hackathon-I/docs/module4-robot-motion-planning-and-control/', '5f4'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module4-robot-motion-planning-and-control/outline',
                component: ComponentCreator('/Project-Hackathon-I/docs/module4-robot-motion-planning-and-control/outline', '211'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module5-robot-learning-and-adaptation/',
                component: ComponentCreator('/Project-Hackathon-I/docs/module5-robot-learning-and-adaptation/', '4d6'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module5-robot-learning-and-adaptation/outline',
                component: ComponentCreator('/Project-Hackathon-I/docs/module5-robot-learning-and-adaptation/outline', 'ccf'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module6-humanoid-robot-design-and-locomotion/',
                component: ComponentCreator('/Project-Hackathon-I/docs/module6-humanoid-robot-design-and-locomotion/', 'fbe'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module6-humanoid-robot-design-and-locomotion/outline',
                component: ComponentCreator('/Project-Hackathon-I/docs/module6-humanoid-robot-design-and-locomotion/outline', '3d2'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module7-humanoid-robot-manipulation-and-interaction/',
                component: ComponentCreator('/Project-Hackathon-I/docs/module7-humanoid-robot-manipulation-and-interaction/', '1ae'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module7-humanoid-robot-manipulation-and-interaction/outline',
                component: ComponentCreator('/Project-Hackathon-I/docs/module7-humanoid-robot-manipulation-and-interaction/outline', '4c5'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module8-reinforcement-learning-for-robotics/',
                component: ComponentCreator('/Project-Hackathon-I/docs/module8-reinforcement-learning-for-robotics/', 'd1a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module8-reinforcement-learning-for-robotics/outline',
                component: ComponentCreator('/Project-Hackathon-I/docs/module8-reinforcement-learning-for-robotics/outline', 'd4a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module9-simultaneous-localization-and-mapping-slam/',
                component: ComponentCreator('/Project-Hackathon-I/docs/module9-simultaneous-localization-and-mapping-slam/', '288'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/module9-simultaneous-localization-and-mapping-slam/outline',
                component: ComponentCreator('/Project-Hackathon-I/docs/module9-simultaneous-localization-and-mapping-slam/outline', 'd57'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Project-Hackathon-I/docs/tutorial-basics/congratulations',
                component: ComponentCreator('/Project-Hackathon-I/docs/tutorial-basics/congratulations', 'f83'),
                exact: true
              },
              {
                path: '/Project-Hackathon-I/docs/tutorial-basics/create-a-blog-post',
                component: ComponentCreator('/Project-Hackathon-I/docs/tutorial-basics/create-a-blog-post', 'fe5'),
                exact: true
              },
              {
                path: '/Project-Hackathon-I/docs/tutorial-basics/create-a-document',
                component: ComponentCreator('/Project-Hackathon-I/docs/tutorial-basics/create-a-document', '3b0'),
                exact: true
              },
              {
                path: '/Project-Hackathon-I/docs/tutorial-basics/create-a-page',
                component: ComponentCreator('/Project-Hackathon-I/docs/tutorial-basics/create-a-page', '91d'),
                exact: true
              },
              {
                path: '/Project-Hackathon-I/docs/tutorial-basics/deploy-your-site',
                component: ComponentCreator('/Project-Hackathon-I/docs/tutorial-basics/deploy-your-site', 'bed'),
                exact: true
              },
              {
                path: '/Project-Hackathon-I/docs/tutorial-basics/markdown-features',
                component: ComponentCreator('/Project-Hackathon-I/docs/tutorial-basics/markdown-features', 'd29'),
                exact: true
              },
              {
                path: '/Project-Hackathon-I/docs/tutorial-extras/manage-docs-versions',
                component: ComponentCreator('/Project-Hackathon-I/docs/tutorial-extras/manage-docs-versions', '6e3'),
                exact: true
              },
              {
                path: '/Project-Hackathon-I/docs/tutorial-extras/translate-your-site',
                component: ComponentCreator('/Project-Hackathon-I/docs/tutorial-extras/translate-your-site', 'ba2'),
                exact: true
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/Project-Hackathon-I/',
    component: ComponentCreator('/Project-Hackathon-I/', '6e3'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
