# Program: Tuple Out Dice Game
# Muatasim Miller

INST 126 Final Project

Welcome to Tuple Out!

Tuple Out is a dice game where players roll three dice and try to score points without tupling out. 

The game runs in the terminal and lets the user choose between Singleplayer and Multiplayer mode.

## What You Need Before Playing

This game uses a few Python libraries for dice rolling, saving data, and making the score graph.

Before playing for the first time, install the required libraries:

```bash
pip install -r requirements.txt
```

Then start the game with:

```bash
python tuple_out.py
```

If that does not work on your computer, try:

```bash
py tuple_out.py
```

## Starting the Game

When the game starts, you will see a menu:

```text
1 - Singleplayer
2 - Multiplayer
```

Type `1` to play Singleplayer.

Type `2` to play Multiplayer.

After choosing the mode, the game will ask for the player name or names.


## Playing Again

After a game ends, the program asks if you want to play again.

Type `Y` to return to the game mode menu.

Type `N` to quit the game.


## Singleplayer Mode

Singleplayer mode is for one player.

The goal is to get the highest score you can in 5 turns.

If this is the first time the game is being played, there will not be a saved high score yet. The game will create one after the first Singleplayer game.

After that, each new Singleplayer game gives the player a chance to beat the saved high score.

## Multiplayer Mode

Multiplayer mode is for two players.

Each player enters their name. Players then take turns rolling dice until one player reaches 50 points.

The first player to reach 50 points wins.

## How a Turn Works

Each turn starts with the player rolling three dice.

The player can then choose:

```text
S - Stop
R - Reroll
```

### If you stop

The dice are added together, and that number is added to your total score.

Example:

```text
[3, 5, 6]
```

This would give the player 14 points for that turn.

### If you reroll

The game rerolls the dice that are not fixed.

### Fixed dice

If two dice have the same number, those dice are fixed. Fixed dice cannot be rerolled for the rest of that turn.

Example:

```text
[2, 5, 5]
```

The two 5s are fixed. The player can only reroll the 2.

### Tupling Out

If all three dice have the same number, the player tuples out.

Example:

```text
[4, 4, 4]
```

If this happens, the player scores 0 points for that turn, and the turn ends.

## Files the Game Creates

The game may create these files while it runs:

```text
game_records.csv
score_graph.png
high_score.csv
```

### game_records.csv

This file saves the final scores from games that have been played.

### score_graph.png

This file shows a graph of how the score changed during the game.

### high_score.csv

This file saves the best Singleplayer score.

These files are created by the program. You do not need to edit them yourself.

## What This Game Can Do

This program can:

- run a Singleplayer game
- save and compare a Singleplayer high score
- run a two-player Multiplayer game
- roll dice using random number generation
- keep track of player scores
- save game results to a CSV file
- create a graph of score progress

## Current Limits

This version only supports:

- one player in Singleplayer mode
- two players in Multiplayer mode
- a 5-turn Singleplayer game
- a 50-point winning score in Multiplayer mode

The game is played fully in the terminal.