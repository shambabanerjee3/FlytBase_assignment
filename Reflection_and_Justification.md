1. Design Philosophy

The system was designed to mimic real-world UAV Traffic Management (UTM) principles while remaining lightweight and understandable.
Rather than relying on ROS or heavy physics engines, the focus was placed on:

Strategic decision-making

Predictive trajectory analysis

Clear separation of responsibilities

Deterministic simulation behavior

This approach allows rapid prototyping and clear reasoning — critical under limited development time.


2. Architectural Choices
Modular Architecture

The system is divided into three logical layers:

Waypoint & Scenario Definition (waypoints.py)

Defines missions independently of logic

Enables reproducible test cases

Supports multiple scenarios with identical drone IDs

Conflict Handling (conflict_handler.py)

Trajectory prediction

Conflict detection

Resolution strategies

Acts as a UTM-style decision engine

Simulation & Visualization (main.py)

Executes resolved missions

Visualizes drone motion

Independent of conflict logic

This separation improves maintainability, extensibility, and testing.


3. Spatial and Temporal Conflict Detection
Spatial Checks

For each predicted position:

Horizontal separation is computed using Euclidean distance in the XY plane.

Vertical separation is computed using absolute altitude difference.


Temporal Checks

Each predicted trajectory is time-stamped using a fixed simulation time step.


4. Conflict Resolution Strategy
Strategic (Pre-Flight) Resolution

All conflicts are resolved before flight execution, ensuring:

No reactive oscillations

No mid-air deadlocks

Predictable behavior

Resolution Method

Primary drone remains unchanged

Secondary drones receive a temporary altitude offset

Original horizontal paths are preserved

This mimics MATLAB UAV Toolbox strategic deconfliction, where vertical separation is preferred over lateral deviation.

5. Waypoint Acceptance Logic

A waypoint acceptance radius is used instead of exact coordinate matching.

This prevents:

Floating-point deadlocks

Oscillatory behavior near waypoints

Unrealistic stop-and-hover artifacts

This reflects real autopilot logic used in PX4 / ArduPilot systems.
