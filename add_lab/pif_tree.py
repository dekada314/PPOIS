import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

plt.figure(figsize=(8, 8))
ax = plt.gca()
ax.set_aspect("equal")
ax.axis("off")


def square_corners(z, s, a):
    v = s * complex(math.cos(a), math.sin(a))
    u = s * complex(-math.sin(a), math.cos(a))
    return [z, z + v, z + v + u, z + u]


def draw_square(z, s, a, color="C0", lw=1):
    corners = square_corners(z, s, a)
    pts = [(c.real, c.imag) for c in corners]
    poly = Polygon(pts, closed=True, facecolor=color, edgecolor="k", linewidth=lw)
    ax.add_patch(poly)


def pythagoras_tree(z, s, a, depth, max_depth, theta):
    colors = ["#b2225a", "#c33b7e", "#59a6d9", "#66c55b"]
    color = colors[min(depth, len(colors) - 1)]

    draw_square(z, s, a, color=color)

    if depth >= max_depth:
        return

    v = s * complex(math.cos(a), math.sin(a))
    u = s * complex(-math.sin(a), math.cos(a))
    top_left = z + u

    sl = s * math.cos(theta)
    sr = s * math.sin(theta)

    zl = top_left
    al = a + theta

    zr = top_left + sl * complex(math.cos(al), math.sin(al))
    ar = a - (math.pi / 2 - theta)

    pythagoras_tree(zl, sl, al, depth + 1, max_depth, theta)
    pythagoras_tree(zr, sr, ar, depth + 1, max_depth, theta)

max_depth = 5
theta = math.pi / 4
z0 = complex(-0.5, 0.0)
s0 = 1.0
a0 = 0.0

pythagoras_tree(z0, s0, a0, 0, max_depth, theta)

ax.relim()
ax.autoscale_view()

plt.show()
