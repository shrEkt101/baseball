import random

from team import Team
from players import Player


def single(bases):
    """
    Return the state of the bases after a single, followed by the runs scored.

    >>> bases = [0,0,0]
    >>> bases = single(bases)[0]
    >>> print(bases)
    [1, 0, 0]
    """

    if bases == [0, 0, 0]:
        bases = [1, 0, 0]
        return (bases, 0)

    elif bases == [1, 0, 0]:
        bases = [1, 1, 0]
        return (bases, 0)

    elif bases == [0, 1, 0]:
        bases = [1, 0, 1]
        return (bases, 0)

    elif bases == [1, 1, 0]:
        bases = [1, 1, 1]
        return (bases, 0)

    elif bases == [0, 0, 1]:
        bases = [1, 0, 0]
        return (bases, 1)

    elif bases == [1, 0, 1]:
        bases = [1, 1, 0]
        return (bases, 1)

    elif bases == [0, 1, 1]:
        bases = [1, 0, 1]
        return (bases, 1)

    elif bases == [1, 1, 1]:
        return (bases, 1)


def double(bases):

    if bases == [0, 0, 0]:
        bases = [0, 1, 0]
        return (bases, 0)

    elif bases == [1, 0, 0]:
        bases = [0, 1, 1]
        return (bases, 0)

    elif bases == [0, 1, 0]:
        bases = [0, 1, 0]
        return (bases, 1)

    elif bases == [1, 1, 0]:
        bases = [0, 1, 1]
        return (bases, 1)

    elif bases == [0, 0, 1]:
        bases = [0, 1, 0]
        return (bases, 1)

    elif bases == [1, 0, 1]:
        bases = [0, 1, 1]
        return (bases, 1)

    elif bases == [0, 1, 1]:
        bases = [0, 1, 0]
        return (bases, 2)

    elif bases == [1, 1, 1]:
        bases = [0, 1, 1]
        return (bases, 2)


def triple(bases):

    if bases == [0, 0, 0]:
        bases = [0, 0, 1]
        return (bases, 0)

    elif bases == [1, 0, 0]:
        bases = [0, 0, 1]
        return (bases, 1)

    elif bases == [0, 1, 0]:
        bases = [0, 0, 1]
        return (bases, 1)

    elif bases == [1, 1, 0]:
        bases = [0, 0, 1]
        return (bases, 2)

    elif bases == [0, 0, 1]:
        bases = [0, 0, 1]
        return (bases, 1)

    elif bases == [1, 0, 1]:
        bases = [0, 0, 1]
        return (bases, 2)

    elif bases == [0, 1, 1]:
        bases = [0, 0, 1]
        return (bases, 2)

    elif bases == [1, 1, 1]:
        bases = [0, 0, 1]
        return (bases, 3)


def Play(team1: Team, team2: Team):
    inning = 1.0
    total1 = []
    total2 = []
    hits1 = []
    hits2 = []


    # who in the lineup is batting
    lineup1 = 0
    lineup2 = 0

    while inning < 10 or sum(total1) == sum(total2):
        score1 = 0
        score2 = 0
        hit_count1 = 0
        hit_count2 = 0
        bases = [0, 0, 0]
        out = 0

        while out < 3:
            # chance of hit
            curr = team1.players[lineup1]
            chance = curr.avg
            dice1 = random.random()

            # a hit
            if dice1 < chance:
                hit_count1 += 1
                dice2 = random.random()
                if dice2 < curr.single:
                    # single
                    temp = single(bases)
                    bases = temp[0]
                    score1 += temp[1]
                elif dice2 > curr.single + curr.double:
                    # double
                    temp = double(bases)
                    bases = temp[0]
                    score1 += temp[1]
                elif dice2 > curr.single + curr.double + curr.triple:
                    # triple
                    temp = triple(bases)
                    bases = temp[0]
                    score1 += temp[1]
                else:
                    score1 += sum(bases) + 1
                    bases = [0, 0, 0]

                lineup1 = (lineup1 + 1) % 9
            else:
                out += 1
        inning += 0.5

        bases = [0, 0, 0]
        out = 0

        while out < 3:
            # chance of hit
            curr = team2.players[lineup2]
            chance = curr.avg
            dice1 = random.random()

            # a hit
            if dice1 < chance:
                hit_count2 += 1
                dice2 = random.random()
                if dice2 < curr.single:
                    # single
                    temp = single(bases)
                    bases = temp[0]
                    score2 += temp[1]
                elif dice2 > curr.single + curr.double:
                    # double
                    temp = double(bases)
                    bases = temp[0]
                    score2 += temp[1]
                elif dice2 > curr.single + curr.double + curr.triple:
                    # triple
                    temp = triple(bases)
                    bases = temp[0]
                    score2 += temp[1]
                else:
                    score2 += sum(bases) + 1
                    bases = [0, 0, 0]

                lineup2 = (lineup2 + 1) % 9
            else:
                out += 1
        turn = 1
        inning += 0.5

        total1.append(score1)
        total2.append(score2)
        hits1.append(hit_count1)
        hits2.append(hit_count2)

    scoreboard = ""
    for i in range(int(inning) - 1):
        scoreboard += f"|{i+1:>2}"

    team1Score = ""
    team2Score = ""
    for i in range(int(inning) - 1):
        team1Score += f"|{total1[i]:>2}"
        team2Score += f"|{total2[i]:>2}"

    # print("inning" + scoreboard + "| T| H")
    # print(f"{team1.name:<6}" + team1Score + f"|{sum(total1):>2}|{sum(hits1):>2}")
    # print(f"{team2.name:<6}" + team2Score + f"|{sum(total2):>2}|{sum(hits2):>2}")

    return [sum(total1), sum(total2)], [sum(hits1), sum(hits2)], inning, "inning" + scoreboard + "| T| H",f"{team1.name:<6}" + team1Score + f"|{sum(total1):>2}|{sum(hits1):>2}", f"{team2.name:<6}" + team2Score + f"|{sum(total2):>2}|{sum(hits2):>2}"
