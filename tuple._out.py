"""File used for running the game."""

from game_tools import DEFAULT_WINNING_SCORE
from game_tools import calculate_score
from game_tools import get_fixed_indexes
from game_tools import is_tuple_out
from game_tools import roll_dice


def play_turn(player_name):
    """Play one turn for a player and return the points earned."""
    print(f"\n{player_name}'s turn")

    dice = roll_dice()
    fixed_indexes = get_fixed_indexes(dice)

    while True:
        print(f"Current dice: {dice}")

        if is_tuple_out(dice):
            print("Tuple out! You score 0 points this turn.")
            return 0

        fixed_indexes = get_fixed_indexes(dice)

        if fixed_indexes:
            print(f"Fixed dice positions: {fixed_indexes}")
        else:
            print("No dice are fixed right now.")

        choice = input("Enter S to stop or R to reroll: ").lower()

        if choice == "s":
            turn_score = calculate_score(dice)
            print(f"You scored {turn_score} points this turn.")
            return turn_score
        elif choice == "r":
            dice = reroll_unfixed_dice(dice, fixed_indexes)
        else:
            print("Please enter S to stop or R to reroll.")


def main():
    """Start the game and run one sample player turn."""
    print("Welcome to Tuple Out!")
    print(f"The first player to reach {DEFAULT_WINNING_SCORE} points wins.")

    player_name = input("Enter a player name: ")
    score = play_turn(player_name)

    print(f"\n{player_name} finished the turn with {score} points.")


main()