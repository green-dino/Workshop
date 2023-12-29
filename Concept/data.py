import streamlit as st
import time
import numpy as np
import pandas as pd 
import altair as alt

# Title and Headers
def display_headers():
    st.title("Learning Data with Streamlit")
    st.header("This is a Markdown Header")
    st.markdown("This is a Markdown Body")
    st.subheader("This is a Subheader")
    st.caption("Streamlit Supports LaTeX")

# Sidebar
def display_sidebar():
    with st.sidebar:
        st.subheader("Sidebar Options")
        name = st.text_input('Enter your name')
        picked_number = st.number_input('Pick a number', 0, 10)
        selected_candy = st.radio('Pick your candy', ['Chocolate', 'Gummies', 'No Candy'])
        selected_vegetable = st.selectbox('Pick your vegetables', ['Carrots', 'Potatoes'])
        selected_planets = st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])
        satisfaction_level = st.select_slider('Pick your satisfaction', ['Bad', 'Good', 'Excellent'])
        selected_number = st.slider('Pick a number', 0, 50)

        # Text Input
        if name:
            st.write(f'Hello, {name}')

        # Checkboxes
        option_yes = st.checkbox('Yes')
        option_no = st.checkbox('No')

        # Button
        if st.button('Click me!'):
            st.success('Button Clicked!')

        # Radio Button
        st.write(f'Selected Candy: {selected_candy}')

        # Select Box
        st.write(f'Selected Vegetable: {selected_vegetable}')

        # Multi-Select
        st.write(f'Selected Planets: {selected_planets}')

        # Select Slider
        st.write(f'Satisfaction Level: {satisfaction_level}')

        # Slider
        st.write(f'Selected Number: {selected_number}')

# New Features
def display_new_features():
    email_address = st.text_input('Email address')
    traveling_date = st.date_input('Travelling date')
    school_time = st.time_input('School time')
    description = st.text_area('Description')
    uploaded_file = st.file_uploader('Upload a photo')
    favorite_color = st.color_picker('Choose your favorite color')

    # Displaying Information from New Features
    st.write(f'Email Address: {email_address}')
    st.write(f'Travelling Date: {traveling_date}')
    st.write(f'School Time: {school_time}')
    st.write(f'Write about the way you travel to school: {description}')
    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Photo', use_column_width=True)
    st.write(f'Favorite Color: {favorite_color}')

# Success Messages
def display_success_messages():
    st.markdown('Success messages')
    st.success("You did it !")
    st.error("Error")
    st.warning("Warning")
    st.info("It's easy to build a streamlit app")
    st.exception(RuntimeError("RuntimeError exception"))

# Data Charts
def display_data_charts():
    st.markdown('Plot chart')

    # Optimized DataFrame
    df = pd.DataFrame(np.random.randn(500, 3), columns=['x', 'y', 'z'])

    # Altair Chart
    c = alt.Chart(df).mark_circle().encode(
        x='x',
        y='y',
        size='z',
        color='z',
        tooltip=['x', 'y', 'z']
    )

    # Streamlit Altair Chart
    st.altair_chart(c, use_container_width=True)

    # Map Chart
    map_df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [32.25, -110.911], columns=['lat', 'lon'])
    st.map(map_df)

def main():
    display_headers()
    display_sidebar()
    display_new_features()
    display_success_messages()
    display_data_charts()

if __name__ == "__main__":
    main()
