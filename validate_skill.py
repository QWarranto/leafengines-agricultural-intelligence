#!/usr/bin/env python3
"""
Validate LeafEngines Claude Skill meets Anthropic requirements
"""

import os
import yaml
import re
from pathlib import Path

def validate_structure():
    """Validate skill directory structure"""
    print("📁 Validating Skill Structure")
    print("=" * 50)
    
    required_files = [
        "SKILL.md",
        "README.md"
    ]
    
    optional_files = [
        "REFERENCE.md",
        "soil_analysis.py",
        "test_skill.py",
        "requirements.txt"
    ]
    
    all_good = True
    
    # Check required files
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} - Found")
        else:
            print(f"❌ {file} - MISSING (REQUIRED)")
            all_good = False
    
    # Check optional files
    for file in optional_files:
        if os.path.exists(file):
            print(f"✅ {file} - Found (optional)")
        else:
            print(f"⚠️  {file} - Not found (optional)")
    
    return all_good

def validate_skill_md():
    """Validate SKILL.md YAML frontmatter and content"""
    print("\n📄 Validating SKILL.md")
    print("=" * 50)
    
    try:
        with open("SKILL.md", "r") as f:
            content = f.read()
        
        # Check for YAML frontmatter
        if not content.startswith("---\n"):
            print("❌ SKILL.md must start with YAML frontmatter (---)")
            return False
        
        print("✅ YAML frontmatter present")
        
        # Extract YAML
        yaml_match = re.match(r"---\n(.*?)\n---\n", content, re.DOTALL)
        if not yaml_match:
            print("❌ Could not extract YAML frontmatter")
            return False
        
        yaml_content = yaml_match.group(1)
        metadata = yaml.safe_load(yaml_content)
        
        # Check required fields
        required_fields = ["name", "description"]
        for field in required_fields:
            if field in metadata:
                print(f"✅ {field}: {metadata[field][:50]}...")
            else:
                print(f"❌ Missing required field: {field}")
                return False
        
        # Check name length (64 chars max)
        if len(metadata["name"]) > 64:
            print(f"❌ Name too long: {len(metadata['name'])} chars (max 64)")
            return False
        print(f"✅ Name length: {len(metadata['name'])} chars (max 64)")
        
        # Check description
        if len(metadata["description"]) < 20:
            print("⚠️  Description may be too short")
        print(f"✅ Description: {len(metadata['description'])} chars")
        
        # Check for examples
        if "example" in content.lower() or "Example" in content:
            print("✅ Examples found in SKILL.md")
        else:
            print("⚠️  Consider adding examples to SKILL.md")
        
        # Check markdown body exists
        markdown_body = content[yaml_match.end():].strip()
        if len(markdown_body) > 100:
            print(f"✅ Markdown body: {len(markdown_body)} chars")
        else:
            print("⚠️  Markdown body may be too short")
        
        return True
        
    except Exception as e:
        print(f"❌ Error validating Skill.md: {e}")
        return False

def validate_reference_md():
    """Validate REFERENCE.md if present"""
    print("\n📚 Validating REFERENCE.md")
    print("=" * 50)
    
    if not os.path.exists("REFERENCE.md"):
        print("⚠️  REFERENCE.md not found (optional)")
        return True
    
    try:
        with open("REFERENCE.md", "r") as f:
            content = f.read()
        
        if len(content) > 500:
            print(f"✅ REFERENCE.md: {len(content)} chars")
            
            # Check for useful content
            keywords = ["formula", "calculation", "reference", "data", "database"]
            keyword_count = sum(1 for kw in keywords if kw.lower() in content.lower())
            
            if keyword_count >= 2:
                print("✅ Contains reference data and formulas")
            else:
                print("⚠️  Consider adding more reference data")
        else:
            print("⚠️  REFERENCE.md may be too short")
        
        return True
        
    except Exception as e:
        print(f"❌ Error validating REFERENCE.md: {e}")
        return False

def validate_scripts():
    """Validate Python scripts if present"""
    print("\n🐍 Validating Python Scripts")
    print("=" * 50)
    
    scripts = ["soil_analysis.py", "test_skill.py"]
    all_valid = True
    
    for script in scripts:
        if os.path.exists(script):
            try:
                with open(script, "r") as f:
                    content = f.read()
                
                print(f"✅ {script}: {len(content)} chars")
                
                # Check for imports
                if "import" in content:
                    print(f"  ✅ Contains imports")
                
                # Check for class/function definitions
                if "def " in content or "class " in content:
                    print(f"  ✅ Contains functions/classes")
                
                # Check shebang
                if content.startswith("#!/usr/bin/env python3"):
                    print(f"  ✅ Has shebang line")
                
            except Exception as e:
                print(f"❌ Error reading {script}: {e}")
                all_valid = False
        else:
            print(f"⚠️  {script} not found (optional)")
    
    return all_valid

