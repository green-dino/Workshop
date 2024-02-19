import streamlit as st

def main():
    st.title("Vehicle and Motor Selection App")

    # Define vehicle options
    vehicle_options = ["Ford", "Chevy", "Dodge"]

    # Define motor options
    motor_options = ["V6 4.2", "V8 5.0", "I4 2.0"]

    # Define use of Application
    application = ["Racing ", "Dragstrip", "Cruising"]

    # User selection widgets
    selected_vehicle = st.selectbox("Choose a vehicle:", vehicle_options)
    selected_motor = st.selectbox("Choose a motor type:", motor_options)
    selected_application = st.selectbox("Choose your application", application)
    

    # Display the selected choices
    st.write(f"You selected a {selected_vehicle} with a {selected_motor} motor for {selected_application}")

if __name__ == "__main__":
    main()
