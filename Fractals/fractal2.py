import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Function to generate a fractal image with color
def generate_colored_fractal(width, height, max_iter=100, color_palette='viridis'):
    # Create a blank image
    img = np.zeros((height, width, 3), dtype=np.uint8)

    # Define the fractal properties
    x_min, x_max = -2, 2
    y_min, y_max = -2, 2

    # Get the color map
    cmap = plt.get_cmap(color_palette)

    # Generate the fractal
    for x in range(width):
        for y in range(height):
            zx, zy = x * (x_max - x_min) / (width - 1) + x_min, y * (y_max - y_min) / (height - 1) + y_min
            c = zx + zy * 1j
            z = c
            for i in range(max_iter):
                if abs(z) > 2.0:
                    break 
                z = z * z + c
            # Map the iteration count to a color based on the chosen color palette
            color = cmap(i / max_iter)[:3]
            img[y, x, :] = (np.array(color) * 255).astype(np.uint8)

    return img

# Streamlit UI
st.title("Colored Fractal Drawing Application")

# User inputs
width = st.sidebar.slider("Image Width", 100, 1000, 500)
height = st.sidebar.slider("Image Height", 100, 1000, 500)
max_iter = st.sidebar.slider("Max Iterations", 50, 500, 100)
color_palette = st.sidebar.selectbox("Color Palette", plt.colormaps())

# Generate fractal image with color
colored_fractal_img = generate_colored_fractal(width, height, max_iter, color_palette)

# Display the fractal image with color
st.image(Image.fromarray(colored_fractal_img), caption="Generated Colored Fractal", use_column_width=True)

# Optionally, you can save the image
if st.button("Save Image"):
    im = Image.fromarray(colored_fractal_img)
    im.save("colored_fractal_image.png")
    st.success("Image saved successfully!")
