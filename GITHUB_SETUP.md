# GitHub Setup Instructions

## Step 1: Initialize Git Repository (Local)

Open terminal in the project folder and run:

```bash
git init
git add .
git commit -m "Initial commit: Delivery route optimization project"
```

## Step 2: Create GitHub Repository

1. Go to https://github.com
2. Click the **+** icon (top right) → **New repository**
3. Fill in:
   - **Repository name:** `delivery-route-optimization`
   - **Description:** `Algorithm Design project implementing Merge Sort and Binary Search for delivery optimization`
   - **Visibility:** Public (so your lecturer can access it)
   - **DO NOT** initialize with README (we already have one)
4. Click **Create repository**

## Step 3: Connect to GitHub

GitHub will show you commands. Use these:

```bash
git remote add origin https://github.com/YOUR-USERNAME/delivery-route-optimization.git
git branch -M main
git push -u origin main
```

Replace `YOUR-USERNAME` with your actual GitHub username.

## Step 4: Verify Upload

1. Refresh your GitHub repository page
2. You should see all your files
3. The README.md will display automatically

## Step 5: Get the Link

Copy the repository URL from the browser address bar.
It will look like:
```
https://github.com/YOUR-USERNAME/delivery-route-optimization
```

## Step 6: Submit to Portal

Paste the GitHub link in your course portal as instructed.

---

## Troubleshooting

**If git command not found:**
- Download Git from: https://git-scm.com/downloads
- Install and restart terminal

**If authentication fails:**
- Use GitHub Personal Access Token instead of password
- Go to GitHub Settings → Developer settings → Personal access tokens
- Generate new token with 'repo' permissions

**Need help?**
Check GitHub's official guide: https://docs.github.com/en/get-started

---

## What Your Lecturer Will See

When they visit your link, they'll see:
- Professional README with project overview
- Clean, well-commented code
- Performance analysis documentation
- Screenshots of results
- All required algorithms implemented

Good luck with your submission!
