"""File used for running the game."""

from game_tools import DEFAULT_WINNING_SCORE
from game_tools import calculate_score
from game_tools import find_winner
from game_tools import get_fixed_indexes
from game_tools import is_tuple_out
from game_tools import reroll_unfixed_dice
from game_tools import roll_dice
from game_tools import save_game

def get_player_names():
    """Have the player enter their names and return them in a list."""
    player_one = input("Player 1: Enter your name!: ").strip()
    player_two = input("Player 2: Enter your name!: ").strip()
    
    while player_one == "":
        print("We need your name, Player 1!")
        player_one = input ("Enter Player 1's name: ").strip()
        
    while player_two == "":
        print("We need your name, Player 2!")
        player_two = input ("Enter Player 2's name: ").strip()
        
    return [player_one, player_two]


def show_scores(scores):
    """Print the current scores to show players where they stand"""
    print("\nCurrent scores:")

    for player, score in scores.items():
        print(f"{player}: {score}")


def play_turn(player_name):
    """Let one player roll, reroll, or stop for the turn."""
    print(f"\n{player_name}'s turn")

    dice = roll_dice()

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

        choice = input("Enter S to stop or R to reroll: ").strip().lower()

        if choice == "s":
            turn_score = calculate_score(dice)
            print(f"You scored {turn_score} points this turn.")
            return turn_score
        elif choice == "r":
            dice = reroll_unfixed_dice(dice, fixed_indexes)
        else:
            print("Please enter S to stop or R to reroll.")


def main():
    """Start the game and control the main game loop."""
    print("Welcome to Tuple Out!")
    print(f"The first player to reach {DEFAULT_WINNING_SCORE} points wins.")

    players = get_player_names()
    scores = {}

    for player in players:
        scores[player] = 0

    while max(scores.values()) < DEFAULT_WINNING_SCORE:
        for player in players:
            show_scores(scores)
            turn_score = play_turn(player)
            scores[player] += turn_score

            if scores[player] >= DEFAULT_WINNING_SCORE:
                break

    winner = find_winner(scores)
    save_game(scores, winner)

    print()
    print("=" * 40)
    print("\nGame over!")
    print("=" * 40)
    show_scores(scores)
    print()
    print(f"\nThe winner is {winner}!")
    print("Game results were saved to game_records.csv.")


if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
def play_turn(player_name):
    """Play one turn for a player and return the points earned."""
    print()
    print("-" * 40)
    print(f"\n{player_name}'s turn")
    print("-" * 40)
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
    print(f"The first player to reach {DEFAULT_WINNING_SCORE} points wins. Let's begin!")

    player_name = input("Enter a player name: ")
    score = play_turn(player_name)

    print(f"\n{player_name} finished the turn with {score} points.")


main()