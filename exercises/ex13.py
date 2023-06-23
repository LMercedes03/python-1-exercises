def frame_it(wordlist):
    max_length = max(len(word) for word in wordlist)  # Find the maximum length of the words

    # Print the top border
    print('*' * (max_length + 4))

    # Print each word in the list with borders
    for word in wordlist:
        padding = ' ' * (max_length - len(word))  # Calculate the padding spaces
        print(f'* {word}{padding} *')

    # Print the bottom border
    print('*' * (max_length + 4))

# Test case
wordlist = ["Hello", "World", "in", "a", "frame"]
frame_it(wordlist)