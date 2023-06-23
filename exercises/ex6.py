def slice_it(strings):
    sliced_words = []  # Initialize an empty list to store the sliced words

    # Iterate over each word in the array
    for word in strings:
        sliced_word = word[:2]  # Extract the first two letters of the word using string slicing
        sliced_words.append(sliced_word)  # Add the sliced word to the list

    return "".join(sliced_words)  # Join the sliced words into a single string


# Usage
array = ["this", "is", "another", "test"]
result = slice_it(array)
print(result)