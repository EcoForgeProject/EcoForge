# EcoForge Simulation Roadmap (March 2026)

**Goal:** Maintain a single source of truth for all simulations, track what has been built and validated, and prioritize the next ones to generate the best possible data for Phase 2 container builds and Mars analogs.

## 1. Simulations Already Built & Run (Earth Baseline)

| Simulation | File(s) | Key Outputs | Status |
|------------|---------|-------------|--------|
| Vermiponics / Aquaponics Nutrient Cycle (ODE) | `sim-aquaponics-nutrient-cycle.py` + enhanced Jupyter version | 95–96.5% recovery, NH₃ <6 ppm, vermicast estimates | Fully built, tested, FastAPI-integrated |
| Reverse Osmosis (RO) Model | Integrated in `/simulate` endpoint | 0.55 kWh/m³, 18.8 LMH flux, TDS <6 ppm | Live & paired |
| Combined Closed-Loop (Vermiponics + RO) | FastAPI `/simulate` | Full water + nutrient recovery | Active |
| Basic Energy Balance / Surplus | `energy_basic.py` | +15–27 kWh/day surplus | Functional |
| Fouling Simulation | `fouling_sim.py` | Drip-line & membrane fouling | Built |
| Parameter Sweep Utility | `param_sweep_example.py` | Rapid parameter testing | Built |
| Visualization Utilities | `viz_utils.py` | Plotting with error bands | Built |
| Orbital Solar Placeholder (v0.1) | `space_solar_v0.1.py` | Simple 5× multiplier | Placeholder only |

## 2. Simulations Still Needed (Prioritized)

**High Priority (Next – Direct Impact on Phase 2 Container Build)**
- Biogas / Anaerobic Digestion Model (methane yield, digestate return, energy generation, interaction with vermiponics)
- Upgraded Full Energy Balance (include biogas + seasonal heating + Powerwall logic)
- Grok Real-Time Optimization Loop (sensor data → Grok tool-calling → adjustments)

**Medium Priority (Mars Layer)**
- Mars-adapted vermiponics / regolith nutrient cycle (low-G, dust, regolith chemistry)
- Low-G nutrient distribution & fluid dynamics
- Mars-specific RO under low pressure/temperature
- Integrated Mars closed-loop sim (orbital solar + all loops)
- Chaos / failure-mode simulation for Mars habitat

**Low Priority (Later)**
- Multi-node scaling & surplus sharing
- Live ESP32 sensor + noise simulation

## 3. Execution Rules
- One simulation at a time
- Run → Document results → Update BOM/checklists → Commit
- Every sim must produce **actionable numbers** for the Cambridge pilot and Phase 2 checklist
- Use worktrees when the controller API grows to keep Earth pilot and Mars experiments separate

**Next Up (Recommended):**  
Start with the **Biogas / Anaerobic Digestion ODE simulation** — it fills the largest gap in the current closed-loop and directly supports the physical container build.

---

We now have one clear master document.  
You can commit this, then we can immediately start building the Biogas sim if you're ready.

Want me to generate the full **Biogas simulation code** next (ready to drop into `simulations/sim-biogas-digestion.py`)?

Or anything else you want to adjust in this roadmap first?

Let me know, fam. We're organized and focused now. ❤️🥷🌱🪐♾️⚒️
