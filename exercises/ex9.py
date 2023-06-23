def vowel_counter(sentence):
    vowels = "aeiouAEIOU"  # Define the vowels
    count = 0  # Initialize the count variable

    # Iterate over each character in the sentence
    for char in sentence:
        # Check if the character is a vowel
        if char in vowels:
            # If the character is a vowel, increment the count by 1
            count += 1

    # Return the result
    return f"Number of vowels: {count}"


# Usage
sentence = "This is a test"
num_vowels = vowel_counter(sentence)
print(num_vowels)
