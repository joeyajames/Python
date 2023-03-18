import random

# list of words to choose from
words = ['apple', 'banana', 'cherry', 'orange', 'pear']

# function to choose a random word
def choose_word(words):
    return random.choice(words)

# function to play the game
def play_game(word):
    guesses = ''
    turns = 10
    while turns > 0:
        incorrect = 0
        for letter in word:
            if letter in guesses:
                print(letter, end=' ')
            else:
                print('_', end=' ')
                incorrect += 1
        if incorrect == 0:
            print('\nYou win!')
            break
        guess = input('\nGuess a letter: ')
        guesses += guess
        if guess not in word:
            turns -= 1
            print('Incorrect! You have', turns, 'turns left.')
            if turns == 0:
                print('Game over. The word was', word)
                
# main function to run the game
def main():
    print('Welcome to Hangman!')
    word = choose_word(words)
    play_game(word)
    play_again = input('Do you want to play again? (y/n) ')
    if play_again.lower() == 'y':
        main()
    else:
        print('Thanks for playing!')
        
# run the game
if __name__ == '__main__':
    main()
