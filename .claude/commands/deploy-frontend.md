---
description: Deploy Docusaurus frontend to GitHub Pages or Render
---

# Deploy Frontend

This command deploys the Docusaurus frontend to GitHub Pages or Render.

## Prerequisites

- Node.js installed
- Frontend dependencies installed (`npm install` in frontend/)
- Git repository configured
- Deployment target set up (GitHub Pages or Render)

## Deployment Options

### Option 1: GitHub Pages (Recommended)

#### Step 1: Configure docusaurus.config.ts

```typescript
// frontend/docusaurus.config.ts
const config: Config = {
  // ...
  url: 'https://YOUR_USERNAME.github.io',
  baseUrl: '/YOUR_REPO_NAME/',
  organizationName: 'YOUR_USERNAME',
  projectName: 'YOUR_REPO_NAME',
  deploymentBranch: 'gh-pages',
  trailingSlash: false,
};
```

#### Step 2: Build the project

```bash
cd frontend
npm run build
```

#### Step 3: Deploy to GitHub Pages

```bash
# Using GIT_USER environment variable
GIT_USER=<Your GitHub username> npm run deploy
```

Or add to package.json:
```json
{
  "scripts": {
    "deploy": "docusaurus deploy"
  }
}
```

#### Step 4: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click on "Settings"
3. Scroll to "Pages" section
4. Source: Select "gh-pages" branch
5. Click "Save"

Your site should be live at: `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`

### Option 2: Render (Static Site)

#### Step 1: Build configuration

Create `render.yaml` in project root:

```yaml
services:
  - type: web
    name: physical-ai-textbook
    env: static
    buildCommand: cd frontend && npm install && npm run build
    staticPublishPath: ./frontend/build
    routes:
      - type: rewrite
        source: /*
        destination: /index.html
```

#### Step 2: Push to GitHub

```bash
git add .
git commit -m "Add Render configuration"
git push origin main
```

#### Step 3: Deploy on Render

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New +" → "Static Site"
3. Connect your GitHub repository
4. Render will auto-detect the configuration
5. Click "Create Static Site"

Your site will be live at: `https://YOUR_SITE_NAME.onrender.com`

## Verification

After deployment, verify:

1. **Homepage loads** - Check the main page renders correctly
2. **Navigation works** - Test sidebar and navbar links
3. **Assets load** - Images, CSS, and JS files are accessible
4. **Search works** - If search is enabled, test it
5. **Links are correct** - No 404 errors on internal links

## Troubleshooting

### Issue: CSS/JS not loading

**Solution:** Check `baseUrl` in `docusaurus.config.ts` matches your deployment path.

For GitHub Pages: `baseUrl: '/repo-name/'`
For custom domain: `baseUrl: '/'`

### Issue: 404 on page refresh

**Solution:** Configure server to serve `index.html` for all routes.

For GitHub Pages: Docusaurus handles this automatically.
For Render: Use the `routes` configuration shown above.

### Issue: Build fails

**Solution:** 
1. Clear node_modules and reinstall: `rm -rf node_modules && npm install`
2. Clear Docusaurus cache: `npm run clear`
3. Check Node.js version: Should be >= 16.14

## Manual Deployment (Alternative)

If you prefer manual deployment:

```bash
# 1. Build the site
cd frontend
npm run build

# 2. The build output is in frontend/build/
# 3. Upload the contents of frontend/build/ to your hosting provider
```

## Continuous Deployment

### GitHub Actions (Automated)

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: 18
          cache: npm
          cache-dependency-path: frontend/package-lock.json
      
      - name: Install dependencies
        run: cd frontend && npm ci
      
      - name: Build website
        run: cd frontend && npm run build
      
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./frontend/build
```

This will automatically deploy on every push to main branch.

## Post-Deployment Checklist

- [ ] Homepage loads correctly
- [ ] All navigation links work
- [ ] Search functionality works (if enabled)
- [ ] Images and assets load
- [ ] Dark mode toggle works
- [ ] Mobile view is responsive
- [ ] Share site URL with team for review

## Related Commands

- `/test-all` - Run tests before deployment
- `/setup-env` - Configure environment variables
