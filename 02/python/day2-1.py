#!/usr/bin/python

from enum import IntEnum


class Action(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3


opponent_col1_map = {"A": Action.Rock, "B": Action.Paper, "C": Action.Scissors}
user_col2_map = {"X": Action.Rock, "Y": Action.Paper, "Z": Action.Scissors}

victories = {
    Action.Rock: [Action.Scissors],  # Rock beats scissors
    Action.Paper: [Action.Rock],  # Paper beats rock
    Action.Scissors: [Action.Paper],  # Scissors beats paper
}


def determine_score(user_action: Action, opponent_action: Action) -> int:
    # outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

    defeats = victories[user_action]
    if user_action == opponent_action:
        print(f"Both 🧝 & 🧝‍♀️ selected {user_action.name}. It's a tie!")
        return 3 + user_action
    elif opponent_action in defeats:
        print(f"{user_action.name} beats {opponent_action.name}! 🧝‍♀️ wins, 🧝  loses!")
        return 6 + user_action
    else:
        print(f"{opponent_action.name} beats {user_action.name}! 🧝 wins,  🧝‍♀️ loses.")
        return user_action


score = 0
with open("../input.txt") as rps_data:
    for line in rps_data:
        opponent_symbol, user_symbol = line.strip().split()
        score += determine_score(
            user_col2_map[user_symbol], opponent_col1_map[opponent_symbol]
        )

print(f"\nTotal Score: {score}")
