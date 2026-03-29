# LeafEngines Agricultural Intelligence Claude Skill

## Overview
This Claude Skill provides agricultural intelligence including soil analysis, crop recommendations, profit calculations, and farm optimization advice. It's designed for farmers, agricultural professionals, and anyone working with soil data.

## Features

### Core Capabilities
- **Soil Analysis**: Interpret soil test results and provide recommendations
- **Crop Recommendations**: Suggest optimal crops based on soil conditions
- **Profitability Analysis**: Calculate profit margins and ROI for different crops
- **Sensor Validation**: Detect sensor drift and calibration issues
- **Planting Guidance**: Provide planting schedules and timing recommendations

### Technical Features
- Integration with SoilSidekickPro API
- USDA soil database references
- Market price analysis
- Weather data integration
- Executable Python scripts for complex calculations

## Installation

### For Claude Desktop/Web
1. Download the skill package
2. Follow Claude's skill installation instructions
3. Import the skill into your Claude workspace

### Requirements
- Python 3.8+
- Required packages: `requests`, `pandas`, `numpy`
- Internet connection for API calls

## Usage Examples

### Basic Soil Analysis
```
User: "My soil test shows pH 6.2, nitrogen 25 ppm, phosphorus 15 ppm, potassium 150 ppm. What should I plant?"

Claude with Skill: "Based on your soil analysis, here are my recommendations..."
```

### Profitability Comparison
```
User: "Should I plant corn or soybeans on my 100-acre field?"

Claude with Skill: "Let me calculate the profitability for both options..."
```

### Sensor Troubleshooting
```
User: "My soil moisture readings seem inconsistent. What should I do?"

Claude with Skill: "Sensor drift is common. Here's how to validate and recalibrate..."
```

## File Structure
```
leafengines-claude-skill/
├── Skill.md              # Main skill definition
├── REFERENCE.md          # Agricultural reference data
├── soil_analysis.py      # Python analysis scripts
├── profitability.py      # Profit calculation scripts
├── sensor_validation.py  # Sensor calibration scripts
└── README.md            # This file
```

## Integration Points

### External APIs
- **SoilSidekickPro**: `https://app.soilsidekickpro.com/leafengines`
- **USDA Soil Data**: SSURGO database access
- **Market Prices**: Real-time commodity pricing
- **Weather Data**: NOAA and weather service integration

### Data Formats Supported
- CSV soil test results
- Excel spreadsheets
- PDF reports (with text extraction)
- JSON sensor data exports

## Best Practices

### For Accurate Results
1. Provide complete soil test data when possible
2. Include field size and location information
3. Specify your primary goals (profit, sustainability, etc.)
4. Mention any constraints (water availability, equipment, etc.)

### For Sensor Data
1. Regular calibration (every 3-6 months)
2. Multiple sensor validation
3. Historical trend analysis
4. USDA reference comparison

## Community & Support

### Discord Community
Join our agricultural AI community: https://discord.gg/leafengines

### GitHub Repository
Contribute to the open source version: https://github.com/QWarranto/leafengines-clawhub-skill

### Feedback & Suggestions
We welcome feedback from agricultural professionals. Your input helps improve the skill for everyone.

## Development

### Adding New Crops
Edit the crop database in `soil_analysis.py` to add new crops with their requirements.

### Custom Formulas
Modify the calculation methods in the Python scripts to implement custom agricultural formulas.

### API Integration
Add new API endpoints in the appropriate script files for additional data sources.

## Security & Privacy
- All calculations can be performed locally
- User data is not stored without permission
- API calls use secure HTTPS connections
- Agricultural data is treated as confidential

## Acknowledgments
This skill was developed with feedback from 1,977 agricultural professionals on Reddit who identified critical issues like sensor drift and calibration requirements.

Special thanks to the agricultural expert who highlighted: "Soil sensors drift ~15% after 6 months without calibration. AI planting recommendations go sideways fast if you ignore it."

## License
This skill is provided under the MIT License. See LICENSE file for details.

## Version
Current version: 1.0.0
Last updated: March 29, 2026
## 🚀 Complete package deployed: Sun Mar 29 13:58:45 EDT 2026
