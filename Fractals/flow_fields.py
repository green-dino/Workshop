import streamlit as st
import turtle

# Function to generate fractals using turtle graphics
def generate_fractal(axiom, rules, iterations, angle):
    result = axiom
    for _ in range(iterations):
        result = "".join(rules.get(char, char) for char in result)
    
    return result

# Function to draw the fractal using turtle graphics
def draw_fractal(axiom, rules, iterations, angle):
    st.title("Fractal Explorer")
    st.sidebar.header("Settings")

    # Sidebar input for iterations
    iterations = st.sidebar.slider("Iterations", min_value=1, max_value=10, value=iterations)

    # Sidebar input for angle
    angle = st.sidebar.slider("Angle", min_value=1, max_value=180, value=angle)

    st.sidebar.subheader("Select Fractal")
    fractal_choice = st.sidebar.radio("", ["Koch Snowflake", "Quadratic Koch Island"])

    if fractal_choice == "Koch Snowflake":
        axiom = "F--F--F"
        rules = {"F": "F+F--F+F"}
    elif fractal_choice == "Quadratic Koch Island":
        axiom = "F+F+F+F"
        rules = {"F": "F-F+F+FFF-F-F+F"}

    st.sidebar.text("")

    # Generate and display the fractal
    fractal_result = generate_fractal(axiom, rules, iterations, angle)
    st.write(f"Generated Fractal: {fractal_result}")

    # Turtle graphics
    turtle.reset()
    turtle.speed(2)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-200, -200)
    turtle.pendown()

    for char in fractal_result:
        if char == "F":
            turtle.forward(5)
        elif char == "+":
            turtle.left(angle)
        elif char == "-":
            turtle.right(angle)

    turtle.done()

# Run the app
if __name__ == "__main__":
    axiom = "F--F--F"  # Set initial values here
    rules = {"F": "F+F--F+F"}
    iterations = 4
    angle = 60

    draw_fractal(axiom, rules, iterations, angle)
