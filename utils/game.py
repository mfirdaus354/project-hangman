"""
Importing libraries
"""
import string as str
import random 

"""
defining class Hangman
"""
class Hangman:
    #class attributes
    POSSIBLE_WORDS = ['becode', 'learning', 'mathematics', 'sessions']

    def __init__(self):
        self.word_to_find = random.choice(Hangman.POSSIBLE_WORDS)
        self.correctly_guessed_letters = ["_" for _ in self.word_to_find]
        self.wrongly_guessed_letters = []
        self.lives = 5
        self.letters_to_use = list(str.ascii_lowercase)
        self.turn_count = 0
        self.error_count = 0
        self.duplicate_loc = []
        self.to_look = 0
    
    #defining method for find locations of dupplicate letters in a self.word_to_find
    def find_duplicate_letter(self, letter):
        self.duplicate_loc = [i for i, l in enumerate(self.word_to_find) if l == letter]
        return self.duplicate_loc

    #defining Hangman.play() method to outline the inner working of the game
    def play(self, guess):
        if guess in self.letters_to_use:
            if guess in self.word_to_find:
                if self.word_to_find.count(guess) != 1:
                    for loc in self.find_duplicate_letter(guess):
                        self.correctly_guessed_letters[loc] = guess
                        self.turn_count += 1
                else:
                    self.correctly_guessed_letters[self.word_to_find.index(guess)] = guess
                    self.turn_count += 1
            elif guess not in self.word_to_find:
                self.lives -= 1
                self.turn_count += 1
                self.wrongly_guessed_letters.append(guess)
        else:
            self.error_count += 1
            self.turn_count += 1
            print("Your input is not a lowercase letter. Please try again!")
        
    #defining Hangman.game_over() method to display a string when the player loses the game
    def game_over(self):
        print("Game over...")

    #defining Hangman.well_played() method to display a string when the player wins the game        
    def well_played(self):
        print(f'You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!')
    
    #defining Hangman.start_game() method to put previously defined methods together to make a functional program
    def start_game(self):
        print("""
-------------------------------------------------------------------------------
                        LET'S PLAY HANGMAN!
-------------------------------------------------------------------------------

        The Great Machine has loaded one secret word into our system.
        Guess that word and win a prize!

-------------------------------------------------------------------------------
        """)

        while self.lives > 0 and "_" in self.correctly_guessed_letters:
            guess = input("Enter a letter: ")
            self.play(guess.lower())
            print("Lives:", self.lives)
            print("Correctly guessed letters:", " | ".join(self.correctly_guessed_letters))
            print("Wrongly guessed letters:", " | ".join(self.wrongly_guessed_letters))
            print('''
-------------------------------------------------------------------------------
             ''')

        if self.lives == 0 and len(self.correctly_guessed_letters) != len(self.word_to_find):
            self.game_over()
        else:
            self.well_played()


"""
Let's play Hangman!!
"""
hangman_game = Hangman()
hangman_game.start_game()


