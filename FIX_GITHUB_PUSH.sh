#!/bin/bash
echo "🔧 Fixing GitHub Push Authentication"
echo "===================================="

# Check current remote
echo "1. Current remote URL:"
git remote -v

echo ""
echo "2. Options:"
echo "   A) Switch to SSH (recommended)"
echo "   B) Use GitHub CLI (opens browser)"
echo "   C) Manual push with token"
echo "   D) Clear credentials and retry"
echo ""
read -p "Choose option (A/B/C/D): " choice

case $choice in
    A|a)
        echo "🔄 Switching to SSH..."
        # Check for SSH key
        if [ ! -f ~/.ssh/id_ed25519 ] && [ ! -f ~/.ssh/id_rsa ]; then
            echo "No SSH key found. Generating new one..."
            ssh-keygen -t ed25519 -C "QWarranto@github.com" -f ~/.ssh/id_ed25519 -N ""
            echo "🔑 New SSH key generated: ~/.ssh/id_ed25519.pub"
            echo "Add this to GitHub: https://github.com/settings/keys"
            cat ~/.ssh/id_ed25519.pub
            echo ""
            read -p "Press Enter after adding key to GitHub..."
        fi
        
        # Change remote to SSH
        git remote set-url origin git@github.com:QWarranto/leafengines-agricultural-intelligence.git
        echo "✅ Remote changed to SSH"
        echo "Now run: git push origin main"
        ;;
        
    B|b)
        echo "🌐 Using GitHub CLI..."
        if ! command -v gh &> /dev/null; then
            echo "Installing GitHub CLI..."
            brew install gh
        fi
        gh auth login
        echo "✅ GitHub CLI authenticated"
        echo "Now run: git push origin main"
        ;;
        
    C|c)
        echo "🔑 Manual push with token..."
        read -p "Enter your GitHub Personal Access Token: " token
        if [ -n "$token" ]; then
            echo "Pushing with token..."
            git push https://QWarranto:$token@github.com/QWarranto/leafengines-agricultural-intelligence.git main
        else
            echo "❌ No token provided"
        fi
        ;;
        
    D|d)
        echo "🧹 Clearing credentials..."
        git config --global --unset credential.helper
        git config --global credential.helper 'cache --timeout=3600'
        echo "✅ Credentials cleared"
        echo "Now run: git push origin main"
        echo "When prompted:"
        echo "  Username: QWarranto"
        echo "  Password: [Your Personal Access Token]"
        ;;
        
    *)
        echo "❌ Invalid option"
        ;;
esac

echo ""
echo "📋 If still having issues:"
echo "1. Visit: https://github.com/settings/tokens"
echo "2. Generate new token with 'repo' scope"
echo "3. Use as password when git asks"
echo "4. Or use: git config --global credential.helper store"