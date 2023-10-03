import sys

class Square:
    def __init__(self, name, linked_squares=None, parity=None):
        self.name = name
        self.parity = parity
        self.linked_squares = linked_squares

    def set_parity(self, new_parity):
        self.parity = new_parity

    def get_parity(self):
    	return self.parity

    def get_name(self):
    	return self.name

    def check_for_three(self, current_parity):
	    parity_to_match = current_parity
	    for chain in self.linked_squares:
	        in_a_row = 0  # Initialize the count for each chain
	        for square_to_check in chain:
	            found_match = False  # Initialize a flag for the current chain
	            for square in squares:
	                if square.get_name() == square_to_check and square.get_parity() == parity_to_match:
	                    found_match = True
	                    break  # Break out of the innermost loop when a match is found
	            if not found_match:
	                break  # Break out of the current chain loop if a mismatch is found
	            in_a_row += 1
	            if in_a_row == 3:
	                return True
	    return False

                   

print("Let's play some frickin tictactoe!")
print("To make a move, type the name of the square you would like to move in. The name of the square is a combination of the row it's in (A, B, or C) and then the column it's in (1, 2, or 3). For example, to play your move in the top left corner, you would type in A1 and then press enter.")

# Setting up board
squares = []
A1, A2, A3, B1, B2, B3, C1, C2, C3 = None, None, None, None, None, None, None, None, None
A1 = Square("A1", [[A2, A3], [B2, C3], [B1, C1]])
A2 = Square("A2", [[B2, C2], [A1, A3]])
A3 = Square("A3", [[B3, C3], [B2, C1], [A1, A2]])
B1 = Square("B1", [[B2, B3], [A1, A3]])
B2 = Square("B2", [[A1, C3], [C1, A3], [B1, B3], [A2, C2]])
B3 = Square("B3", [[B1, B2], [A3, C3]])
C1 = Square("C1", [[B2, A3], [C2, C3], [A1, B1]])
C2 = Square("C2", [[C1, C3], [A2, B2]])
C3 = Square("C3", [[C1, C2], [A1, B2], [A3, B3]])
squares.extend([A1, A2, A3, B1, B2, B3, C1, C2, C3])


# Receives, checks, and prepares input on where to play
occupied_squares = []
def get_input():
    sqr = input("Where would you like to play? ").upper()
    # Finds and selects square that player selected
    for square in squares:
        if square.get_name() == sqr:
            # Ensures that square has not yet been played in
            if square.get_parity() != None:
                print("Oops, that square has already been played in, please pick a different square.")
                return get_input()
            return square
    print("Oops, that wasn't a valid input. Please try again.")
    return get_input()


# Game play
win_status = False
players_turn = None
number_of_moves = 0

while win_status is False and number_of_moves < 9:
    # Ensures players take turns
    if players_turn == "X":
        players_turn = "O"
    else:
        players_turn = "X"
    print("It is player " + players_turn + "'s turn.")

    played_square = get_input()
    played_square.set_parity(players_turn)
    number_of_moves += 1
    # Checks for winners and updates win_status
    win_status = played_square.check_for_three(players_turn)

if win_status is True:
    print("The " + players_turn + "'s won the game this time! Yay!")
elif number_of_moves == 9:
    print("Looks like the cat got this one. Well done though, that's what happens when both players play perfectly!")
