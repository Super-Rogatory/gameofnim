# Chukwudi Ikem
# For testing locally!
# Making the directory in aima-python available to reference
import sys
import os

sys.path.append(
    os.path.abspath("/home/super-rogatory/Desktop/Spring_2022/CPSC481/aima-python")
)
# For testing locally!

from games import *


class GameOfNim(Game):
    # YOUR CODE GOES HERE
    def __init__(self, board):
        # Similar to TicTacToe, we can define the parameters of our problem.
        moves = []
        for i in range(len(board)):
            for j in range(1, board[i] + 1):  # ex.) changed from [0,5) to [1,6)
                moves.append((i, j))
        self.initial = GameState(to_move="MAX", utility=0, board=board, moves=moves)

    def result(self, state, move):
        if move not in state.moves:
            return state
        board = state.board.copy()  # creates copy of the board
        # modifies the board in response to move
        (index, amount_to_remove) = move  # unpacks the index and the amount to remove
        start = board[index]  # ex.) board[1] = 5
        board[index] -= amount_to_remove  # removes amount from element at position
        # modifies the moves list in response to move. removing from right to left.
        moves = list(state.moves)
        end = start - moves.index(move)  # ex.) index 5 - 3 = 2
        # run from index 4 and end at 1. (0) not included
        for i in range(start - 1, end - 2, -1):
            moves.remove(moves[i])

        return GameState(
            to_move=("MAX" if state.to_move == "MIN" else "MIN"),
            utility=0,
            board=board,
            moves=moves,
        )


if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1])  # Creating the game instance
    # nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    print(nim.initial.board)  # must be [0, 5, 3, 1]
    print(
        nim.initial.moves
    )  # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2,1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1, 5)))
    utility = nim.play_game(alpha_beta_player, query_player)  # computer moves first
    if utility < 0:
        print("MIN won the game")
    else:
        print("MAX won the game")
