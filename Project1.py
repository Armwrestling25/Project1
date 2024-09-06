# Define ANSI escape codes for text color
RED = '\033[91m'  # Red color for error messages
RESET = '\033[0m'  # Reset color to default

# Prompt user to input their name
name = input("Write Your Name??\n")

# Validate that the name contains only alphabetic characters
if name.isalpha():
    try:
        # Attempt to convert the input for age to an integer
        age = int(input("Write Your Age\n"))
        if 0 < age < 120:
            # Print a greeting message with the user's name and age
            print(f"Hello {name}, {age}")
        else:
            # Print an error message if the age is out of the valid range
            print(f"{RED}Error {age} put your real age {RESET}")
    except ValueError:
        # Print an error message if the age input is not a valid integer
        print(f"{RED}Error - Print only Numbers-{RESET}")
else:
    # Print an error message if the name contains non-alphabetic characters
    print(f"{RED}Error - Name should contain only alphabetic characters.{RESET}")

