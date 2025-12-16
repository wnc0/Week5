import streamlit as st
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

# ------------------------------
# Color palettes
# ------------------------------
PALETTES = {
    "Peach Sky": [(0.996, 0.867, 0.839), (0.992, 0.745, 0.682), (0.592, 0.741, 0.867), (0.8, 0.88, 0.97)],
    "Mint Cloud": [(0.85, 0.96, 0.91), (0.67, 0.82, 0.9), (0.98, 0.89, 0.87), (0.94, 0.96, 0.98)],
    "Lavender Mist": [(0.89, 0.86, 0.98), (0.82, 0.77, 0.93), (0.98, 0.92, 0.95), (0.94, 0.98, 0.99)]
}

# ------------------------------
# Blob generator
# ------------------------------
def blob(center=(0.5, 0.5), r=0.3, wobble=0.15, points=100):
    angles = np.linspace(0, 2*np.pi, points)
    radius = r * (1 + wobble * np.sin(angles * random.uniform(2, 5)))
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return x, y

# ------------------------------
# Poster generator
# ------------------------------
def generate_poster(palette_name, n_shapes, alpha_val):
    fig, ax = plt.subplots(figsize=(6, 8))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_facecolor((0.95, 0.95, 0.97))

    palette = PALETTES[palette_name].copy()
    random.shuffle(palette)

    patches, colors = [], []
    for _ in range(n_shapes):
        cx, cy = random.uniform(0.2, 0.8), random.uniform(0.2, 0.8)
        rr = random.uniform(0.2, 0.45)
        wobble_val = random.uniform(0.05, 0.25)
        x, y = blob((cx, cy), rr, wobble_val)
        patches.append(Polygon(np.column_stack((x, y)), closed=True))
        colors.append(random.choice(palette))

    collection = PatchCollection(patches, facecolor=colors, alpha=alpha_val, edgecolor="none")
    ax.add_collection(collection)

    ax.text(0.5, 0.82, "Soft Geometry", fontsize=28, weight="bold",
            color=random.choice(palette), ha="center")
    ax.text(0.5, 0.77, "Generative Poster", fontsize=12,
            color=(0.3, 0.3, 0.3), ha="center")
    ax.text(0.9, 0.06, f"Edition #{random.randint(1000, 9999)}",
            fontsize=8, color=(0.4, 0.4, 0.4), ha="right")

    return fig

# ------------------------------
# Streamlit UI
# ------------------------------
st.title("Interactive Generative Poster")

palette_name = st.selectbox("Palette", list(PALETTES.keys()))
n_shapes = st.slider("Number of Shapes", 3, 12, 6)
alpha_val = st.slider("Transparency", 0.2, 0.9, 0.6)

if st.button("Generate Poster"):
    fig = generate_poster(palette_name, n_shapes, alpha_val)
    st.pyplot(fig)
