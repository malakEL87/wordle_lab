"""Module for displaying colored text in the terminal for the Wordle game.

    Functions:
        - header: Prints a header in the terminal.
        - game_instructions: Prints the game instructions in the terminal.
        - game_start_display: Prints the starting message for the game.
        - display_word_feedback: Displays the colored feedback for a guess.

    Constants:
        - COLORS: A dictionary containing ANSI color codes for GREEN, YELLOW, RED, and RESET.
"""


from typing import List

# ANSI color formatting
COLORS = {
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "RED": "\033[31m",
    "RESET": "\033[0m"
}


 def header(text: str) -> None:
   """Print a header in the terminal."""
     header = f"""
----------------------------------------------------------------------------------------------------------
                                                WORDLE GAME
----------------------------------------------------------------------------------------------------------
    """
    print(header)
   pass


def game_instructions():
    """Print the game instructions in the terminal."""
    print("Welcome to the Wordle game!")
    print("You have 6 attempts to guess the 5-letter word.")
    print("Feedback will be provided for each guess:")
    print(f"{COLORS['GREEN']}GREEN{COLORS['RESET']} = Correct letter in the correct position.")
    print(f"{COLORS['YELLOW']}YELLOW{COLORS['RESET']} = Correct letter in the wrong position.")
    print(f"{COLORS['RED']}RED{COLORS['RESET']} = Incorrect letter.")
    print("Good luck!\n")

    pass


def game_start_display():
    """Print the starting message for the game."""
    print("Starting the Wordle game!")
    print("guess the word.\n")
    pass


def display_word_feedback(guess: str, feedback: List[str]) -> str:
    """Display the coloured feedback for a guess."""
    
def display_word_feedback(guess: str, feedback: List[str]) -> str:
   """Display the coloured feedback for a guess."""
    colored_guess = ""
    for letter, color in zip(guess, feedback):
        if color == "GREEN":
            colored_guess += f"{COLORS['GREEN']}{letter}{COLORS['RESET']}"
        elif color == "YELLOW":
            colored_guess += f"{COLORS['YELLOW']}{letter}{COLORS['RESET']}"
        else:  # RED
            colored_guess += f"{COLORS['RED']}{letter}{COLORS['RESET']}"
    print(colored_guess)
    return colored_guess
    pass


def display_win(word: str, attempt: int) -> None:
    """Display for winning"""
    """Display for winning."""
    print(Congratulations!You guessed the right word!")
  pass


def display_lost(word: str) -> None:
    """Display for losing"""
    pass    print(Game Over. Better luck next time!")

