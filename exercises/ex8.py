def c_to_f(celsius):
    # Convert Celsius to Fahrenheit
    fahrenheit = round((celsius * 9/5) + 32)
    # Return the conversion result using an f-string
    return f"{celsius} degrees Celsius is {fahrenheit} degrees Fahrenheit."

def f_to_c(fahrenheit):
    # Convert Fahrenheit to Celsius
    celsius = round((fahrenheit - 32) * 5/9)
    # Return the conversion result using an f-string
    return f"{fahrenheit} degrees Fahrenheit is {celsius} degrees Celsius."

# Example usage
print(f_to_c(22))
print(c_to_f(-6))