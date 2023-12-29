import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Load the CSV file
file_path = "Table data.csv"
df = pd.read_csv(file_path)

# Title of the app
st.title("YouTube Data Visualization App")

# Display the loaded data
st.write("## Raw Data")
st.write(df)

# Sidebar filters
st.sidebar.header("Filters")

# Add filter for selecting the chart option
chart_option = st.sidebar.selectbox("Select Chart Option", df.columns[1:])

# Visualization section

# Example: Bar chart for selected option
st.header(f"{chart_option} Distribution")
bar_chart = st.bar_chart(df[chart_option])

# Function to update the bar chart based on user-selected option
def update_bar_chart(option):
    plt.clf()  # Clear previous plot

    # Plot the bar chart
    plt.bar(df['Video title'], df[option])
    plt.xlabel('Video Title')
    plt.ylabel(option)
    plt.title(f'Bar Chart - {option}')
    plt.xticks(rotation=45, ha='right')
    plt.gca().xaxis.set_major_locator(MaxNLocator(prune='lower'))  # Adjust x-axis labels for better visibility

    # Show the updated plot
    st.pyplot()

# Add interactivity to update the bar chart
update_button = st.sidebar.button("Update Bar Chart")
if update_button:
    update_bar_chart(chart_option)

# Example: Line chart for Watch time
st.header("Watch Time Over Time")
watch_time_chart = st.line_chart(df['Watch time (hours)'])

# Example: Scatter plot for Impressions vs CTR
st.header("Impressions vs CTR")
scatter_chart = st.scatter_chart(df[['Impressions', 'Impressions click-through rate (%)']])

# More visualizations can be added based on your needs

# Add interactivity (if needed)
# Example: Display detailed information for a selected video
selected_video = st.selectbox("Select a video", df['Video title'])
video_details = df[df['Video title'] == selected_video]
st.write("## Selected Video Details")
st.write(video_details)

# Run the app
# Run the app
if __name__ == "__main__":
    st.sidebar.write("Click below to run the app.")
    st.sidebar.button("Run App", on_click=st.balloons)
