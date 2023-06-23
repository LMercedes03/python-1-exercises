def count_words(sentence):
    word_count = 0  # Initialize word count at 0
    word_start = False  # Track if a word has started

    # Iterate over each character in the sentence
    for char in sentence:
        # If the character is not a space and a word has not started yet,then it's a new word
        if char != ' ' and not word_start:  # Start of a new word
            word_count += 1  # Increment the word count
            word_start = True  # Set the word_start to True

        elif char == ' ':
            # If the character is a space set word_start to false
            word_start = False

    return word_count  # Return the word count

    # words = sentence.split()  # Split the input into words
    # return len(words)


sentence = input("Enter sentence: ")
num_words = count_words(sentence)
print(num_words)
