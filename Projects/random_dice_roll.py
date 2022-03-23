from os import system
import random

#parse the input function
def parse_input(input_string):
    """Return `input_string` as an integer between 1 and 6.
    
    Check if `input_string` is an integer number between 1 and 6.

    If so, return an integer with the same value. Otherwise, tell

    the user to enter a valid number and quit the program.

    """
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number between 1 and 6")
        raise SystemExit(1)


def roll_dice(num_dice):
     """
     Return a list of integers with length `num_dice`.

     Each integer in the returned list is a random number between

     1 and 6, inclusive.
    """
     roll_results = []
     for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
     return roll_results

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",  
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (

        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "


def generate_die_faces_diagram(dice_values):
    """
    Return an ASCII diagram of dice faces from `dice_values`.
    The string returned contains an ASCII representation of each die.
    For example, if `dice_values = [4, 1, 3, 2]` then the string
    returned looks like this:
  
    ~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~
    ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
    │  ●   ●  │ │         │ │  ●      │ │  ●      │
    │         │ │    ●    │ │    ●    │ │         │
    │  ●   ●  │ │         │ │      ●  │ │      ●  │
    └─────────┘ └─────────┘ └─────────┘ └─────────┘
    """
    #Generate a list of die faces from DICE_ART
    dice_face = []
    for value in dice_values:
        dice_face.append(DICE_ART[value])
    
    #Generate a list contatinining the die faces in a row
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_face:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)
    
    #Generate headers with the word "results" centered
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram


#Diver Code
#1. Get and Validate User Input
num_dice_input = input("How many dice do you want to roll? : ")
num_dice = parse_input(num_dice_input)
#2. Roll the dice
roll_results = roll_dice(num_dice)
#print(roll_results)
#3. Generate the dice faces diagram
dice_faces_diagram = generate_die_faces_diagram(roll_results)
#Display the dice faces diagram
print(f"\n{dice_faces_diagram}")