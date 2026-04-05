#!/bin/bash
echo "🔑 Setting up SSH for GitHub"
echo "============================="

echo "1. Generating SSH key..."
ssh-keygen -t ed25519 -C "QWarranto@github.com" -f ~/.ssh/id_ed25519 -N ""

echo ""
echo "2. Starting SSH agent..."
eval "$(ssh-agent -s)"

echo "3. Adding SSH key to agent..."
ssh-add ~/.ssh/id_ed25519

echo ""
echo "4. 🔑 YOUR SSH PUBLIC KEY:"
echo "=========================================="
cat ~/.ssh/id_ed25519.pub
echo "=========================================="

echo ""
echo "5. Add this key to GitHub:"
echo "   a) Go to: https://github.com/settings/keys"
echo "   b) Click 'New SSH key'"
echo "   c) Title: 'iMac - LeafEngines'"
echo "   d) Key type: Authentication Key"
echo "   e) Paste the key above"
echo "   f) Click 'Add SSH key'"
echo ""
read -p "Press Enter AFTER adding key to GitHub..."

echo ""
echo "6. Testing SSH connection..."
ssh -T git@github.com

echo ""
echo "7. Switching remote to SSH..."
git remote set-url origin git@github.com:QWarranto/leafengines-agricultural-intelligence.git

echo ""
echo "8. Pushing changes..."
git push origin main

echo ""
echo "✅ Done! Check GitHub for your repository."