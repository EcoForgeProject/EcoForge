# EcoForge – Open-Source Closed-Loop AI Homesteads

**Grok-optimized regenerative systems for Earth abundance & Mars readiness.**  
Vermiponics + biogas spine + RO + Grok reasoning/voice agents (Ara default) + Optimus hooks. Family-scale nodes scaling to multi-node networks.

## Visual Overview

![Container 1 Interior - Stacked Grow Beds](https://raw.githubusercontent.com/SeanSestinaEcoForge/SeanSestinaEcoForge/main/images/container-interior.jpg)  
*Insulated shipping container setup with vermiponics beds and lighting for year-round abundance*

![Closed-Loop System Diagram](https://raw.githubusercontent.com/SeanSestinaEcoForge/SeanSestinaEcoForge/main/images/closed-loop-diagram.jpg)  
*Nutrient & energy flow: Vermiponics → Biogas → RO → Powerwall hybrid (pH, energy, recovery all tied in)*

![Reverse Osmosis Unit](https://raw.githubusercontent.com/SeanSestinaEcoForge/SeanSestinaEcoForge/main/images/ro-unit.jpg)  
*Low-energy RO achieving <6 ppm permeate in the closed loop*

![Biogas Digester Integration](https://raw.githubusercontent.com/SeanSestinaEcoForge/SeanSestinaEcoForge/main/images/biogas-digester.jpg)  
*Biogas spine: Waste-to-methane powering storage & ops*

**Current Status (March 2026)**  
- Blueprint v3 "Supernova" locked: 95–96.5% resource recovery, NH₃ <6 ppm, RO 0.55 kWh/m³, 18.8 LMH flux.  
- API: FastAPI /simulate endpoint (vermiponic + RO ODEs) – live but throttled.  
- Grok Integration: In progress – API key ready, testing reasoning for sim tuning + realtime voice agents (Ara voice locked for warm, conversational agents). Awaiting credits top-up for heavy usage.  
- Physical Build: Container 1 prototype queued (Cambridge I-70/I-77 node) – awaiting site confirmation from Dad/Danny.  
- Team: Core push with Danny (build experience), Bridget (reviewing repo/sims), Sean leading. Open for aligned contributors!  
- Treasury: Activation pending (X Money/multisig) – $0 current.  

**Vision**  
True closed-loop abundance: Waste-to-food-to-energy cycles powering homesteads. Grok agents (Ara voice) guide ops, explain sims, optimize in realtime. Dual-use Earth/Mars (Starship scalable).  
Full details: [docs/EcoForge-Complete-Vision-Consistency-v3.md]

**Key Metrics (v3 Supernova – Targets Achieved in Sims)**  
- Vermiponics: 95–96.5% recovery, NH₃ <6 ppm  
- RO: 4.5–5.8 ppm permeate, 0.55 kWh/m³  
- Pilot Scale: 10-person node → 400+ lbs/month surplus food, 30–90 min daily ops  
Live dashboard/sensor feeds: In dev (ESP32 → Grok → Ara alerts)

**Quick Start**  
1. Clone: `git clone https://github.com/SeanSestinaEcoForge/SeanSestinaEcoForge`  
2. Install: `pip install -r requirements.txt`  
3. Run sim: `python simulations/sim-aquaponics-nutrient-cycle.py`  
4. API: `uvicorn api.main:app --reload` (throttled)  
5. Grok/Voice: Key at console.x.ai. Test Ara TTS in playground (x.ai/api/voice):  
   Sample prompt: "Fam, let's optimize this vermiponic cycle step by step."  

**Roadmap & Phases**  
- **Phase 1**: Blueprint lock + sim validation → **Complete**  
- **Phase 2**: Container 1 physical build + first cycle → **Next** (queued for site/Danny/Dad greenlight)  
- **Phase 3**: Grok agents live (reasoning + Ara realtime voice), multi-node scaling → Queued  
- **Phase 4**: Treasury activation, community nodes, Optimus integration  

Checklists: [docs/Phase2_Checklist.md] | [docs/Master-BOM-All-Tiers.md]

**Get Involved**  
- Fork & prototype your node  
- PR code/docs/sims/feedback  
- Issues or reach out @SeanSestina  
Current priorities: Sensor integration examples, Grok tool calling stubs, BOM sourcing updates, Container 1 build sequencing  

License: MIT  
Let's forge abundance together! 🌱⚡️🚀
