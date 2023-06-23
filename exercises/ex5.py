def replace_period(sentence, punctuation):
    # Split the sentence into a list of words
    words = sentence.split()

    # Iterate over each word in the list
    for i in range(len(words)):
        # Check if the word ends with a period
        if words[i].endswith('.'):
            # Replace the period with the given punctuation character
            words[i] = words[i].replace('.', punctuation)

    # Join the words back into a sentence using spaces
    modified_sentence = ' '.join(words)

    return modified_sentence


# Example usage
sentence = "Test. This is a test. Testing."
sentence2 = replace_period(sentence, "!")
print(sentence2)