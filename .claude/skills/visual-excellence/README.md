# 🎨 Visual Excellence Kit (Reusable Intelligence)

This folder contains the **Visual Excellence Design System** extracted from the AI-Native Book Reader. It is designed to be a "plug-and-play" skill for any AI Agent or Developer to instantly upgrade the aesthetics of a project.

## 📦 Contents

1.  **`styles/tailwind.preset.js`**: The core configuration (Colors, Typography, Animations).
2.  **`styles/global.css`**: Essential global styles and utility classes.
3.  **`components/`**: Reusable "Premium" React components.

## 🚀 How to Apply (The "Skill" for Agents)

### 1. Install Dependencies
Ensure the target project has Tailwind CSS and Lucide React installed:
```bash
npm install -D tailwindcss postcss autoprefixer
npm install lucide-react clsx tailwind-merge
npx tailwindcss init -p
```

### 2. Configure Tailwind
Modify your `tailwind.config.js` to use the preset:

```javascript
// tailwind.config.js
import visualExcellence from './reusable-intelligence/visual-excellence-kit/styles/tailwind.preset.js';

export default {
  presets: [visualExcellence],
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
    // Add path to kit components if they stay in this folder
    "./reusable-intelligence/**/*.{js,ts,jsx,tsx}" 
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

### 3. Import Global Styles
Import the global CSS in your main entry file (e.g., `main.tsx` or `App.tsx`) or your main CSS file:

```css
/* In your index.css */
@import './reusable-intelligence/visual-excellence-kit/styles/global.css';
```

### 4. Use the Components
Copy the components from `components/` to your project's `src/components/` directory OR import them directly if you keep this folder structure.

---

## 🧠 Agent Instructions (Prompt)

If you are an AI Agent, use this kit as follows:
> "I have access to the 'Visual Excellence Kit'. I will use the 'Brand' color palette (Cyan/Blue) for primary actions and 'Slate' (900/950) for backgrounds to ensure a premium dark-mode aesthetic. I will utilize the `GradientTitle` for headers and `InteractiveCard` for list items to maintain visual consistency."