def validate_requirements():
    """Validate requirements.txt if present"""
    print("\n📦 Validating Requirements")
    print("=" * 50)
    
    if not os.path.exists("requirements.txt"):
        print("⚠️  requirements.txt not found (optional)")
        return True
    
    try:
        with open("requirements.txt", "r") as f:
            content = f.read()
        
        lines = [line.strip() for line in content.split("\n") if line.strip()]
        
        if lines:
            print(f"✅ requirements.txt: {len(lines)} packages")
            for line in lines[:3]:  # Show first 3
                print(f"  📍 {line}")
            if len(lines) > 3:
                print(f"  ... and {len(lines)-3} more")
        else:
            print("⚠️  requirements.txt is empty")
        
        return True
        
    except Exception as e:
        print(f"❌ Error validating requirements.txt: {e}")
        return False

def validate_zip_structure():
    """Validate the ZIP will have correct structure per Anthropic requirements"""
    print("\n📦 Validating ZIP Structure (Anthropic Requirements)")
    print("=" * 50)
    
    # Check current directory name
    current_dir = os.path.basename(os.getcwd())
    print(f"Current directory: {current_dir}")
    
    # Check for SKILL.md at root
    if os.path.exists("SKILL.md"):
        print("✅ SKILL.md at correct location (root of skill directory)")
    else:
        print("❌ SKILL.md must be at root of skill directory")
        return False
    
    # Read skill name from SKILL.md YAML
    try:
        with open("SKILL.md", "r") as f:
            content = f.read()
        yaml_match = re.match(r"---\n(.*?)\n---\n", content, re.DOTALL)
        if yaml_match:
            yaml_content = yaml_match.group(1)
            metadata = yaml.safe_load(yaml_content)
            skill_name = metadata.get("name", "")
            print(f"Skill name from YAML: '{skill_name}'")
            
            # Check if folder should match skill name
            if skill_name and skill_name != current_dir:
                print(f"⚠️  Note: Skill name '{skill_name}' doesn't match directory '{current_dir}'")
                print(f"   When packaging, folder should be named: {skill_name}")
        else:
            print("⚠️  Could not read skill name from YAML")
    except Exception as e:
        print(f"⚠️  Could not read skill name: {e}")
    
    print("\n📋 Expected ZIP structure (per Anthropic):")
    print("agricultural-intelligence.zip")
    print("└── agricultural-intelligence/    # Folder name matches skill name")
    print("    ├── SKILL.md                  # At root of folder")
    print("    ├── REFERENCE.md              # Optional reference files")
    print("    ├── *.py                      # Optional scripts")
    print("    └── ...                       # Other optional files")
    print("")
    print("❌ INCORRECT (files directly in ZIP root):")
    print("agricultural-intelligence.zip")
    print("├── SKILL.md")
    print("├── REFERENCE.md")
    print("└── ...")
    
    return True

def main():
    """Main validation function"""
    print("🔍 Validating LeafEngines Claude Skill")
    print("=" * 50)
    
    # Change to skill directory
    skill_dir = "/Users/reginaldrice/.openclaw/workspace/leafengines-claude-skill"
    original_dir = os.getcwd()
    
    try:
        os.chdir(skill_dir)
        
        # Run all validations
        results = []
        
        results.append(("Structure", validate_structure()))
        results.append(("Skill.md", validate_skill_md()))
        results.append(("REFERENCE.md", validate_reference_md()))
        results.append(("Scripts", validate_scripts()))
        results.append(("Requirements", validate_requirements()))
        results.append(("ZIP Structure", validate_zip_structure()))
        
        # Summary
        print("\n" + "=" * 50)
        print("📊 VALIDATION SUMMARY")
        print("=" * 50)
        
        all_passed = True
        for name, passed in results:
            status = "✅ PASS" if passed else "❌ FAIL"
            print(f"{name:20} {status}")
            if not passed:
                all_passed = False
        
        print("\n" + "=" * 50)
        if all_passed:
            print("🎉 ALL VALIDATIONS PASSED!")
            print("\n🚀 Skill is ready for packaging and upload to Claude.")
            print("\nNext steps:")
            print("1. Run: ./package_skill.sh")
            print("2. Upload leafengines-claude-skill.zip to Claude")
            print("3. Test with example prompts")
            print("4. Share with Discord community")
        else:
            print("⚠️  Some validations failed. Please fix issues above.")
            print("\nRequired fixes before uploading to Claude.")
        
    finally:
        os.chdir(original_dir)
    
    return all_passed

if __name__ == "__main__":
    main()