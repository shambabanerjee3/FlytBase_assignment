# main.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from waypoints import primary_waypoints, secondary_drones
from conflict_handler import main_conflict_handler

WAYPOINT_RADIUS = 0.4
ARM_LEN = 0.6
dt = 0.1


class Drone3D:
    def __init__(self, start, waypoints, speed, color):
        self.pos = np.array(start, float)
        self.wps = [np.array(w, float) for w in waypoints]
        self.speed = speed
        self.idx = 0
        self.color = color

    def update(self):
        if self.idx >= len(self.wps):
            return self.pos

        tgt = self.wps[self.idx]
        d = tgt - self.pos
        dist = np.linalg.norm(d)

        if dist < WAYPOINT_RADIUS:
            self.pos = tgt.copy()
            self.idx += 1
            return self.pos

        step = self.speed * dt
        self.pos += d / dist * min(step, dist)
        return self.pos


# ------------------ Deconfliction ------------------
primary_start = (2, 2, 1)
primary_speed = 1.5

primary_wp, resolved_secs = main_conflict_handler(
    primary_start, primary_waypoints, primary_speed, secondary_drones
)

# ------------------ Init Drones ------------------
primary = Drone3D(primary_start, primary_wp, primary_speed, "blue")

colors = ["green", "red", "purple", "orange"]
secondaries = [
    Drone3D(d["start"], d["waypoints"], d["speed"], colors[i % 4])
    for i, d in enumerate(resolved_secs)
]

# ------------------ Plot ------------------
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")

ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.set_zlim(0, 10)

ax.set_title("Multi-Drone Strategic Deconfliction (3D)")
ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")
ax.set_zlabel("Z (m)")


def create_drone(color):
    arm1, = ax.plot([], [], [], color=color, lw=2)
    arm2, = ax.plot([], [], [], color=color, lw=2)

    rotors = [
        ax.plot([], [], [], marker='o', color=color, markersize=5)[0]
        for _ in range(4)
    ]
    return arm1, arm2, rotors


def draw(drone, elems):
    arm1, arm2, rot = elems
    x, y, z = drone.pos

    arm1.set_data([x-ARM_LEN, x+ARM_LEN], [y, y])
    arm1.set_3d_properties([z, z])

    arm2.set_data([x, x], [y-ARM_LEN, y+ARM_LEN])
    arm2.set_3d_properties([z, z])

    offs = [(ARM_LEN,0),(-ARM_LEN,0),(0,ARM_LEN),(0,-ARM_LEN)]
    for r,(dx,dy) in zip(rot,offs):
        r.set_data(x+dx, y+dy)
        r.set_3d_properties(z)


p_elems = create_drone("blue")
s_elems = [create_drone(d.color) for d in secondaries]


def update(frame):
    primary.update()
    draw(primary, p_elems)

    for d,e in zip(secondaries, s_elems):
        d.update()
        draw(d, e)

    return []


ani = FuncAnimation(fig, update, interval=80)
plt.show()
