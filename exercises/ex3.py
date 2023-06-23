def add_numbers(numbers):
    # Initialize a variable to hold the sum of the numbers
    total = 0.0

    # Iterate over each number in the numbers array
    for num in numbers:
        # Convert the number to a float
        num_float = float(num)

        # Add the float number to the total sum
        total += num_float

    # Return the calculated total as a float value
    return total


array = [1.0, 1.1, "1"]
# result = add_numbers(array)
# print(result)