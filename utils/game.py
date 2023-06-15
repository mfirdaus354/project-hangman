import string as str
import random

class Hangman:
    """
    Defining class Hangman.
    It has a class attribute: Hangman.LETTERS_TO_USE.
    There are 7 methods enlisted within the class.
    The 'start_game' method is called to start the game.
    """

    LETTERS_TO_USE = list(str.ascii_lowercase)

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
        # Method to find locations of duplicate letters in self.word_to_find
        self.duplicate_loc = [i for i, l in enumerate(self.word_to_find) if l == letter]
        return self.duplicate_loc

    def play(self, guess):
        # Method to outline the inner workings of the game

        if guess not in Hangman.LETTERS_TO_USE:
            self.error_count += 1
            self.turn_count += 1
            print("Your input is not a lowercase letter. Please try again!")
        else:
            if guess in self.word_to_find:
                if guess in self.correctly_guessed_letters:
                    self.error_count += 1
                    print("You have used that letter before. Think hard and try again!")
                else:
                    if self.word_to_find.count(guess) != 1:
                        # Handle situations when guess has multiple occurrences in self.word_to_find
                        for loc in self.find_duplicate_letter(guess):
                            self.correctly_guessed_letters[loc] = guess
                            self.turn_count += 1
                    else:
                        # Handle situations when guess has a single occurrence in self.word_to_find
                        self.correctly_guessed_letters[self.word_to_find.index(guess)] = guess
                        self.turn_count += 1
            else:
                if guess in self.wrongly_guessed_letters or guess in self.correctly_guessed_letters:
                    print("You have used that letter before. Think hard and try again!")
                    self.error_count += 1
                    self.turn_count += 1
                else:
                    # Handle situations when the guess is not in self.word_to_find
                    print("Wrong answer!")
                    self.lives -= 1
                    self.turn_count += 1
                    self.wrongly_guessed_letters.append(guess)

    def game_over(self):
        # Method to display a message when the player loses the game
        print("Game over...")

    def well_played(self):
        # Method to display a message when the player wins the game
        print(f'''
Congratulations! 
You have found the word: \'{self.word_to_find}\' 
You did it in {self.turn_count} turns with {len(self.wrongly_guessed_letters)} mistakes and {self.error_count} errors!
''')

    def is_continue(self):
        # Method to inquire the player what to do next
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
        # Method to put the previously-defined methods together and make a functional program
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
            print("Turns:", self.turn_count)
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

# Create an instance of Hangman and start the game
game = Hangman()
game.start_game()
