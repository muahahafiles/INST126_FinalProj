"""Tuple Out dice game helper functions."""

import csv
from pathlib import Path

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Game settings 
DICE_COUNT = 3
DIE_SIDES = 6
DEFAULT_WINNING_SCORE = 50
RECORD_FILE = "game_records.csv"
GRAPH_FILE = "score_graph.png"

#Game tools functions / methods 
def roll_die() -> int:
    """Return a single random die roll with numpy."""
    return int(np.random.randint(1, DIE_SIDES + 1))


def roll_dice(count: int = DICE_COUNT) -> list[int]:
    """Return a list of random die rolls using numpy."""
    rolls = np.random.randint(1, DIE_SIDES + 1, size=count)
    return [int(roll) for roll in rolls]


def is_tuple_out(dice: list[int]) -> bool:
    """Return True when all dice have the same value."""
    return len(set(dice)) == 1


def fixed_indices(dice: list[int]) -> list[int]:
    """Return the indexes of dice that are fixed by a matching pair."""
    fixed = []

    for index, value in enumerate(dice):
        if dice.count(value) == 2:
            fixed.append(index)

    return fixed


def available_indices(dice: list[int], fixed: list[int]) -> list[int]:
    """Return the indexes of dice that may still be re-rolled."""
    available = []

    for index in range(len(dice)):
        if index not in fixed:
            available.append(index)

    return available


    