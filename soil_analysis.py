#!/usr/bin/env python3
"""
Soil Analysis Module for Claude Agricultural Intelligence Skill
"""

import json
import math
from typing import Dict, List, Optional, Tuple
import statistics

class SoilAnalyzer:
    """Analyze soil data and provide recommendations"""
    
    def __init__(self):
        self.crop_database = self._load_crop_database()
        self.usda_soil_reference = self._load_usda_reference()
        
    def _load_crop_database(self) -> Dict:
        """Load crop requirements database"""
        return {
            "corn": {
                "name": "Corn",
                "optimal_ph": (6.0, 6.8),
                "nitrogen_lbs": (150, 200),
                "phosphorus_lbs": (60, 80),
                "potassium_lbs": (120, 160),
                "yield_range": (150, 250),  # bu/acre
                "profit_range": (200, 400),  # $/acre
                "gdd_required": (2200, 2800)
            },
            "soybeans": {
                "name": "Soybeans",
                "optimal_ph": (6.0, 7.0),
                "nitrogen_lbs": (0, 0),  # Fixes own nitrogen
                "phosphorus_lbs": (40, 60),
                "potassium_lbs": (100, 140),
                "yield_range": (40, 70),  # bu/acre
                "profit_range": (150, 300),  # $/acre
                "gdd_required": (2000, 2500)
            },
            "wheat": {
                "name": "Wheat",
                "optimal_ph": (6.0, 7.0),
                "nitrogen_lbs": (80, 120),
                "phosphorus_lbs": (40, 60),
                "potassium_lbs": (80, 120),
                "yield_range": (60, 100),  # bu/acre
                "profit_range": (100, 250),  # $/acre
                "gdd_required": (1800, 2200)
            },
            "tomatoes": {
                "name": "Tomatoes",
                "optimal_ph": (6.0, 6.8),
                "nitrogen_lbs": (100, 150),
                "phosphorus_lbs": (80, 120),
                "potassium_lbs": (150, 200),
                "yield_range": (25, 40),  # tons/acre
                "profit_range": (2000, 5000),  # $/acre
                "gdd_required": (1500, 2000)
            }
        }
    
    def _load_usda_reference(self) -> Dict:
        """Load USDA soil reference values"""
        return {
            "ph_classification": {
                "strongly_acidic": (4.0, 5.4),
                "moderately_acidic": (5.5, 6.0),
                "slightly_acidic": (6.1, 6.5),
                "neutral": (6.6, 7.3),
                "slightly_alkaline": (7.4, 7.8),
                "moderately_alkaline": (7.9, 8.4),
                "strongly_alkaline": (8.5, 9.0)
            },
            "nutrient_sufficiency": {
                "nitrogen": {
                    "very_low": (0, 20),
                    "low": (20, 40),
                    "medium": (40, 60),
                    "high": (60, 80),
                    "very_high": (80, 1000)
                },
                "phosphorus": {
                    "very_low": (0, 10),
                    "low": (10, 20),
                    "medium": (20, 30),
                    "high": (30, 40),
                    "very_high": (40, 1000)
                },
                "potassium": {
                    "very_low": (0, 100),
                    "low": (100, 150),
                    "medium": (150, 200),
                    "high": (200, 250),
                    "very_high": (250, 1000)
                }
            }
        }
    
    def analyze_soil(self, soil_data: Dict) -> Dict:
        """
        Analyze soil data and provide recommendations
        
        Args:
            soil_data: Dictionary containing soil parameters
                {
                    "ph": 6.2,
                    "nitrogen_ppm": 25,
                    "phosphorus_ppm": 15,
                    "potassium_ppm": 150,
                    "organic_matter_percent": 2.5,
                    "field_size_acres": 50,
                    "location": "Iowa"
                }
        
        Returns:
            Dictionary with analysis results and recommendations
        """
        results = {
            "soil_analysis": {},
            "crop_recommendations": [],
            "fertilizer_recommendations": {},
            "sensor_validation": {},
            "confidence_score": 0.0
        }
        
        # Analyze pH
        ph = soil_data.get("ph")
        if ph:
            ph_analysis = self._analyze_ph(ph)
            results["soil_analysis"]["ph"] = ph_analysis
        
        # Analyze nutrients
        nutrients = {
            "nitrogen": soil_data.get("nitrogen_ppm"),
            "phosphorus": soil_data.get("phosphorus_ppm"),
            "potassium": soil_data.get("potassium_ppm")
        }
        
        nutrient_analysis = {}
        for nutrient, value in nutrients.items():
            if value is not None:
                nutrient_analysis[nutrient] = self._analyze_nutrient(nutrient, value)
        results["soil_analysis"]["nutrients"] = nutrient_analysis
        
        # Generate crop recommendations
        results["crop_recommendations"] = self._recommend_crops(soil_data)
        
        # Calculate fertilizer requirements
        results["fertilizer_recommendations"] = self._calculate_fertilizer(soil_data)
        
        # Calculate confidence score
        results["confidence_score"] = self._calculate_confidence(soil_data)
        
        return results
    
    def _analyze_ph(self, ph: float) -> Dict:
        """Analyze soil pH and provide classification"""
        classification = "unknown"
        recommendation = ""
        
        for class_name, (low, high) in self.usda_soil_reference["ph_classification"].items():
            if low <= ph <= high:
                classification = class_name.replace("_", " ").title()
                break
        
        # Provide recommendations based on pH
        if ph < 6.0:
            recommendation = "Consider adding lime to raise pH. Target pH 6.0-6.8 for most crops."
        elif ph > 7.5:
            recommendation = "Consider adding sulfur to lower pH. Target pH 6.0-6.8 for most crops."
        else:
            recommendation = "pH is in optimal range for most crops."
        
        return {
            "value": ph,
            "classification": classification,
            "recommendation": recommendation,
            "optimal_range": (6.0, 6.8)
        }
    
    def _analyze_nutrient(self, nutrient: str, value: float) -> Dict:
        """Analyze nutrient level and provide classification"""
        classification = "unknown"
        sufficiency_ranges = self.usda_soil_reference["nutrient_sufficiency"].get(nutrient, {})
        
        for level, (low, high) in sufficiency_ranges.items():
            if low <= value < high:
                classification = level.replace("_", " ").title()
                break
        
        return {
            "value": value,
            "classification": classification,
            "unit": "ppm"
        }
    
    def _recommend_crops(self, soil_data: Dict) -> List[Dict]:
        """Recommend crops based on soil conditions"""
        recommendations = []
        
        for crop_id, crop_info in self.crop_database.items():
            score = self._calculate_crop_score(crop_info, soil_data)
            
            if score > 0.5:  # Only recommend if score > 50%
                recommendations.append({
                    "crop": crop_info["name"],
                    "suitability_score": score,
                    "expected_yield": self._estimate_yield(crop_info, soil_data),
                    "expected_profit": self._estimate_profit(crop_info, soil_data),
                    "key_considerations": self._get_crop_considerations(crop_info, soil_data)
                })
        
        # Sort by suitability score (highest first)
        recommendations.sort(key=lambda x: x["suitability_score"], reverse=True)
        return recommendations[:3]  # Return top 3 recommendations
    
    def _calculate_crop_score(self, crop_info: Dict, soil_data: Dict) -> float:
        """Calculate suitability score for a crop (0-1)"""
        score = 0.0
        factors = 0
        
        # pH factor (30% weight)
        ph = soil_data.get("ph")
        if ph:
            optimal_low, optimal_high = crop_info["optimal_ph"]
            if optimal_low <= ph <= optimal_high:
                score += 0.3
            else:
                # Penalize based on distance from optimal range
                distance = min(abs(ph - optimal_low), abs(ph - optimal_high))
                penalty = max(0, 0.3 - (distance * 0.1))
                score += penalty
            factors += 1
        
        # Nutrient factors (40% weight total)
        nutrients = ["nitrogen", "phosphorus", "potassium"]
        nutrient_weight = 0.4 / len(nutrients)
        
        for nutrient in nutrients:
            ppm_value = soil_data.get(f"{nutrient}_ppm")
            if ppm_value:
                # Simple check: is nutrient level sufficient?
                if ppm_value >= 20:  # Basic sufficiency threshold
                    score += nutrient_weight
                factors += 1
        
        # Organic matter factor (20% weight)
        om = soil_data.get("organic_matter_percent")
        if om:
            if om >= 2.0:  # Good organic matter level
                score += 0.2
            elif om >= 1.0:  # Acceptable
                score += 0.1
            factors += 1
        
        # Location/climate factor (10% weight)
        # This would integrate with climate data in a real implementation
        score += 0.1
        factors += 1
        
        return score
    
    def _estimate_yield(self, crop_info: Dict, soil_data: Dict) -> Dict:
        """Estimate crop yield based on soil conditions"""
        yield_low, yield_high = crop_info["yield_range"]
        
        # Adjust based on soil quality
        ph = soil_data.get("ph", 6.5)
        adjustment = 1.0
        
        # pH adjustment
        optimal_low, optimal_high = crop_info["optimal_ph"]
        if optimal_low <= ph <= optimal_high:
            adjustment *= 1.0
        else:
            adjustment *= 0.8  # 20% reduction for suboptimal pH
        
        # Nutrient adjustment (simplified)
        avg_nutrient = statistics.mean([
            soil_data.get("nitrogen_ppm", 0) or 0,
            soil_data.get("phosphorus_ppm", 0) or 0,
            soil_data.get("potassium_ppm", 0) or 0
        ])
        
        if avg_nutrient >= 30:
            adjustment *= 1.0
        elif avg_nutrient >= 20:
            adjustment *= 0.9
        else:
            adjustment *= 0.7
        
        estimated_yield = (yield_low + yield_high) / 2 * adjustment
        
        return {
            "estimated": round(estimated_yield, 1),
            "range": (round(yield_low * adjustment, 1), round(yield_high * adjustment, 1)),
            "unit": "bu/acre" if crop_info["name"] in ["Corn", "Soybeans", "Wheat"] else "tons/acre"
        }
    
    def _estimate_profit(self, crop_info: Dict, soil_data: Dict) -> Dict:
        """Estimate profit based on crop and soil conditions"""
        profit_low, profit_high = crop_info["profit_range"]
        field_size = soil_data.get("field_size_acres", 1)
        
        # Adjust profit based on yield estimation
        yield_est = self._estimate_yield(crop_info, soil_data)
        adjustment = yield_est["estimated"] / ((yield_est["range"][0] + yield_est["range"][1]) / 2)
        
        estimated_profit = ((profit_low + profit_high) / 2) * adjustment * field_size
        
        return {
            "per_acre": round((profit_low + profit_high) / 2 * adjustment, 2),
            "total_field": round(estimated_profit, 2),
            "range": (round(profit_low * adjustment * field_size, 2), 
                     round(profit_high * adjustment * field_size, 2)),
            "unit": "USD"
        }
    
    def _get_crop_considerations(self, crop_info: Dict, soil_data: Dict) -> List[str]:
        """Get key considerations for growing this crop"""
        considerations = []
        
        # pH considerations
        ph = soil_data.get("ph")
        if ph:
            optimal_low, optimal_high = crop_info["optimal_ph"]
            if ph < optimal_low:
                considerations.append(f"pH ({ph}) is below optimal range ({optimal_low}-{optimal_high}). Consider adding lime.")
            elif ph > optimal_high:
                considerations.append(f"pH ({ph}) is above optimal range ({optimal_low}-{optimal_high}). Consider adding sulfur.")
        
        # Nutrient considerations
        for nutrient in ["nitrogen", "phosphorus", "potassium"]:
            ppm_value = soil_data.get(f"{nutrient}_ppm")
            if ppm_value and ppm_value < 20:
                considerations.append(f"{nutrient.capitalize()} level ({ppm_value} ppm) is low. Fertilizer application recommended.")
        
        # Crop-specific considerations
        if crop_info["name"] == "Corn":
            considerations.append("Corn requires significant nitrogen. Consider split applications.")
        elif crop_info["name"] == "Soybeans":
            considerations.append("Soybeans fix their own nitrogen. Inoculate seeds for best results.")
        elif crop_info["name"] == "Tomatoes":
            considerations.append("Tomatoes benefit from consistent moisture. Consider drip irrigation.")
        
        return considerations
    
    def _calculate_fertilizer(self, soil_data: Dict) -> Dict:
        """Calculate fertilizer requirements"""
        recommendations = {}
        
        # Nitrogen recommendation
        nitrogen_ppm = soil_data.get("nitrogen_ppm")
        if nitrogen_ppm is not None:
            target_nitrogen = 40  # ppm target for most crops
            nitrogen_deficit = max(0, target_nitrogen - nitrogen_ppm)
            nitrogen_lbs = nitrogen_deficit * 2.0  # Conversion factor
            recommendations["nitrogen"] = {
                "required": round(nitrogen_lbs, 1),
                "unit": "lbs N/acre",
                "product_suggestion": "Urea (46-0-0) or Ammonium Nitrate (34-0-0)"
            }
        
        # Phosphorus recommendation
        phosphorus_ppm = soil_data.get("phosphorus_ppm")
        if phosphorus_ppm is not None:
            target_phosphorus = 25  # ppm target
            phosphorus_deficit = max(0, target_phosphorus - phosphorus_ppm)
            phosphorus_lbs = phosphorus_deficit * 4.5  # Conversion factor
            recommendations["phosphorus"] = {
                "required": round(phosphorus_lbs, 1),
                "unit": "lbs P₂O₅/acre",
                "product_suggestion": "Triple Super Phosphate (0-46-0) or DAP (18-46-0)"
            }
        
        # Potassium recommendation
        potassium_ppm = soil_data.get("potassium_ppm")
        if potassium_ppm is not None:
            target_potassium = 175  # ppm target
            potassium_deficit = max(0, target_potassium - potassium_ppm)
            potassium_lbs = potassium_deficit * 1.2  # Conversion factor
            recommendations["potassium"] = {
                "required": round(potassium_lbs, 1),
                "unit": "lbs K₂O/acre",
                "product_suggestion": "Potassium Chloride (0-0-60) or Potassium Sulfate (0-0-50)"
            }
        
        return recommendations
    
    def _calculate_confidence(self, soil_data: Dict) -> float:
        """Calculate confidence score for recommendations (0-1)"""
        confidence = 1.0
        
        # Penalize for missing data
        required_fields = ["ph", "nitrogen_ppm", "phosphorus_ppm", "potassium_ppm"]
        missing_count = sum(1 for field in required_fields if soil_data.get(field) is None)
        
        if missing_count > 0:
            confidence *= (1 - (missing_count * 0.15))  # 15% penalty per missing field
        
        # Penalize for extreme values
        ph = soil_data.get("ph")
        if ph and (ph < 4.0 or ph > 9.0):
            confidence *= 0.7  # 30% penalty for extreme pH
        
        # Penalize for very low nutrient levels
        low_nutrient_count = 0
        for nutrient in ["nitrogen_ppm", "phosphorus_ppm", "potassium_ppm"]:
            value = soil_data.get(nutrient)
            if value and value < 10:
                low_nutrient_count += 1
        
        if low_nutrient_count > 0:
            confidence *= (1 - (low_nutrient_count * 0.1))  # 10% penalty per very low nutrient
        
        return round(max(0.0, min(1.0, confidence)), 2)
    
