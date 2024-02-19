import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to create a visualization with dynamic variables
def create_visualization(amplitude, frequency):
    x = np.linspace(0, 2 * np.pi, 1000)
    y = amplitude * np.sin(frequency * x)

    # Create and plot the figure
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(f"Sine Wave: Amplitude={amplitude}, Frequency={frequency}")

    # Show the plot
    st.pyplot(fig)

# Main Streamlit app
def main():
    st.title("Dynamic Visual Effects")

    # Sidebar for user input
    st.sidebar.header("Variable Settings")

    # User input for amplitude and frequency
    amplitude = st.sidebar.slider("Amplitude", 1.0, 10.0, 5.0)
    frequency = st.sidebar.slider("Frequency", 1.0, 10.0, 2.0)

    # Create the visualization with dynamic variables
    create_visualization(amplitude, frequency)

# Run the Streamlit app
if __name__ == "__main__":
    main()
