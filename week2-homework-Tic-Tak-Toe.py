# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 17:13:19 2018

@author: Olena

Homework week 2

"""

import numpy as np
import matplotlib.pyplot as plt
import time

"""
Tic-tac-toe (or noughts and crosses) is a simple strategy game 
in which two players take turns placing a mark on a 3x3 board, 
attempting to make a row, column, or diagonal of three with their mark. 
In this homework, we will use the tools we've covered in the past two weeks 
to create a tic-tac-toe simulator and evaluate basic winning strategies.
"""

"""
For our tic-tac-toe board, we will use a numpy array with dimension 3 by 3.
Make a function create_board() that creates such a board, 
with values of integers 0. Call create_board(), and store this as board.

"""
def create_board():
    return np.zeros((3,3), dtype = np.int16)

board = create_board()

"""
Create a function place(board, player, position), where:
player is the current player (an integer 1 or 2)

position a tuple of length 2 specifying a desired location to place their marker.

Your function should only allow the current player to place a marker on the board 
(change the board position to their number) if that position is empty (zero).

Use create_board() to store a board as board, and use place to have Player 1 
place a marker on location (0, 0).

"""

def place(board, player, position):
    if board[position] == 0:
        board[position] = player

place(board, 2, (0, 2))

"""
In this exercise, we will determine which positions are available to either 
player for placing their marker.

Create a function possibilities(board) that returns a list of all 
positions (tuples) on the board that are not occupied (0). 
(Hint: numpy.where is a handy function that returns a list of indices 
that meet a condition.)
board is already defined from previous exercises. 
Call possibilities(board) to see what it returns!

"""
def possibilities(board):
    free_cells = np.where(board == 0)
    return [e for e in zip(free_cells[0], free_cells[1])]
    
possibilities(board)   


"""
The next step is for the current player to place a marker among the available 
positions. In this exercise, we will select an available board position 
at random and place a marker there.


Write a function random_place(board, player) that places a marker for 
the current player at random among all the available positions 
(those currently set to 0).

Find possible placements with possibilities(board).
Select one possible placement at random using random.choice(selection).

board is already defined from previous exercises. 
Call random_place(board, player) to place a random marker for Player 2, 
and store this as board to update its value.

"""

def random_place(board, player):
    import random
    
    selection = possibilities(board)
    
    if not selection == [] :
        place(board, player, random.choice(selection))
    
    
random_place(board, 2)


"""
board is already given. Call random_place(board, player) to place three pieces 
each on board for players 1 and 2. Print board to see your result.

"""
for i in range(3):
    random_place(board, 1)
    random_place(board, 2)

print(board)

"""
Make a function row_win(board, player) that takes the player (integer), 
and determines if any row consists of only their marker. Have it 
return True of this condition is met, and False otherwise.
board is already defined from previous exercises. 
Call row_win to check if Player 1 has a complete row.

"""

def row_win(board, player):
    return np.any(np.all(board == player, 1))
         

row_win(board, 1)        


"""
Create a similar function col_win(board, player) that takes 
the player (integer), and determines if any column consists 
of only their marker. Have it return True if this condition is met, 
and False otherwise.
board is already defined from previous exercises. Call col_win to 
check if Player 1 has a complete column.
"""
def col_win(board, player):
    return np.any(np.all(board == player, 0))
         

col_win(board, 1)      

"""
Finally, create a function diag_win(board, player) that tests if either 
diagonal of the board consists of only their marker. 
Have it return True if this condition is met, and False otherwise.
board is already defined from previous exercises. Call diag_win to check 
if Player 1 has a complete diagonal.

"""
def diag_win(board, player):
     return np.all(np.diag(np.flip(board, axis = 0)) == player) or \
         np.all(np.diag(board) == player)



board = np.eye(3, dtype=np.int16)
board = np.fliplr(board)

diag_win(board, 1)

"""
Create a function evaluate(board) that uses row_win, col_win, and diag_win \
functions for both players. If one of them has won, return that player's number. 
If the board is full but no one has won, return -1. Otherwise, return 0.
board is already defined from previous exercises. Call evaluate to see if 
either player has won the game yet.

"""

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # Check if `row_win`, `col_win`, or `diag_win` apply. 
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            # If so, store `player` as `winner`
            winner = player
            break
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

evaluate(board)


"""
create_board(), random_place(board, player), and evaluate(board) 
have been created from previous exercises. Create a function play_game() that:
Creates a board.
Alternates taking turns between two players (beginning with Player 1), 
placing a marker during each turn.
Evaluates the board for a winner after each placement.
Continues the game until one player wins 
(returning 1 or 2 to reflect the winning player), 
or the game is a draw (returning -1).
Call play_game once.

"""

def play_game():
    
    game_end = 0
    board = create_board()

    while game_end == 0:
        
        for player in [1,2]:
            random_place(board, player)
        
        game_end = evaluate(board)
    
    return game_end

play_game()        


"""
Use the play_game() function to play 1,000 random games, where Player 1 
always goes first.
Import and use the time library to call the time() function both 
before and after playing all 1,000 games.
Store these times as start and stop, respectively.
Subtract them to evaluate how long it takes to play 1,000 games, 
and print your answer.
The library matplotlib.pyplot has already been stored as plt. 
Use plt.hist() and plt.show() to plot a histogram of the results.
Does Player 1 win more than Player 2?
Does either player win more than each player draws?

"""

import time

start_time = time.time()

game_results = []
for i in range(1000):
    game_results.append(play_game())
    
end_time = time.time()

calculation_time = end_time - start_time

calculation_time


plt.hist(game_results, bins = [-1.2, -0.8, 0.8,  1.2, 1.8, 2.2], color = "m", ec = "black", alpha = 0.5)
plt.xlabel("Winners")
plt.ylabel("Number of games")

plt.xticks([-1.0, 1.0, 2.0]);


"""
create_board(), random_place(board, player), and evaluate(board) have been 
created from previous exercises. Create a function play_strategic_game(), 
where Player 1 always starts with the middle square, and otherwise both players 
place their markers randomly.

"""
def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            random_place(board, player)
            winner = evaluate(board) 
            if winner != 0:
                break
    return winner

play_strategic_game()

# ===========================================

start_time = time.time()

game_results = []
for i in range(1000):
    game_results.append(play_strategic_game())
    
end_time = time.time()

calculation_time = end_time - start_time

print(calculation_time)


plt.hist(game_results, bins = [-1.2, -0.8, 0.8,  1.2, 1.8, 2.2], color = "m", ec = "black", alpha = 0.5)
plt.xlabel("Winners")
plt.ylabel("Number of games")

plt.xticks([-1.0, 1.0, 2.0]);
