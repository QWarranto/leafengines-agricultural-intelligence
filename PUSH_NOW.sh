#!/bin/bash
echo "🚀 Quick GitHub Push Solution"
echo "=============================="

# First, let's commit if not already committed
if git status --porcelain | grep -q "^[MADRC]"; then
    echo "Committing changes..."
    git commit -m "Add complete agricultural intelligence Claude skill package"
fi

echo ""
echo "Option 1: Try SSH (if you have SSH key setup)"
echo "---------------------------------------------"
echo "git remote set-url origin git@github.com:QWarranto/leafengines-agricultural-intelligence.git"
echo "git push origin main"
echo ""

echo "Option 2: Use token in URL (one-time)"
echo "--------------------------------------"
echo "Replace YOUR_TOKEN with your Personal Access Token:"
echo "git push https://QWarranto:YOUR_TOKEN@github.com/QWarranto/leafengines-agricultural-intelligence.git main"
echo ""

echo "Option 3: GitHub Desktop"
echo "-----------------------"
echo "1. Download GitHub Desktop: https://desktop.github.com"
echo "2. Add this repository"
echo "3. Commit and push via GUI"
echo ""

echo "Option 4: Manual credential setup"
echo "---------------------------------"
echo "1. Generate token: https://github.com/settings/tokens"
echo "2. Store it: git config --global credential.helper store"
echo "3. Push: git push origin main"
echo "   Username: QWarranto"
echo "   Password: [paste token]"
echo ""

echo "📋 Current status:"
git status --short