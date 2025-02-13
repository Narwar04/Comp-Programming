def calculate_value(user_input):
    # Check for sequential vowels
    vowels = 'AEIOUL'
    for i in range(len(user_input) - 1):
        if user_input[i] in vowels and user_input[i + 1] in vowels:
            return "Invalid: Sequential vowels found"

    # Check for sequential consonants
    for i in range(len(user_input) - 1):
        if user_input[i].isalpha() and user_input[i + 1].isalpha():
            if user_input[i] not in vowels and user_input[i + 1] not in vowels:
                return "Invalid: Sequential consonants found"

    # Check for at least one letter 'L'
    # if 'L' not in user_input:
    #     return "Invalid: No 'L' found"

    # Count the underscores in the input
    underscore_count = user_input.count('_')
    # Multiply by the number of vowels (5)
    result = underscore_count * 6
    return result

# Get user input
user_input = input()
# Calculate and print the result
print(calculate_value(user_input))

