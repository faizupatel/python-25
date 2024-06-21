#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Faizan
#
# Created:     13/06/2024
# Copyright:   (c) Faizan 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    players = ['X', 'O']
    player_index = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    for _ in range(9):
        row = int(input(f"Player {players[player_index]}, enter row (0, 1, 2): "))
        col = int(input(f"Player {players[player_index]}, enter column (0, 1, 2): "))

        if board[row][col] == " ":
            board[row][col] = players[player_index]
        else:
            print("This position is already taken. Try again.")
            continue

        print_board(board)

        if check_winner(board, players[player_index]):
            print(f"Player {players[player_index]} wins!")
            break

        player_index = (player_index + 1) % 2
    else:
        print("It's a draw!")

tic_tac_toe()
