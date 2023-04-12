from games import *

class GameOfNim(Game):
    def __init__(self, board):
        self.board = board
        self.initial = GameState(to_move='MAX', utility=0, board=board, moves=self.get_moves(board))

    
    def actions(self, state):
        """Return a list of the allowable moves at this point."""
        return state.moves
    
    def result(self, state, move):
        """Return the state that results from making a move from a state."""
        board = state.board[:]
        board[move[0]] -= move[1]
        return GameState(to_move='MIN' if state.to_move == 'MAX' else 'MAX',
                         utility=self.compute_utility(board, state.to_move),
                         board=board,
                         moves=self.get_moves(board))
    
    def utility(self, state, player):
        """Return the value of this final state to player."""
        return state.utility if player == 'MAX' else -state.utility
    
    def terminal_test(self, state):
        return state.utility != 0 or state.moves == []
    
    def compute_utulity(self, board, player):
        if sum(board) == 0:
            return 1 if player == 'MAX' else -1
        else:
            return 0
        
    

    

if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1])  # Creating the game instance
    #nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    print(nim.initial.board) # must be [0, 5, 3, 1]
    print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1,3) ))
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first 
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")

    nim.display