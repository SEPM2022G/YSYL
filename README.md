# YSYL

You Stack You Lose, The project for Group G 2022

## Project Structure
All application code should be placed in `src/` and the test in `tests/` where
the test file is prefixed with `test_...`. Example:

```
src/StateValidator/state.py
tests/test_state.py
```

## Installing the environment
This repo uses [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html)
for handling virtual environments. If you are using a command line version of
conda, use the environment.yml file to create an environment with `conda env
create -f environment.yml` and activate the environment with `conda activate
ysyl`.

## Contributing

All changes to the main branch are made through pull requests on GitHub. In
order to contribute, create a branch with your changes and submit a pull request
to `main`. Include a title that refers to the task in trello together with a
description of your changes to help reviewers understand your changes.

```
Feature: Save a state in the statemanager

Added a function to save a new state in the statemanager component. 
```

**Important** Never commit and push directly to the main branch!

When naming branches start off with a "tag" describing what kind of changes the
branch includes (feature, fix, hotfix, etc..) and follow with a
description of what you are working on. It is also a good idea to mention what
part of the system the changes are related to if it helps identifying the purpose
of the branch. The branch naming convention exists to make it easier figuring
out what a branch contains and to force the author to keep his/her changes
coherent with the naming. Try to avoid being overly specific to keep the names
to a reasonable length, common sense is more important than any convention!

```
feat-validator
feat-savestate
feat-io-processfile
fix-validator
hotfix-imports
feat-alphabetapruning

```

All changes should be reviewed by a minimum of `1` other person after submitting
a pull request to ensure that other members can weigh in on the changes. Try to
avoid having people that are involved with the changes review their own pull
request, even if this is tempting.

When merging pull requests we `Squash and merge` to the main branch. Squashing
combines all the commits in the pull request and allows us to use our own format
for individual commits on individual branches and still keep the history of the
main branch in a coherent format.

## Reviewing
When reviewing a pull request, make sure that it meets the most important
guidelines before merging:

- Is the feature/fix well defined and only solve a single or narrow group of
problems?

- Are tests written?

- No magic constants, misleading variable names etc..

- Are the changes in the correct component?

Here are some more detailed checks: 
[PR checklist](https://devchecklists.com/pull-requests-checklist/)

## Using the AI
The AI is run in a separate process in order to not block the UI.
```
Usage: python -m src.GameEngine.GameAI [OPTION] [INPUT FILE] [OUTPUT FILE]
Options:
	--diff= : a difficulty level from 1 to 3
	--color= : the color for the AI (black or white)
	--config= : the file path to a config
```

Write a move to the input file and the AI will return the following in the
output:
* Outcome from input move as a number 
	* 0 = invalid move
	* 1 = valid move
	* 2 = White wins
	* 3 = Black wins
* Id, an unique identifier for each move to help avoid reading duplicates
* The move, see below for an example

```
{
    "outcome": 1,
    "id": "09f1b621-7b60-4696-865f-9f4fa119a1e6",
    "move": {...}
}
```


### Format of a move 

* Source
    * Is it from the pile?
    * Position
* Destination
    * Position
    * Orientation of the piece at the top as a number (0 = flat | 1 = standing)
* The amount of pieces
* Color of the player as a number (0 = white | 1 = black)
* Is it the first turn in the game?

### Example of a move input
```
{
    "src": {
        "pile": true,
        "pos_x": 0,
        "pos_y": 0,
    },
    "des": {
        "pos_x": 0,
        "pos_y": 0,
        "orientation": 0
    },
    "pieces": 1,
    "color": 0,
    "first_turn": false
}
```

### Config
A path to a config can be passed as an argument which will overwrite any inputed
options, the config can be used to change any values after the game is started
by changing the corresponding fields.

Currently there is the following options:

```
{
	difficulty: 1
}
```

### Format of the board
```
[[[0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]]

 [[0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]]

 [[0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]]

 [[0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]]

 [[0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]]]

shape(x = 5, y = 5, z = 42)

The maximum pieces in a stack is 42
