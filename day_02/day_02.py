'''
 D -> Draw
 L -> Lost
 W -> Win
'''
ACTIONS = {
    "A X": "D",
    "A Y": "W",
    "A Z": "L",
    "B X": "L",
    "B Y": "D",
    "B Z": "W",
    "C X": "W",
    "C Y": "L",
    "C Z": "D",
}

REQUIRED_ACTIONS = {
    "A X": "A Z",
    "A Y": "A X",
    "A Z": "A Y",
    "B X": "B X",
    "B Y": "B Y",
    "B Z": "B Z",
    "C X": "C Y",
    "C Y": "C Z",
    "C Z": "C X",
}

ROUND_SCORES = {
    "L": 0,
    "D": 3,
    "W": 6
}

MOVE_SCORES = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

with open("input.txt") as file:
    lines = file.readlines()

    # Part - 1
    points = 0
    for line in lines:
        action = line.replace("\n", "").strip()
        round = ACTIONS[action]
        points += ROUND_SCORES[round] + MOVE_SCORES[action[-1]]

    print(points)

    # Part - 2
    points = 0
    for line in lines:
        action = line.replace("\n", "").strip()
        required_action = REQUIRED_ACTIONS[action]
        round = ACTIONS[required_action]
        points += ROUND_SCORES[round] + MOVE_SCORES[required_action[-1]]

    print(points)