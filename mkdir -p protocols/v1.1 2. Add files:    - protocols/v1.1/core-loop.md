# BSF Loop Accelerator – Black Soldier Fly Larvae Side-Loop
**Daily Solids → Larvae Yield → Protein/Biogas Boost**

## Purpose
Processes fish/plant solids waste into high-value protein (larvae harvest) + frass (biogas feedstock/compost). Accelerates core loop by reducing solids load, closing protein cycle.

## Daily Workflow
1. Solids input: 5-15 kg/day wet waste from core loop (fish feces, plant trimmings).
2. BSF rearing: Stacked bins/trays, 25-35°C, 60-70% humidity.
3. Larvae growth: 14-21 days to prepupae.
4. Harvest: Self-harvest ramps → dry/freeze larvae (25-40% protein, high omega-3).
5. Frass output: Larvae manure → anaerobic digester for extra biogas or direct compost tea.
6. Yield calcs:
   - Conversion: 15-25% wet waste → dry larvae biomass.
   - Protein: 40-50% of dry larvae.
   - Biogas bonus: Frass VS higher than raw solids.

## Starter .py Snippet (bsfl_yield_calc.py – add to folder or simulations/)
```python
import numpy as np

def bsf_yield(wet_solids_kg_day, conversion_rate=0.20, dry_matter=0.30, protein_frac=0.45):
    dry_larvae = wet_solids_kg_day * conversion_rate * dry_matter
    protein_kg = dry_larvae * protein_frac
    frass_kg = wet_solids_kg_day * (1 - conversion_rate)
    return {
        'dry_larvae_kg': dry_larvae,
        'protein_kg': protein_kg,
        'frass_kg': frass_kg
    }

# Example daily
print(bsf_yield(10))  # Adjust params from trials
