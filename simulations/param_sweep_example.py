# simulations/param_sweep_example.py
import numpy as np
import matplotlib.pyplot as plt
from aquaponics_vermiponics_enhanced_ph_alk import run_simulation  # assume this function exists in the enhanced file

# Example: sweep temperature impact on nitrate production
temps = np.linspace(15, 35, 21)          # 15–35 °C
nitrates = []

for t in temps:
    # Pass temperature to simulation function (adapt to your actual args)
    results = run_simulation(temperature=t, days=30)
    final_nitrate = results['nitrate'][-1] if 'nitrate' in results else 0
    nitrates.append(final_nitrate)

plt.plot(temps, nitrates, marker='o')
plt.xlabel('Temperature (°C)')
plt.ylabel('Final Nitrate Concentration (mg/L)')
plt.title('Temperature Sensitivity – Nitrate Production')
plt.grid(True)
plt.savefig('simulations/temp_nitrate_sweep.png')
plt.show()
