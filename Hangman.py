'''
Description:
        You must create a Hangman game that allows the user to play and guess a secret word.  
        See the assignment description for details.
    
@author: Bri Butler    bb274
'''

import random


def handleUserInputDifficulty():
    '''
    This function asks the user if they would like to play the game in (h)ard or (e)asy mode, then returns the 
    corresponding number of misses allowed for the game. 
    '''
    print("How many misses do you want? Hard has 8 and Easy has 12")
    easy = 8
    hard = 12
    useranswer = input("(h)ard or (e)asy> ")
    if useranswer == "h":
        difficulty = 8
    else:
        difficulty = 12
    return difficulty
    pass 




def getWord(words, length):
    '''
    Selects the secret word that the user must guess. 
    This is done by randomly selecting a word from words that is of length length.
    '''
    length_words = []
    for word in words:
        if len(word) == length:
            length_words.append(word)

    gameword = random.choice(length_words)
    return gameword
    pass 




def createDisplayString(lettersGuessed, misses, hangmanWord):
    '''
    Creates the string that will be displayed to the user, using the information in the parameters.
    '''
    lettersGuessed = " ".join(sorted(lettersGuessed))
    hangmanWord = " ".join(hangmanWord)
    phrase = "letters you've guessed:  " + lettersGuessed + "\n" + "misses remaining = " + str(misses) + "\n" + hangmanWord 
    return phrase 




def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed and checks if it is a repeated letter.
    '''
    print(displayString)

    letterguessed = input("letter> ")

    while letterguessed in lettersGuessed:
        print("You already guessed that!")
        letterguessed = input("letter> ")
    if letterguessed not in lettersGuessed:
            lettersGuessed.append(letterguessed)
            #print(lettersGuessed)
    return letterguessed




def updateHangmanWord(guessedLetter, secretWord, hangmanWord):
    '''
    Updates hangmanWord according to whether guessedLetter is in secretWord and where in secretWord guessedLetter is in.
    '''
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    count = 0
    secret = list(secretWord)
    if guessedLetter in secret:
       # while count < len(secretWord):
        for i in range((len(secret)-1)):
            findlet = secret[i]
            if findlet == guessedLetter:
                hangmanWord[i] = guessedLetter
            elif findlet in alphabet and hangmanWord[i] != "_":
                hangmanWord[i] =  findlet
            else:
                hangmanWord[i] = "_"
    return hangmanWord




def processUserGuess(guessedLetter, secretWord, hangmanWord, misses):
    '''
    Uses the information in the parameters to update the user's progress in the hangman game.
    '''
    resultlist = []
    beforeword = hangmanWord
    hangmanword = updateHangmanWord(guessedLetter, secretWord, hangmanWord)
    resultlist.append(hangmanword)
    if hangmanWord == beforeword:
        misses -= 1
        resultlist.append(misses)
        resultlist.append(False)
    else:
        resultlist.append(misses)
        resultlist.append(True)
    return resultlist




def runGame(filename):
    '''
    This function sets up the game, runs each round, and prints a final message on whether or not the user won.
    True is returned if the user won the game. If the user lost the game, False is returned.
    '''
    words = []
    file = open(filename)
    for line in file:
        words.append(line)
    length = random.randint(5,11)
    misses = handleUserInputDifficulty()
    secretWord = getWord(words, length)
    hangmanWord = list(secretWord)
    hangdude = []
    for s in range((len(hangmanWord)-1)):
        hangdude.append("_")

    hangmanWord = hangdude
    #print(secretWord)
    lettersGuessed = []

    while misses > 0:
        displayString = createDisplayString(lettersGuessed, misses, hangmanWord)
        guessedLetter = handleUserInputLetterGuess(lettersGuessed, displayString)
        bag = processUserGuess(guessedLetter, secretWord, hangmanWord, misses)
        misses = bag[1]
        hangmanWord = bag[0]
        if "_" not in hangmanWord:
            print("You win!")
            return True

    #find a eay to update hangman in the list
    print("You lose!")
    print("The word was " + secretWord + ".")
    return False

if __name__ == "__main__":
    '''
    Running Hangman.py should start the game, which is done by calling runGame, therefore, we have provided you this code below.
    '''
    runGame('lowerwords.txt')
    #handleUserInputDifficulty()
    #print(getWord(['apple', 'banana', 'grape', 'fruit', 'peach', 'nut', 'dog', 'frog', 'mammary'], 5))
    #print(createDisplayString(['A','B','C','D'], 5, ["_","_","B","_","_"]))
    #print(handleUserInputLetterGuess(['A','B','C','D'], "_____"))
    #print(processUserGuess("a", "banana", ["_","_","_","_","_","_"], 8))
