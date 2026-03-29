#!/bin/bash
echo "📦 Packaging LeafEngines Claude Skill (Correct Anthropic Structure)"
echo "==================================================================="

# According to Anthropic: "Ensure the folder name matches your Skill's name"
# Our skill name is "agricultural-intelligence" (from SKILL.md YAML frontmatter)
SKILL_NAME="agricultural-intelligence"
FOLDER_NAME="$SKILL_NAME"
ZIP_FILE="$SKILL_NAME.zip"

echo "1. Cleaning up old files..."
rm -f "$ZIP_FILE"
rm -rf "$FOLDER_NAME"

echo "2. Creating skill folder: $FOLDER_NAME/"
mkdir -p "$FOLDER_NAME"

echo "3. Copying skill files to folder..."
cp SKILL.md "$FOLDER_NAME/"
cp REFERENCE.md "$FOLDER_NAME/"
cp README.md "$FOLDER_NAME/"
cp soil_analysis.py "$FOLDER_NAME/"
cp test_skill.py "$FOLDER_NAME/"
cp validate_skill.py "$FOLDER_NAME/"
cp requirements.txt "$FOLDER_NAME/"

echo "4. Creating installation guide..."
cat > "$FOLDER_NAME/INSTALL.md" << 'EOF'
# Installation Guide

## For Claude Desktop/Web

### Method 1: Direct Import (Recommended)
1. Download `agricultural-intelligence.zip`
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

## Python Requirements
If you want to use the Python scripts independently:
```bash
cd agricultural-intelligence
pip install -r requirements.txt
```

## Testing
Run the test script to verify installation:
```bash
cd agricultural-intelligence
python test_skill.py
```

## Validation
Check the skill meets Anthropic requirements:
```bash
cd agricultural-intelligence
python validate_skill.py
```

## Usage
Once installed, Claude will automatically use the skill when you ask agricultural questions like:
- "Analyze this soil test data..."
- "What crops should I plant?"
- "Calculate profitability for my farm..."
- "Check my sensor calibration..."

## Support
Join our Discord community: https://discord.gg/leafengines
EOF

echo "5. Creating ZIP with CORRECT Anthropic structure..."
echo "   According to Anthropic documentation:"
echo "   ✅ Correct: agricultural-intelligence.zip → agricultural-intelligence/ → SKILL.md"
echo "   ❌ Incorrect: agricultural-intelligence.zip → SKILL.md (files directly in root)"
echo ""
echo "   Creating ZIP with folder as root..."
zip -r "$ZIP_FILE" "$FOLDER_NAME"

echo "6. Verifying structure..."
echo ""
echo "📋 Package Contents (must show folder as root):"
unzip -l "$ZIP_FILE" | head -15

echo ""
echo "✅ Package created: $ZIP_FILE"
echo ""
echo "📁 CORRECT Structure (per Anthropic requirements):"
echo "$ZIP_FILE"
echo "└── $FOLDER_NAME/"
echo "    ├── SKILL.md                    (Main skill file)"
echo "    ├── REFERENCE.md                (Agricultural formulas)"
echo "    ├── soil_analysis.py            (Python analysis engine)"
echo "    ├── test_skill.py               (Test suite)"
echo "    ├── validate_skill.py           (Validation script)"
echo "    ├── requirements.txt            (Python dependencies)"
echo "    ├── INSTALL.md                  (Installation guide)"
echo "    └── README.md                   (Documentation)"
echo ""
echo "🔍 Structure Validation:"
if unzip -l "$ZIP_FILE" | grep -q "^[[:space:]]*[0-9].*$FOLDER_NAME/"; then
    echo "✅ CORRECT: Files are inside $FOLDER_NAME/ folder"
else
    echo "❌ INCORRECT: Files are directly in ZIP root"
fi

echo ""
echo "🚀 Next Steps:"
echo "1. Upload $ZIP_FILE to Claude Skills interface"
echo "2. Test with example agricultural queries"
echo "3. Share with Discord community (1,977 Reddit viewers)"
echo "4. Submit to Anthropic skills repository"
echo ""
echo "🌱 Skill follows exact Anthropic format. Ready for deployment!"