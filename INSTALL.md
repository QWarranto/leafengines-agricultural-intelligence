# Installation Guide

## For Claude Desktop/Web

### Method 1: Direct Import (Recommended)
1. Download `agricultural-intelligence.zip` from GitHub releases
2. Open Claude and go to Skills settings
3. Click "Import Skill"
4. Select the ZIP file
5. The skill will be available immediately

### Method 2: Manual Installation
1. Extract the ZIP file
2. Place the `agricultural-intelligence` folder in Claude's skills directory:
   - **macOS**: `~/Library/Application Support/Claude/skills/`
   - **Windows**: `%APPDATA%\Claude\skills\`
   - **Linux**: `~/.config/Claude/skills/`
3. Restart Claude

### Method 3: GitHub Integration (Automatic Updates)
1. Connect this GitHub repository to Claude skills platform
2. Enable automatic updates
3. Changes in GitHub will automatically sync to Claude

## Python Requirements
If you want to use the Python scripts independently:
```bash
pip install -r requirements.txt
```

## Testing
Run the test script to verify installation:
```bash
python test_skill.py
```

## Validation
Check the skill meets Anthropic requirements:
```bash
python validate_skill.py
```

## Usage
Once installed, Claude will automatically use the skill when you ask agricultural questions like:
- "Analyze this soil test data..."
- "What crops should I plant?"
- "Calculate profitability for my farm..."
- "Check my sensor calibration..."

## Support
- **GitHub Issues**: Report bugs or request features
- **Discord**: Join our community at https://discord.gg/leafengines
- **Email**: Contact for enterprise support