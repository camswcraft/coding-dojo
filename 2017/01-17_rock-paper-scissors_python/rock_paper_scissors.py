SCISSORS = "scissors"
PAPER = "paper"
ROCK = "rock"

DRAW = 0
P1_WIN = 1
P2_WIN = 2


def round(player1, player2):
    if player1.hand == player2.hand:
        return DRAW
    elif player1.hand == ROCK:
        if player2.hand == SCISSORS:
            return P1_WIN
        return P2_WIN
    elif player1.hand == PAPER:
        if player2.hand == ROCK:
            return P1_WIN
        return P2_WIN
    else:
        if player2.hand == PAPER:
            return P1_WIN
        return P2_WIN


class Player(object):
    def __init__(self, hand):
        self.hand = hand