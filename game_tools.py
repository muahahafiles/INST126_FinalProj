"""Tuple Out dice game helper functions."""

import csv
import os

import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# Game settings 
DICE_COUNT = 3
DIE_SIDES = 6
DEFAULT_WINNING_SCORE = 50
RECORD_FILE = "game_records.csv"
GRAPH_FILE = "score_graph.png"

#Game tools functions / methods 

def roll_dice(dice_count=DICE_COUNT, die_sides=DIE_SIDES):
    """Roll the dice and return the results as a list."""
    rolls = np.random.randint(1, die_sides + 1, size=dice_count)
    return rolls.tolist()


def is_tuple_out(dice):
    """Return True if all dice have the same value."""
    return len(set(dice)) == 1


def get_fixed_indexes(dice):
    """Find which dice are locked in place."""
    fixed_indexes = []

    for value in dice:
        if dice.count(value) == 2:
            for index, die in enumerate(dice):
                if die == value:
                    fixed_indexes.append(index)
            return fixed_indexes

    return fixed_indexes


def reroll_unfixed_dice(dice, fixed_indexes):
    """Reroll the dice that are still in play."""
    new_dice = dice.copy()

    for index in range(len(new_dice)):
        if index not in fixed_indexes:
            new_dice[index] = roll_dice(1)[0]

    return new_dice


def calculate_score(dice):
    """Add up the dice for the player's turn score."""
    return sum(dice)


def find_winner(scores):
    """Return the player with the highest score."""
    return max(scores, key=scores.get)


def save_game(scores, winner, record_file=RECORD_FILE):
    """Save the final scores after a game ends."""
    file_exists = os.path.exists(record_file)

    with open(record_file, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["player", "score", "winner"])

        for player, score in scores.items():
            if player == winner:
                winner_status = "yes"
            else:
                winner_status = "no"

            writer.writerow([player, score, winner_status])


def score_graph(score_history, graph_file=GRAPH_FILE):
    """Create a graph showing how the game score changed."""
    score_data = pd.DataFrame(history)
    
    
    sns.lineplot(data=score_data, x="turn", y="score", hue="player")
    plt.title("Tuple Out Score Progress")
    plt.xlabel("Turn")
    plt.ylabel("Score")
    plt.tight_layout()
    plt.savefig(graph_file)
    plt.close()