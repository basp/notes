import matplotlib.pyplot as plt
from matplotlib import patches
import plotutils as pu
import math

def aperture_examples():
    fig, axes = plt.subplots(1, 3, figsize=(6, 2))

    pu.setup_axes(axes[0], xlim=[-1,1], ylim=[-1,1])
    pu.setup_axes(axes[1], xlim=[-1,1], ylim=[-1,1])
    pu.setup_axes(axes[2], xlim=[-1,1], ylim=[-1,1])

    a11 = patches.Wedge((-0.4, 0.1), 0.24, 0, 180)
    a12 = patches.Wedge((0.4, -0.1), 0.24, 180, 0)

    a21 = patches.Wedge((0.1, -0.4), 0.24, 270, 90)
    a22 = patches.Wedge((-0.1, 0.4), 0.24, 90, 270)

    a31 = patches.Wedge((-0.4, 0.1), 0.18, 0, 180)
    a32 = patches.Wedge((0.4, -0.1), 0.18, 180, 0)
    a33 = patches.Wedge((0.1, -0.4), 0.18, 270, 90)
    a34 = patches.Wedge((-0.1, 0.4), 0.18, 90, 270)

    axes[0].set_title("Moon X")
    axes[0].add_patch(a11)
    axes[0].add_patch(a12)
    
    axes[1].set_title("Moon Y")
    axes[1].add_patch(a21)
    axes[1].add_patch(a22)

    axes[2].set_title("Moon XY")
    axes[2].add_patch(a31)
    axes[2].add_patch(a32)
    axes[2].add_patch(a33)
    axes[2].add_patch(a34)

def aperture_reflection_examples():
    fig, axes = plt.subplots(1, 4, figsize=(8, 2))

    pu.setup_axes(axes[0], xlim=[-1,1], ylim=[-1,1])
    pu.setup_axes(axes[1], xlim=[-1,1], ylim=[-1,1])
    pu.setup_axes(axes[2], xlim=[-1,1], ylim=[-1,1])
    pu.setup_axes(axes[3], xlim=[-1,1], ylim=[-1,1])

    a1i = patches.Wedge((-0.4, 0.1), 0.24, 0, 180, color="blue")
    a1o = patches.Wedge((0.4, 0.1), 0.24, 0, 180, color="red")

    a2i = patches.Wedge((0.1, -0.4), 0.24, 270, 90, color="blue")
    a2o = patches.Wedge((0.1, 0.4), 0.24, 270, 90, color="red")

    a31i = patches.Wedge((-0.4, 0.1), 0.18, 0, 180, color="blue")
    a32i = patches.Wedge((-0.1, 0.4), 0.18, 90, 270, color="blue")
    a31o = patches.Wedge((0.4, 0.1), 0.18, 0, 180, color="red")
    a32o = patches.Wedge((0.1, 0.4), 0.18, 270, 90, color="red")

    a41i = patches.Wedge((0.1, -0.4), 0.18, 270, 90, color="blue")
    a42i = patches.Wedge((0.4, -0.1), 0.18, 180, 0, color="blue")
    a41o = patches.Wedge((0.4, 0.1), 0.18, 0, 180, color="red")
    a42o = patches.Wedge((0.1, 0.4), 0.18, 270, 90, color="red")

    axes[0].set_title("Moon X")
    axes[0].add_patch(a1i)
    axes[0].add_patch(a1o)

    axes[1].set_title("Moon Y")
    axes[1].add_patch(a2i)
    axes[1].add_patch(a2o)

    axes[2].set_title("Moon XY")
    axes[2].add_patch(a31i)
    axes[2].add_patch(a32i)
    axes[2].add_patch(a31o)
    axes[2].add_patch(a32o)

    axes[3].set_title("Moon XY")
    axes[3].add_patch(a41i)
    axes[3].add_patch(a42i)    
    axes[3].add_patch(a41o)
    axes[3].add_patch(a42o) 