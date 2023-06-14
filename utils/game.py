"""
Importing libraries
"""
import string as str
import random 


class Hangman:
    """
    defining class attributes
    """
    POSSIBLE_WORDS = ['becode', 'learning', 'mathematics', 'sessions']
    WORD_TO_FIND = POSSIBLE_WORDS[random.randint(0, len(POSSIBLE_WORDS)-1)]
    LETTERS_TO_USE = list(str.ascii_lowercase)

    def __init__(self):
        self.lives = 5   
        self.correctly_guessed_letters = ["_" for _ in Hangman.WORD_TO_FIND]
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0
    
    def play(self, guess=str):
        while True: 
            if self.guess in Hangman.LETTERS_TO_USE :
                if self.guess in Hangman.WORD_TO_FIND:
                    self.correctly_guessed_letters[Hangman.WORD_TO_FIND.index(self.guess)] = self.guess
                    self.turn_count += 1
                    print(" | ".join(self.correctly_guessed_letters))
                else:
                    self.lives -= 1
                    self.turn_count += 1
                    self.wrongly_guessed_letters.append(self.guess)
            else:
                self.error_count += 1
                self.turn_count += 1
                print("Your input is not a (lowercase) letter. Please try again!")
        
    def game_over(self, game_over):
            print("game over...")
    
    def well_played(self):
        print(f'You found the word: {Hangman.WORD_TO_FIND} in {self.turn_count} turns with {self.error_count} errors!')
    
    def start_game(self):
        play()
        if self.lives == 0 and len(self.correctly_guessed_letters) != len(Hangman.WORD_TO_FIND):
            game_over()
        else:
            well_played()


lets_play = Hangman()

print(type(lets_play))


