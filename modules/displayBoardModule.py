def displayBoard(missedLetters, correctLetters, secretWord):
    # displays the lettes typed and blanks left
    print('Missed letters:', end=" ")
    for letter in missedLetters:
        print(letter, end=" ")
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        # Replace blanks with correctly guessed letters.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        # Show the secret word with spaces in between each letter.
        print(letter, end=" ")
    print()
