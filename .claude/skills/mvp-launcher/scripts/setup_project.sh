#!/bin/bash
# MVP Launcher — Project Setup Script
# Usage: bash setup_project.sh <project-name> [components...]
#
# Example:
#   bash setup_project.sh my-saas-app button card input dialog toast table
#
# This script:
# 1. Creates a Next.js app with TypeScript + Tailwind
# 2. Initializes shadcn/ui
# 3. Installs requested components
# 4. Installs lucide-react for icons
# 5. Sets up the project structure

set -e

PROJECT_NAME="${1:?Usage: setup_project.sh <project-name> [components...]}"
shift
COMPONENTS=("$@")

echo "🚀 MVP Launcher — Setting up $PROJECT_NAME"
echo "============================================"

# Step 1: Create Next.js app
echo ""
echo "📦 Step 1/4: Creating Next.js app..."
npx create-next-app@latest "$PROJECT_NAME" \
  --typescript \
  --tailwind \
  --eslint \
  --app \
  --src-dir \
  --import-alias "@/*" \
  --use-npm \
  --no-turbopack 2>&1

cd "$PROJECT_NAME"

# Step 2: Install additional dependencies
echo ""
echo "📦 Step 2/4: Installing dependencies..."
npm install lucide-react 2>&1

# Step 3: Initialize shadcn/ui
echo ""
echo "🎨 Step 3/4: Initializing shadcn/ui..."
npx shadcn@latest init -d 2>&1

# Step 4: Install components
if [ ${#COMPONENTS[@]} -gt 0 ]; then
  echo ""
  echo "🧩 Step 4/4: Installing shadcn/ui components..."
  for component in "${COMPONENTS[@]}"; do
    echo "  Installing: $component"
    npx shadcn@latest add "$component" -y 2>&1 || echo "  ⚠️ Could not install $component, skipping"
  done
else
  echo ""
  echo "🧩 Step 4/4: No components specified, installing defaults..."
  npx shadcn@latest add button card -y 2>&1
fi

# Create directory structure
echo ""
echo "📁 Creating project structure..."
mkdir -p src/components/layout
mkdir -p src/components/features
mkdir -p src/lib
mkdir -p public

echo ""
echo "✅ Project setup complete!"
echo ""
echo "📂 $PROJECT_NAME/"
echo "├── src/"
echo "│   ├── app/           (pages & routes)"
echo "│   ├── components/"
echo "│   │   ├── ui/        (shadcn components)"
echo "│   │   ├── layout/    (Navbar, Footer, etc.)"
echo "│   │   └── features/  (your components)"
echo "│   └── lib/           (utilities)"
echo "└── public/            (static assets)"
echo ""
echo "Next: cd $PROJECT_NAME && npm run dev"
