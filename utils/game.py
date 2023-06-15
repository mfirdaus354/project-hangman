"""
-------------------------------------------------------------------------------
project-hangman
-------------------------------------------------------------------------------
By: Muhammad Anhar Firdausyi

Last Update: 
"""


# Importing libraries

import string as str
import random 

"""
Defining class Hangman
Has a class attribute: Hangman.LETTER_TO_USE
There are 5 methods enlisted within the class, with the purpose to start the game upon calling the 'star_game' method
"""
class Hangman:
    
    LETTERS_TO_USE = list(str.ascii_lowercase)
        # class attributes
    def __init__(self):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = random.choice(self.possible_words)
        self.turn_count = 0
        self.error_count = 0
        self.correctly_guessed_letters = ["_" for _ in self.word_to_find] 
        self.wrongly_guessed_letters = []
        self.lives = 5
    
        ## to enhance user experience and to make it easier to draw conclusion of the game, these following attributes are defined
        self.duplicate_loc = []
        self.to_look = 0
        
        
    # defining method for find locations of duplicate letters in a self.word_to_find
    def find_duplicate_letter(self, letter):
        self.duplicate_loc = [i for i, l in enumerate(self.word_to_find) if l == letter]
        return self.duplicate_loc
    
    # defining Hangman.play() method to outline the inner working of the game
    def play(self, guess):
        if guess in Hangman.LETTERS_TO_USE: 
            if guess in self.word_to_find:

                #### to address situations when self.word_to_find contains duplicate letters
                if self.word_to_find.count(guess) != 1:
                    for loc in self.find_duplicate_letter(guess):
                        self.correctly_guessed_letters[loc] = guess
                        self.turn_count += 1
                else:
                    self.correctly_guessed_letters[self.word_to_find.index(guess)] = guess
                    self.turn_count += 1

            ### to address situations when user input a previously used letter
            elif guess in self.wrongly_guessed_letters or guess in self.correctly_guessed_letters:
                if guess != "_":
                    self.error_count += 1
                    self.turn_count += 1
                    print("You have used that letter before. Think hard and try again!")

            else:
                self.lives -= 1
                self.turn_count += 1
                self.wrongly_guessed_letters.append(guess)
        else:
            self.error_count += 1
            self.turn_count += 1
            print("Your input is not a lowercase letter. Please try again!")

    # defining Hangman.game_over() method to display a string when the player loses the game
    def game_over(self):
        print("Game over...")

    # defining Hangman.well_played() method to display a string when the player wins the game        
    def well_played(self):
        print(f'''
Congratulations ! 
You have found the word: \'{self.word_to_find}\' in {self.turn_count} turns with {self.error_count} errors!''')
    
    # defining Hangman.is_continue() to inquire the player what to do next
    def is_continue(self):
        while True:
            inquiry = input("""
-------------------------------------------------------------------------------
    Do you wish to continue? 
    Type [y] if you wish to continue playing
    Type [n] if you wish to quit playing
-------------------------------------------------------------------------------
    """)
            if inquiry == "y":
                new_game = Hangman()
                new_game.start_game()
                break

            elif inquiry == "n":
                print("""
-------------------------------------------------------------------------------        
Thank you for playing! Have a nice day! 
------------------------------------------------------------------------------- 
        """)
                break

            else:
                print("Invalid input. Please try again.")
    
    # defining Hangman.start_game() method to put previously-defined methods together to make a functional program
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

        if self.lives == 0:
            self.game_over()

        else:
            self.well_played()
        
        self.is_continue()


