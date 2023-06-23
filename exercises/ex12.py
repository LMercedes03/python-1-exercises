def word_histogram(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Create an empty dictionary to store word frequencies
    histogram = {}

    # Iterate over each word
    for word in words:
        # If the word is already in the dictionary, increment the count by 1
        if word in histogram:
            histogram[word] += 1
        # Otherwise, add the word to the dictionary with an initial count of 1
        else:
            histogram[word] = 1

    # iterate over each key-value pair in the dictionary and print the word along with its count
    for word, count in histogram.items():
        print(f"{word}: {count}")


# Usage
word_histogram("three three three two two one")
