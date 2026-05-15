"""File used for running the game."""

from game_tools import DEFAULT_WINNING_SCORE
from game_tools import calculate_score
from game_tools import score_graph
from game_tools import find_winner
from game_tools import get_fixed_indexes
from game_tools import is_tuple_out
from game_tools import load_high_score
from game_tools import reroll_unfixed_dice
from game_tools import roll_dice
from game_tools import save_game
from game_tools import save_high_score


def choose_mode():
    """Let the user pick singleplayer or multiplayer."""
    print()
    print("Choose a game mode:")
    print("1 - Singleplayer")
    print("2 - Multiplayer")

    mode = input("Enter 1 or 2: ").strip()

    while mode != "1" and mode != "2":
        print("Please enter 1 for Singleplayer or 2 for Multiplayer.")
        mode = input("Enter 1 or 2: ").strip()

    return mode



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


def get_single_player():
    """Get the singleplayer ready for the game."""
    player = input("Enter your name: ").strip()

    while player == "":
        print("We need your name!")
        player = input("Enter your name: ").strip()

    return player



def show_scores(scores):
    """Print the current scores to show players where they stand"""
    print()
    print("Current scores:")

    for player, score in scores.items():
        print(f"{player}: {score}")


def play_turn(player_name):
    """Let one player roll, reroll, or stop for the turn."""
    print()
    print("-" * 40)
    print(f"\n{player_name}'s turn")
    print("-" * 40)
    
    dice = roll_dice()

    while True:
        print()
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
            points = calculate_score(dice)
            print(f"You scored {points} points this turn.")
            return points
        elif choice == "r":
            dice = reroll_unfixed_dice(dice, fixed_indexes)
        else:
            print("Please enter S to stop or R to reroll.")


def play_multiplayer():
    """Start the game and control the main game loop."""
    print(f"The first player to reach {DEFAULT_WINNING_SCORE} points wins.")
  

    players = get_player_names()
    scores = {}
    history = []
    turn = 1

    for player in players:
        scores[player] = 0

    while max(scores.values()) < DEFAULT_WINNING_SCORE:
        for player in players:
            show_scores(scores)
            points = play_turn(player)
            scores[player] += points
            
            history.append(
                {
                  "turn": turn,
                  "player": player,
                  "score": scores[player],  
            
                }
            )
            turn += 1
            
            if scores[player] >= DEFAULT_WINNING_SCORE:
                break    

    winner = find_winner(scores)
    save_game(scores, winner)
    score_graph(history)

    print()
    print("=" * 40)
    print("\nGame over!")
    print("=" * 40)
    show_scores(scores)
    print()
    print(f"\nThe winner is {winner}!")
    print("Game results were saved to game_records.csv.")
    print("A score graph can be viewed in score_graph.png.")
    


if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    