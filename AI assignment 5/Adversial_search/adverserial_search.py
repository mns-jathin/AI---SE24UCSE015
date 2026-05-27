"""
Adversarial Search Algorithms
Game: Stone Picking Game

Rules:
- Start with random stones (10–20)
- Players take either 1 or 2 stones
- Whoever takes the last stone wins
"""

import math
import random


class StoneGame:

    def __init__(self, stones, player="X"):
        self.stones = stones
        self.player = player

    def actions(self):
        moves = []

        if self.stones >= 1:
            moves.append(1)

        if self.stones >= 2:
            moves.append(2)

        return moves

    def result(self, move):

        remaining = self.stones - move

        next_player = "O" if self.player == "X" else "X"

        return StoneGame(
            remaining,
            next_player
        )

    def terminal(self):
        return self.stones == 0

    def utility(self):

        if self.stones != 0:
            return 0

        previous = "O" if self.player == "X" else "X"

        if previous == "X":
            return 1
        else:
            return -1


def minimax(state):

    if state.terminal():
        return state.utility(), None

    if state.player == "X":

        best = -math.inf
        move = None

        for action in state.actions():

            value, _ = minimax(
                state.result(action)
            )

            if value > best:
                best = value
                move = action

        return best, move

    else:

        best = math.inf
        move = None

        for action in state.actions():

            value, _ = minimax(
                state.result(action)
            )

            if value < best:
                best = value
                move = action

        return best, move


def alpha_beta(
        state,
        alpha=-math.inf,
        beta=math.inf):

    if state.terminal():
        return state.utility(), None

    if state.player == "X":

        best = -math.inf
        move = None

        for action in state.actions():

            value, _ = alpha_beta(
                state.result(action),
                alpha,
                beta
            )

            if value > best:
                best = value
                move = action

            alpha = max(
                alpha,
                best
            )

            if beta <= alpha:
                break

        return best, move

    else:

        best = math.inf
        move = None

        for action in state.actions():

            value, _ = alpha_beta(
                state.result(action),
                alpha,
                beta
            )

            if value < best:
                best = value
                move = action

            beta = min(
                beta,
                best
            )

            if beta <= alpha:
                break

        return best, move


def heuristic(state):

    return -state.stones


def heuristic_alpha_beta(
        state,
        depth,
        alpha=-math.inf,
        beta=math.inf):

    if state.terminal():
        return state.utility(), None

    if depth == 0:
        return heuristic(state), None

    if state.player == "X":

        best = -math.inf
        move = None

        for action in state.actions():

            value, _ = heuristic_alpha_beta(
                state.result(action),
                depth-1,
                alpha,
                beta
            )

            if value > best:
                best = value
                move = action

            alpha = max(
                alpha,
                best
            )

            if beta <= alpha:
                break

        return best, move

    else:

        best = math.inf
        move = None

        for action in state.actions():

            value, _ = heuristic_alpha_beta(
                state.result(action),
                depth-1,
                alpha,
                beta
            )

            if value < best:
                best = value
                move = action

            beta = min(
                beta,
                best
            )

            if beta <= alpha:
                break

        return best, move


def mcts(state, simulations=1000):

    scores = {}

    for action in state.actions():

        wins = 0

        for _ in range(simulations):

            current = state.result(
                action
            )

            while not current.terminal():

                move = random.choice(
                    current.actions()
                )

                current = current.result(
                    move
                )

            if current.utility() == 1:
                wins += 1

        scores[action] = wins

    return max(
        scores,
        key=scores.get
    )


stones = random.randint(
    10,
    20
)

state = StoneGame(
    stones
)

print(
    "Initial stones:",
    stones
)

print(
    "Current player:",
    state.player
)

print(
    "Minimax move:",
    minimax(state)[1]
)

print(
    "Alpha-Beta move:",
    alpha_beta(state)[1]
)

print(
    "Heuristic Alpha-Beta move:",
    heuristic_alpha_beta(
        state,
        depth=3
    )[1]
)

print(
    "MCTS move:",
    mcts(state)
)