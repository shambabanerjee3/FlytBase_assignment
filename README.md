# FlytBase_assignment
Multi-Drone Strategic Deconfliction Simulation (Python)
Overview

This project implements a strategic (pre-flight) deconfliction system for multiple UAVs operating in shared 3D airspace.
It simulates a primary mission drone and multiple secondary drones, predicts their future trajectories, detects spatial–temporal conflicts, and resolves them using altitude-based separation — similar to concepts used in UTM systems and MATLAB UAV Toolbox.

The simulation includes:

Multi-drone trajectory prediction

Spatial + temporal conflict detection

Pre-flight conflict resolution

3D visualization with quadcopter-style drone models

Multiple reproducible test scenarios

project/
│
├── main.py                 # Simulation + visualization
├── conflict_handler.py     # Trajectory prediction & deconfliction logic
├── waypoints.py            # Test scenarios (with / without conflicts)
├── README.md
└── Reflection_and_Justification.md
How to Run

 Open waypoints.py

Select a scenario:
SCENARIO = 1   # 1–4
Run the simulation:
python main.py
Key Features

Strategic (pre-flight) deconfliction

Spatial + temporal conflict checks

Waypoint acceptance radius (real UAV behavior)

Scalable architecture for multi-agent systems

Deterministic and reproducible testing

