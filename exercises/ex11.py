def diagonal_printer(text):
    # Split the text into words
    words = text.split()

    # Iterate over each word
    for word in words:
        # Iterate over each character index in the word
        for i in range(len(word)):
            # Print leading spaces based on the current index
            print(" " * i, end="")

            # Print the character
            print(word[i])

# Test the diagonal_printer function
diagonal_printer("This is a test")
