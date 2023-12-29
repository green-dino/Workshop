import streamlit as st
import pandas as pd
from datetime import datetime

# Sample data
projects_data = {
    'Project Name': ['Project A', 'Project B', 'Project C', 'Project D'],
    'Client': ['Client 1', 'Client 2', 'Client 1', 'Client 3'],
    'Due Date': ['2023-01-15', '2023-02-28', '2023-03-10', '2023-04-05']
}

projects_df = pd.DataFrame(projects_data)
projects_df['Due Date'] = pd.to_datetime(projects_df['Due Date'])

# Sidebar filters
client_options = sorted(projects_df['Client'].unique())
selected_client = st.sidebar.selectbox('Select Client:', client_options)

# Filter projects based on selected client
filtered_projects = projects_df[projects_df['Client'] == selected_client]

# Display filtered projects
st.header(f'Projects for {selected_client}')
st.table(filtered_projects)

# Due date filter
due_date_min = st.sidebar.date_input('Filter by Minimum Due Date', min(projects_df['Due Date']))
due_date_max = st.sidebar.date_input('Filter by Maximum Due Date', max(projects_df['Due Date']))

# Convert Python date to Pandas Timestamp
due_date_min = pd.to_datetime(due_date_min)
due_date_max = pd.to_datetime(due_date_max)

# Apply due date filter
due_date_filtered_projects = projects_df[
    (projects_df['Due Date'] >= due_date_min) & (projects_df['Due Date'] <= due_date_max)
]

# Display filtered projects based on due date
st.header('Projects filtered by Due Date')
st.table(due_date_filtered_projects)
