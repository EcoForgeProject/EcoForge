# src/tools/energy.py
def chp_efficiency_calc(power_kw: float = 10.0, fuel_type: str = "propane") -> dict:
    """Simple CHP calc (expand later with real physics)"""
    if fuel_type == "propane":
        base_eff = 0.78
    elif fuel_type == "biodiesel":
        base_eff = 0.75
    else:
        base_eff = 0.70
    
    electrical = power_kw * base_eff
    thermal = power_kw * (0.85 - base_eff)  # approx heat recovery
    
    return {
        "electrical_kw": round(electrical, 2),
        "thermal_kw": round(thermal, 2),
        "total_eff": round(base_eff + (thermal / power_kw), 3),
        "margin_pct": 35  # placeholder from patch
    }

# Test
if __name__ == "__main__":
    print(chp_efficiency_calc(7.5, "propane"))
