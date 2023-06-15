"""
project-hangman
-------------------------------------------------------------------------------
By: Muhammad Anhar Firdausyi
-------------------------------------------------------------------------------

Last Update: 15/06/2023 22:00
"""


# Importing libraries

import string as str
import random 

class Hangman:
    """
        Defining class Hangman
        It has a class attribute: Hangman.LETTER_TO_USE
        There are 7 methods enlisted within the class
        The 'star_game' method is called to start the game
    """
    
    LETTERS_TO_USE = list(str.ascii_lowercase)
        # class attributes
    def __init__(self):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = random.choice(self.possible_words)
        self.turn_count = 0
        self.error_count = 0
        self.lives = 5
        self.correctly_guessed_letters = ["_" for _ in self.word_to_find] 
        self.wrongly_guessed_letters = []
        self.duplicate_loc = []
        self.to_look = 0

        
    
    def find_duplicate_letter(self, letter):
        # defining method for find locations of duplicate letters in a self.word_to_find
        self.duplicate_loc = [i for i, l in enumerate(self.word_to_find) if l == letter]
        return self.duplicate_loc
    
    def play(self, guess):
        # defining Hangman.play() method to outline the inner working of the game

        if guess not in Hangman.LETTERS_TO_USE:
            self.error_count += 1
            self.turn_count += 1
            print("Your input is not a (lowercase) letter. Please try again!")
        
        if guess in self.word_to_find or guess in self.wrongly_guessed_letters or guess in self.correctly_guessed_letters:
            if guess in self.word_to_find:
                if self.word_to_find.count(guess) != 1:
                        ###### to address situations when guess has multiple occurences in self.word_to_find
                    for loc in self.find_duplicate_letter(guess):
                        self.correctly_guessed_letters[loc] = guess
                        self.turn_count += 1
                else:
                    ###### to address situations when guess has single occurrence of self.word_to_find
                    self.correctly_guessed_letters[self.word_to_find.index(guess)] = guess
                    self.turn_count += 
            elif guess in self.wrongly_guessed_letters or guess in self.correctly_guessed_letters:
                #### to address situations when user input a previously used letter
                if guess != "_":
                    self.error_count += 1
                    self.turn_count += 1
                    print("You have used that letter before. Think hard and try again!")
            else:
                ##### if the condition 'guess in self.word_to_find' is not fulfilled
                self.lives -= 1
                self.turn_count += 1
                self.wrongly_guessed_letters.append(guess)
        else:
            """
            if the condition below is not fulfilled:
                
            'if guess in self.word_to_find 
            or guess in self.wrongly_guessed_letters 
            or guess in self.correctly_guessed_letters'

            """
            self.lives -= 1
            self.turn_count += 1
            self.wrongly_guessed_letters.append(guess)
        
    def game_over(self):
        # defining Hangman.game_over() method to display a string when the player loses the game
        print("Game over...")
       
    def well_played(self):
        # defining Hangman.well_played() method to display a string when the player wins the game 
        print(f'''
Congratulations ! 
You have found the word: \'{self.word_to_find}\' 
You did it in {self.turn_count} turns with {len(self.wrongly_guessed_letters)} mistakes and {self.error_count} errors!''')
    
    def is_continue(self):
        # defining Hangman.is_continue() to inquire the player what to do next
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
    
    
    def start_game(self):
        # defining Hangman.start_game() method to put previously-defined methods together to make a functional program
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
            print("Errors:", self.error_count)
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