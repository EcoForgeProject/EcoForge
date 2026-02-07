## EcoForge – Open-Source Closed-Loop AI Homesteads

**Earth abundance today. Mars readiness tomorrow.**

EcoForge is building modular, AI-optimized closed-loop systems for sustainable food production — starting with aquaponics + vermiponics, and scaling toward fully autonomous habitats on Earth and eventually Mars.

- Grok-optimized models & decision protocols  
- Optimus-compatible automation hooks (future)  
- Starship-scale transport & deployment thinking  

MIT Licensed · Community-first · Always improving

## Current Focus: Aquaponics + Vermiponics Simulation

We're iterating on high-fidelity simulations that model:
- Fish growth & feed conversion
- Plant nutrient uptake (nitrate preferred)
- Nitrification (ammonia → nitrite → nitrate)
- Vermicomposting (solids → ammonia release)
- Dissolved oxygen dynamics & crashes
- Alkalinity consumption & approximate pH effects

These models help test parameter ranges, stress scenarios, and long-term stability before building physical prototypes.

### Available Simulations

All simulations live in the `simulations/` folder.

| File | Description | Features | How to Run |
|------|-------------|----------|------------|
| `sim-aquaponics-nutrient-cycle.py` | Basic nutrient cycling model | Ammonia, nitrite, nitrate, simple uptake | `python simulations/sim-aquaponics-nutrient-cycle.py` |
| `aquaponics-vermiponics-enhanced-ph-alk.py` | Enhanced version with vermiponics, DO, temp scaling, pH & alkalinity | Temperature Q10, DO limitation, pH-dependent nitrification, alkalinity decay | `python simulations/aquaponics-vermiponics-enhanced-ph-alk.py` |
| `aquaponics-vermiponics-enhanced-ph-alk.ipynb` | **Interactive Jupyter notebook** | Sliders for temperature & initial alkalinity, real-time plots of biomass, nutrients, DO, pH, alkalinity | `jupyter notebook simulations/aquaponics-vermiponics-enhanced-ph-alk.ipynb` |

**Dependencies** (install once):
```bash
pip install -r requirements.txt
# or manually:
pip install numpy scipy matplotlib ipywidgets jupytercd EcoForge
jupyter notebook simulations/aquaponics-vermiponics-enhanced-ph-alk.ipynb
