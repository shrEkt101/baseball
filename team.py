from players import Player


class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players

    def __repr__(self):
        return self.name
