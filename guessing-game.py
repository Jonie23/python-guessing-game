import random
from modules.getGuessModule import getGuess
from modules.displayBoardModule import displayBoard

words = 'ant cow bat hen pig cat dog'.split()

# we could add more words

def getRandomWord(wordList):
    # This function returns a random string from the list of strings above.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]










def playAgain():
    # This function returns True if the player wantsto play again, otherwise, it returns False.
    print('Do you want to play again? (Yes or No)')
    return input().lower().startswith('y')


print('H A N G M A N')
missedLetters = ' '
correctLetters = ' '
secretWord = getRandomWord(words)
gameIsDone = False





while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! the secret word is "' +
                  secretWord + '"! You have won!')
            gameIsDone = True

    else:
        missedLetters = missedLetters + guess

        # Check if player has guesssed too many times and lost.
        if len(missedLetters) == 6:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' +
                  str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was ' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
