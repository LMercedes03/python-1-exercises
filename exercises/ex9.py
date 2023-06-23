def vowel_counter(sentence):
    vowels = "aeiouAEIOU"  # Define the vowels
    count = 0  # Initialize the count variable

    for char in sentence:
        if char in vowels:
            count += 1

    return f"Number of vowels: {count}"


# Usage
sentence = "This is a test"
num_vowels = vowel_counter(sentence)
print(num_vowels)
