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
    WORD_TO_FIND = POSSIBLE_WORDS[random.randint(0, len(POSSIBLE_WORDS)-1)]
    LETTERS_TO_USE = list(str.ascii_lowercase)

    def __init__(self):
        self.lives = 5   
        self.correctly_guessed_letters = ["_" for _ in Hangman.WORD_TO_FIND]
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0
        self.duplicate_loc = []
        self.to_look = -1
    
    #defining method for find locations of dupplicate letters in a Hangman.WORD_TO_FIND
    def find_duplicate_letter(self, letter):
         while True:
              self.loc_dupli = Hangman.WORD_TO_FIND.index(letter, self.to_look+1)
              self.duplicate_loc.append(self.loc_dupli)
              self.to_look = self.loc_dupli
              return self.duplicate_loc

    def play(self, guess):
            if guess in Hangman.LETTERS_TO_USE :
                if guess in Hangman.WORD_TO_FIND :
                    if Hangman.WORD_TO_FIND.count(guess) != 1:
                        for letter in self.find_duplicate_letter(guess):
                            self.correctly_guessed_letters[letter] = guess
                        self.turn_count += 1
                    else:
                         self.correctly_guessed_letters[Hangman.WORD_TO_FIND.index(guess)] = guess
                         self.turn_count += 1
                else:
                    self.lives -= 1
                    self.turn_count += 1
                    self.wrongly_guessed_letters.append(guess)
            else:
                self.error_count += 1
                self.turn_count += 1
                print("Your input is not a (lowercase) letter. Please try again!")
        
    def game_over(self):
            print("game over...")
            
    def well_played(self):
        print(f'You found the word: {Hangman.WORD_TO_FIND} in {self.turn_count} turns with {self.error_count} errors!')
    
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
             guess =  input("Enter a letter = ")
             self.play(guess.lower())
             print("Lives:", self.lives)
             print("Correctly guessed letters:", " | ".join(self.correctly_guessed_letters))
             print("Wrongly guessed letters:", " | ".join(self.wrongly_guessed_letters))

        if self.lives == 0 and len(self.correctly_guessed_letters) != len(Hangman.WORD_TO_FIND):
            self.game_over()
        else:
            self.well_played()


hangman_game = Hangman()
hangman_game.start_game()


