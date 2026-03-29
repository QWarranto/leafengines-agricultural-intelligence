#!/usr/bin/env python3
"""
Test script for LeafEngines Claude Skill
"""

import json
from soil_analysis import SoilAnalyzer

def test_basic_analysis():
    """Test basic soil analysis functionality"""
    print("🧪 Testing LeafEngines Claude Skill")
    print("=" * 50)
    
    # Create analyzer
    analyzer = SoilAnalyzer()
    
    # Test soil data
    test_soil = {
        "ph": 6.2,
        "nitrogen_ppm": 25,
        "phosphorus_ppm": 15,
        "potassium_ppm": 150,
        "organic_matter_percent": 2.5,
        "field_size_acres": 50,
        "location": "Iowa"
    }
    
    print("📊 Test Soil Data:")
    print(json.dumps(test_soil, indent=2))
    print()
    
    # Run analysis
    print("🔬 Running Analysis...")
    results = analyzer.analyze_soil(test_soil)
    
    print("📈 Analysis Results:")
    print("=" * 50)
    
    # Display pH analysis
    ph_analysis = results["soil_analysis"]["ph"]
    print(f"pH: {ph_analysis['value']} ({ph_analysis['classification']})")
    print(f"Recommendation: {ph_analysis['recommendation']}")
    print()
    
    # Display nutrient analysis
    print("Nutrient Analysis:")
    for nutrient, analysis in results["soil_analysis"]["nutrients"].items():
        print(f"  {nutrient.capitalize()}: {analysis['value']} ppm ({analysis['classification']})")
    print()
    
    # Display crop recommendations
    print("🌱 Top Crop Recommendations:")
    for i, crop in enumerate(results["crop_recommendations"][:3], 1):
        print(f"{i}. {crop['crop']} (Suitability: {crop['suitability_score']:.0%})")
        print(f"   Expected Yield: {crop['expected_yield']['estimated']} {crop['expected_yield']['unit']}")
        print(f"   Expected Profit: ${crop['expected_profit']['total_field']:,.2f} total")
        if crop['key_considerations']:
            print(f"   Considerations: {crop['key_considerations'][0]}")
        print()
    
    # Display fertilizer recommendations
    print("🧪 Fertilizer Recommendations:")
    for nutrient, rec in results["fertilizer_recommendations"].items():
        print(f"  {nutrient.capitalize()}: {rec['required']} {rec['unit']}")
        print(f"    Suggested: {rec['product_suggestion']}")
    print()
    
    # Display confidence score
    print(f"🎯 Confidence Score: {results['confidence_score']:.0%}")
    print("=" * 50)
    
    return results

def test_sensor_validation():
    """Test sensor validation logic"""
    print("\n🔧 Testing Sensor Validation")
    print("=" * 50)
    
    # Simulate sensor drift scenario
    sensor_readings = {
        "current_ph": 6.8,
        "historical_ph_avg": 6.2,
        "months_since_calibration": 7,
        "sensor_type": "pH"
    }
    
    print("Sensor Data:")
    print(json.dumps(sensor_readings, indent=2))
    print()
    
    # Calculate drift
    drift_percent = abs((sensor_readings["current_ph"] - sensor_readings["historical_ph_avg"]) / 
                       sensor_readings["historical_ph_avg"] * 100)
    
    print(f"📊 Sensor Analysis:")
    print(f"  Current pH: {sensor_readings['current_ph']}")
    print(f"  Historical Average: {sensor_readings['historical_ph_avg']}")
    print(f"  Drift: {drift_percent:.1f}%")
    print(f"  Months since calibration: {sensor_readings['months_since_calibration']}")
    print()
    
    # Provide recommendations
    if drift_percent > 15:
        print("🚨 CRITICAL: Sensor drift >15% detected!")
        print("   Immediate recalibration required.")
    elif drift_percent > 10:
        print("⚠️  WARNING: Sensor drift 10-15% detected.")
        print("   Schedule recalibration soon.")
    elif sensor_readings["months_since_calibration"] > 6:
        print("ℹ️  INFO: Sensor due for routine calibration.")
        print("   Recommend recalibration within 30 days.")
    else:
        print("✅ Sensor appears to be functioning within normal parameters.")
    
    print("=" * 50)

def test_profitability_calculation():
    """Test profitability calculations"""
    print("\n💰 Testing Profitability Analysis")
    print("=" * 50)
    
    # Example market prices (2026)
    market_prices = {
        "corn": 5.25,  # $/bu
        "soybeans": 13.50,  # $/bu
        "wheat": 6.75,  # $/bu
        "tomatoes": 100.00  # $/ton
    }
    
    # Example costs
    production_costs = {
        "corn": {
            "seed": 120,  # $/acre
            "fertilizer": 180,
            "chemicals": 80,
            "labor": 60,
            "equipment": 100,
            "total": 540  # $/acre
        },
        "soybeans": {
            "seed": 70,
            "fertilizer": 90,
            "chemicals": 60,
            "labor": 50,
            "equipment": 80,
            "total": 350
        }
    }
    
    print("Market Prices:")
    for crop, price in market_prices.items():
        print(f"  {crop.capitalize()}: ${price:.2f}")
    print()
    
    # Calculate profitability for 100-acre field
    field_size = 100
    expected_yields = {
        "corn": 200,  # bu/acre
        "soybeans": 55  # bu/acre
    }
    
    print("Profitability Analysis for 100-acre field:")
    print("-" * 40)
    
    for crop in ["corn", "soybeans"]:
        revenue = expected_yields[crop] * market_prices[crop] * field_size
        cost = production_costs[crop]["total"] * field_size
        profit = revenue - cost
        roi = (profit / cost) * 100
        
        print(f"\n{crop.capitalize()}:")
        print(f"  Revenue: ${revenue:,.2f}")
        print(f"  Cost: ${cost:,.2f}")
        print(f"  Profit: ${profit:,.2f}")
        print(f"  ROI: {roi:.1f}%")
        print(f"  Profit/acre: ${profit/field_size:,.2f}")
    
    print("=" * 50)

if __name__ == "__main__":
    print("🌱 LeafEngines Claude Skill Test Suite")
    print("=" * 50)
    
    # Run all tests
    test_basic_analysis()
    test_sensor_validation()
    test_profitability_calculation()
    
    print("\n✅ All tests completed successfully!")
    print("\n📋 Next Steps:")
    print("1. Package skill directory into ZIP file")
    print("2. Upload to Claude Skills interface")
    print("3. Test with real agricultural queries")
    print("4. Gather feedback from Discord community")
    print("5. Iterate based on user feedback")