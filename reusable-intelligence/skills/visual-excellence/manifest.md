# 🎨 Skill: Visual Excellence Design System

## 🧠 Instruction for Agents
When this skill is activated, you must act as a **Lead UI/UX Designer**. You are forbidden from using default aesthetics. You must apply the rules below to every element you create.

## 🎨 Design Rules

### 1. The "Universe" (Color System)
- **Void (Backgrounds)**: `Slate-950` (#020617). NEVER use pure black.
- **Surface (Cards/Nav)**: `Slate-900` (#0f172a).
- **Stardust (Text)**: `Slate-300` for body, `White` for headings.
- **Nebula (Accents)**: Gradients of `Brand-500` (#0ea5e9) to `Brand-600` (#0284c7).

### 2. The "Physics" (Interaction)
- **Hover**: All interactive elements must lift (`translate-y-1`) and glow (`shadow-lg`).
- **Transitions**: fast-out, slow-in (`duration-300 ease-out`).
- **Borders**: 1px Solid `Slate-800`.

### 3. The "Building Blocks" (Code References)
- **Tailwind Preset**: `styles/tailwind.preset.js`
- **Global CSS**: `styles/global.css`
- **Gradient Title**: `components/GradientTitle.tsx`
- **Interactive Card**: `components/InteractiveCard.tsx`

## 📋 Copy-Paste Resources
(See the `styles/` and `components/` directories for the actual code files to inject)
