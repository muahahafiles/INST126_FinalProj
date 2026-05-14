"""File used for running the game."""

from game_tools import DEFAULT_WINNING_SCORE
from game_tools import calculate_score
from game_tools import roll_dice


def main():
    print("Welcome to the Tuple Out game! Have fun!")
    print(f"The first player to reach {DEFAULT_WINNING_SCORE} points is the winner.")
    
    player_name = input("Enter a player name: ")
    
    
    dice = roll_dice()
    score = calculate_score(dice)

    print(f"{player_name} rolled: {dice}")
    print(f"Starting score for this sample turn: {score}")
    
    
main() 