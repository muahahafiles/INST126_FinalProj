"""Test for the game's helper functions"""

from game_tools import calculate_score
from game_tools import find_winner
from game_tools import get_fixed_indexes
from game_tools import is_tuple_out
from game_tools import reroll_unfixed_dice
from game_tools import roll_dice


def test_rolls_three_dice():
    """Test that the game rolls three dice."""
    dice = roll_dice()

    assert len(dice) == 3


def test_rolls_stay_in_range():
    """Test that dice rolls stay between 1 and 6."""
    dice = roll_dice()

    for die in dice:
        assert die >= 1
        assert die <= 6


def test_tuple_out():
    """Test that three matching dice count as a tuple out."""
    dice = [4, 4, 4]

    assert is_tuple_out(dice) is True


def test_not_tuple_out():
    """Test that mixed dice do not count as a tuple out."""
    dice = [2, 4, 4]

    assert is_tuple_out(dice) is False


def test_finds_fixed_dice():
    """Test that matching dice are marked as fixed."""
    dice = [2, 5, 5]

    assert get_fixed_indexes(dice) == [1, 2]


def test_no_fixed_dice():
    """Test that no dice are fixed when there is no pair."""
    dice = [1, 3, 5]

    assert get_fixed_indexes(dice) == []


def test_adds_score():
    """Test that the score is the total of the dice."""
    dice = [3, 4, 5]

    assert calculate_score(dice) == 12


def test_finds_winner():
    """Test that the highest-scoring player wins."""
    scores = {
        "Maya": 42,
        "Jordan": 55,
    }

    assert find_winner(scores) == "Jordan"


def test_keeps_fixed_dice():
    """Test that fixed dice do not change when rerolling."""
    dice = [6, 6, 2]
    fixed = [0, 1]

    new_dice = reroll_unfixed_dice(dice, fixed)

    assert new_dice[0] == 6
    assert new_dice[1] == 6
    assert len(new_dice) == 3
