# EcoForge – Open-Source Closed-Loop AI Homesteads

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-F37626.svg?logo=jupyter)](https://jupyter.org/)

**Earth abundance today. Mars readiness tomorrow.**

EcoForge builds modular, AI-optimized closed-loop systems for sustainable food production — starting with aquaponics + vermiponics, and scaling toward fully autonomous habitats on Earth and eventually Mars.

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

All models are located in the `simulations/` directory.

| File                                              | Description                                                                 | Key Features                                                                                  | How to Run                                                                 |
|---------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| `sim-aquaponics-nutrient-cycle.py`                | Basic nutrient cycling model                                                | Ammonia → nitrite → nitrate conversion, simple plant uptake                                  | `python simulations/sim-aquaponics-nutrient-cycle.py`                      |
| `aquaponics-vermiponics-enhanced-ph-alk.py`       | Enhanced aquaponics + vermiponics with pH & alkalinity dynamics            | Temperature scaling (Q10), DO limitation & crashes, vermicomposting, pH-dependent nitrification, alkalinity decay | `python simulations/aquaponics-vermiponics-enhanced-ph-alk.py`             |
| `aquaponics-vermiponics-enhanced-ph-alk.ipynb`    | **Interactive Jupyter notebook** for parameter tuning                      | Real-time plots, sliders for temperature and initial alkalinity, full system overview (biomass, nutrients, DO, pH, Alk) | `jupyter notebook simulations/aquaponics-vermiponics-enhanced-ph-alk.ipynb` |

**Quick setup (if you haven't already):**
```bash
pip install -r requirements.txt
# or manually:
pip install numpy scipy matplotlib ipywidgets jupyter
