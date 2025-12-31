"""
Waypoints Test Scenarios for Strategic Deconfliction
All scenarios:
- Same drone IDs (1–4)
- Each drone has ≥ 3 waypoints
- Waypoints do NOT repeat start position
"""

# ================================
# SCENARIO SELECT
# ================================
SCENARIO = 4   # 1 / 2 / 3 / 4


# ================================
# PRIMARY DRONE
# ================================
primary_start = (2, 2, 1)
primary_speed = 1.5

primary_waypoints = [
    (4, 4, 3),
    (8, 8, 4),
    (12, 12, 5),
    (16, 16, 6),
]


# ================================
# SCENARIO 1: NO CONFLICT
# ================================
secondary_case_1 = [
    {
        "id": 1,
        "start": (2, 18, 2),
        "speed": 1.2,
        "waypoints": [(4,16,3), (6,18,3), (8,16,3)]
    },
    {
        "id": 2,
        "start": (18, 2, 2),
        "speed": 1.3,
        "waypoints": [(16,4,3), (18,6,3), (16,8,3)]
    },
    {
        "id": 3,
        "start": (18, 18, 4),
        "speed": 1.1,
        "waypoints": [(16,16,4), (14,18,4), (12,16,4)]
    },
    {
        "id": 4,
        "start": (5, 2, 6),
        "speed": 1.0,
        "waypoints": [(7,4,6), (9,6,6), (11,8,6)]
    }
]


# ================================
# SCENARIO 2: SINGLE CONFLICT
# (Drone-2 crosses primary path)
# ================================
secondary_case_2 = [
    {
        "id": 1,
        "start": (2, 18, 2),
        "speed": 1.2,
        "waypoints": [(4,16,3), (6,14,3), (8,12,3)]
    },
    {
        "id": 2,  # ⚠ conflict
        "start": (16, 4, 5),
        "speed": 1.3,
        "waypoints": [(12,8,5), (8,12,5), (4,16,5)]
    },
    {
        "id": 3,
        "start": (18, 18, 4),
        "speed": 1.1,
        "waypoints": [(16,18,4), (14,16,4), (12,14,4)]
    },
    {
        "id": 4,
        "start": (5, 2, 6),
        "speed": 1.0,
        "waypoints": [(7,4,6), (9,6,6), (11,8,6)]
    }
]


# ================================
# SCENARIO 3: MULTIPLE CONFLICTS
# (Three drones intersect primary)
# ================================
secondary_case_3 = [
    {
        "id": 1,
        "start": (14, 14, 5),
        "speed": 1.2,
        "waypoints": [(10,10,5), (8,8,5), (6,6,5)]
    },
    {
        "id": 2,
        "start": (12, 6, 4),
        "speed": 1.1,
        "waypoints": [(10,8,4), (8,10,4), (6,12,4)]
    },
    {
        "id": 3,
        "start": (10, 10, 5),
        "speed": 1.3,
        "waypoints": [(12,12,5), (14,14,5), (16,16,5)]
    },
    {
        "id": 4,
        "start": (18, 2, 6),
        "speed": 1.0,
        "waypoints": [(16,4,6), (14,6,6), (12,8,6)]
    }
]


# ================================
# SCENARIO 4: NEAR-MISS (EDGE CASE)
# (Above vertical separation)
# ================================
secondary_case_4 = [
    {
        "id": 1,
        "start": (4, 6, 6.5),
        "speed": 1.2,
        "waypoints": [(8,6,6.5), (12,6,6.5), (16,6,6.5)]
    },
    {
        "id": 2,
        "start": (6, 4, 6.5),
        "speed": 1.1,
        "waypoints": [(6,8,6.5), (6,12,6.5), (6,16,6.5)]
    },
    {
        "id": 3,
        "start": (18, 18, 3),
        "speed": 1.0,
        "waypoints": [(16,16,3), (14,14,3), (12,12,3)]
    },
    {
        "id": 4,
        "start": (18, 2, 6),
        "speed": 1.0,
        "waypoints": [(16,4,6), (14,6,6), (12,8,6)]
    }
]


# ================================
# ACTIVE SCENARIO SELECTION
# ================================
if SCENARIO == 1:
    secondary_drones = secondary_case_1
elif SCENARIO == 2:
    secondary_drones = secondary_case_2
elif SCENARIO == 3:
    secondary_drones = secondary_case_3
elif SCENARIO == 4:
    secondary_drones = secondary_case_4
else:
    raise ValueError("Invalid SCENARIO")
