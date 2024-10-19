import random
from team import Team
from players import Player
from play import Play

teamA = []
teamB = []
for i in range(9):
    # teamA.append(Player("A{}".format(i+1), random.randrange(200, 400)/1000, random.randrange(250, 750)/1000, 0.01))
    # teamB.append(Player("B{}".format(i+1), random.randrange(200, 400)/1000, random.randrange(250, 750)/1000, 0.01))

    teamA.append(Player("A{}".format(i+1), 0.250, 0.7, 0.19, 0.005, 0.105))
    teamB.append(Player("B{}".format(i+1), 0.250, 0.7, 0.19, 0.005, 0.105))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    team1 = Team("Team A", teamA)
    team2 = Team("Team B", teamB)

    P = Play(team1, team2)

    while P[2] < 51 :
        P = Play(team1, team2)

    print(P[3], P[4], P[5], sep="\n")
