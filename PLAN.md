### Tic Tac Toe Game

## Goal
This will be a Python implementation of a Tic Tac Toe game featuring PvP and PvAI gamemodes. The project will be implemented through TDD with pytest.
## Requirements
ID| Type | What it describes | How to verify
1 | Functional | The game contains a PVAI and a PVP mode | Must | Test a game vs EasyAi, and a game vs another opponent
2 | Functional | If the player selects PvE, the player will be prompted to select a difficulty | Must | Verify difficulty AI classes in ai.py
3 | Functional | Easy, Medium, and Hard AI will inherit from the same class structure, but choose_move will behave differently between the bots (Easy selects next available, medium will defend against wins, but otherwise select randomly, hard runs minimax) | Must | verifyable in AI.py. Run a game in easy, medium, and hard
4 | Non-Functional | First move is assigned randomly via coinflip (50% chance of X or O) | Could | test multiple games on a set seed. (Scrapped. Goes against the requirements)
5 | Functional | Given a player selects an illegal move, the game should reject their decision and prompt them to enter a new move | Must | Test an illegal move in the game loop
6 | Functional | Given a player selects a legal move, the game should accept their decision and handoff the turn to the opponent | Must | Test multiple Xs or Os aren't placed in subsequent turns
7 | Functional | Once a player has achieved 3 X's or O's in a row (on diagonal, vertical, or horizontal) the game will end | Must | Test a winning game condition
8 | Non-Functional | The AI at any level should not take more than 3000ms to make its turn | should | Test response time on maximum recursion depth with minimax
9 | Functional | The player can designate a board of any size at game creation | won't | Test boards with various sizes.
10 | Functional | HardAI never loses when it plays second | should | Play a significant amount of games and ensure that HardAI always wins.
11 | Functional | The game logic detects when a game has become a cats-game (tied) | Must | Test that tied game condition goes into effect during a cats game.

## Components

# Files
board.py - Contains the board class
ai.py - Contains the AI class
game.py - Turns, modes, draw/win checks
main.py - handles user input, prompts, and printing
tests/ - pytest suite
PLAN.md - Contains implementation plans, functional and non-functional requirements, repository structure, and decisions
README.md
.github/workflows/ci.yml

# Classes

AIAgent - contains the blueprint for AI difficulty levels
EasyAI - inherits from AIAgent, makes move choice based on first available cell
MediumAI - inherits from AIAgent, makes its move choice to defend against player wins (ex, if player has 2 x's in a row, medium AI will block the win) otherwise its selection is random
HardAI - inherits from AIAgent, makes its move choice off of minimax()

Board - the game board class. Determines valid/invalid moves, and contains the logic for placing moves, making a copy (for minimax), returning empty cells, and returning which cells are full.

## Decisions
Decided that variable board size is out of scope for this project. Requirements don't designate a particular board size, and it would be nice to have, but I'm sticking with a typical board size of 3 for this project.

Decided that, instead of creating separate AI classes for each difficulty, to instead create a parent AIAgent class that contains the blueprints for each AI difficulty class to inherit from.

## What Changed
I ended up abandoning the board of variable size requirements as it went against the rubric. I also decided to not implement a complicated mediumAI that would resist losing due to time constraints
