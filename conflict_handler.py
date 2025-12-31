# conflict_handler.py
import numpy as np

SAFETY_RADIUS = 2.0      # horizontal meters
ALT_SEP = 1.5            # vertical meters
TIME_STEP = 0.2          # seconds
LOOKAHEAD = 25.0         # seconds


def predict_trajectory(start, waypoints, speed):
    traj = []
    pos = np.array(start, dtype=float)
    t = 0.0

    for wp in waypoints:
        wp = np.array(wp, dtype=float)
        d = wp - pos
        dist = np.linalg.norm(d)
        if dist < 1e-3:
            continue

        vel = d / dist * speed
        steps = int((dist / speed) / TIME_STEP)

        for _ in range(steps):
            pos += vel * TIME_STEP
            t += TIME_STEP
            traj.append((round(t, 2), pos.copy()))

        pos = wp.copy()

    return traj


def detect_conflict(traj_a, traj_b):
    for ta, pa in traj_a:
        for tb, pb in traj_b:
            if abs(ta - tb) > TIME_STEP:
                continue

            hdist = np.linalg.norm(pa[:2] - pb[:2])
            vdist = abs(pa[2] - pb[2])

            if hdist < SAFETY_RADIUS and vdist < ALT_SEP:
                return {
                    "time": ta,
                    "location": pa,
                    "h_dist": round(hdist, 2),
                    "v_dist": round(vdist, 2)
                }
    return None


def resolve_secondary_altitude(secondary, offset):
    new_wp = []
    for i, wp in enumerate(secondary["waypoints"]):
        if i == 0:
            new_wp.append((wp[0], wp[1], wp[2] + offset))
        else:
            new_wp.append(wp)
    secondary["waypoints"] = new_wp
    return secondary


def main_conflict_handler(primary_start, primary_wp, primary_speed, secondaries):
    primary_traj = predict_trajectory(primary_start, primary_wp, primary_speed)

    resolved = []
    altitude_offset = ALT_SEP

    for sec in secondaries:
        sec_traj = predict_trajectory(sec["start"], sec["waypoints"], sec["speed"])
        conflict = detect_conflict(primary_traj, sec_traj)

        if conflict:
            print(f"[CONFLICT] Primary vs Drone-{sec['id']} at t={conflict['time']}s")
            sec = resolve_secondary_altitude(sec, altitude_offset)
            altitude_offset += ALT_SEP

        resolved.append(sec)

    return primary_wp, resolved
