def find_first_letter(number):
    # Dictionary mapping numbers to their corresponding letters
    number_to_letter = {
        1: 'o',
        2: 't',
        3: 't',
        4: 'f',
        5: 'f',
        6: 's',
        7: 's',
        8: 'e',
        9: 'n',
        0: 'z'
    }

    # Get the first digit of the number
    first_digit = int(str(number)[0])

    # Check if the first digit is in the dictionary
    if first_digit in number_to_letter:
        return number_to_letter[first_digit]
    else:
        return "Invalid input"

# Get user input
user_input = input("Enter a number: ")

try:
    # Convert user input to an integer
    user_number = int(user_input)

    # Call the function and print the result
    result = find_first_letter(user_number)
    print(f"The first letter of {user_number} is: {result}")

except ValueError:
    print("Invalid input. Please enter a valid number.")
