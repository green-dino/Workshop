import io
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from fractpy.models import NewtonFractal, JuliaFractal

def generate_fractal(func_str, xmin, xmax, ymin, ymax, resolution, fractal_type, c=None):
    if fractal_type == "Newton":
        model = NewtonFractal(func_str)
    elif fractal_type == "Julia":
        model = JuliaFractal(c)
    
    # Create a new figure and axis
    fig, ax = plt.subplots(figsize=(6, 6))
    model.plot(xmin, xmax, ymin, ymax, resolution)
    
    # Convert the Matplotlib figure to PNG format
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format="png")
    plt.close(fig)
    
    return image_stream.getvalue()

def main():
    st.title("Fractal Generator")

    # Sidebar for user input
    with st.sidebar:
        st.subheader("Settings")
        fractal_type = st.radio("Fractal Type", ["Newton", "Julia"])
        func_str = st.text_input("Enter function (e.g., x**3 - 1)", "x**3 - 1", key="func_input")
        xmin = st.slider("X Min", -10.0, 10.0, -2.0)
        xmax = st.slider("X Max", -10.0, 10.0, 2.0)
        ymin = st.slider("Y Min", -10.0, 10.0, -2.0)
        ymax = st.slider("Y Max", -10.0, 10.0, 2.0)
        resolution = st.slider("Resolution", 100, 1000, 500)
        
        if fractal_type == "Julia":
            real_part = st.slider("Real Part (c)", -2.0, 2.0, 0.0, key="real_part")
            imag_part = st.slider("Imaginary Part (c)", -2.0, 2.0, 0.0, key="imag_part")
            c = complex(real_part, imag_part)
        else:
            c = None

    # Generate fractal based on user settings
    fractal = generate_fractal(func_str, xmin, xmax, ymin, ymax, (resolution, resolution), fractal_type, c)

    # Display the fractal
    st.image(fractal, caption="Generated Fractal", use_column_width=True)

if __name__ == "__main__":
    main()
