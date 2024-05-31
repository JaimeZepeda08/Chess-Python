# Chess

## Description

This is a game of Chess I coded in Python as my final project for _**AP CSP**_. You can play against a friend on the same device or against the computer, which uses the _Minimax_ algorithm. This app allows players to customize several things such as board color and even enable some special rules!

## Installation

To play the game, you need to have Python as well as the dependencies listed below installed on your computer.

1. **Install Python**: Download and install the latest version of Python from the official [Python website](https://www.python.org/downloads/).

2. **Install Dependencies**: Use `pip` to install the neccessary dependencies by running the following commands in your terminal or command prompt:

```
pip install pygame
pip install numpy
pip install pandas
```

## Running the Game

1. **Clone the Repository**: clone this repository to your local machine using the following command:

```
git clone https://github.com/JaimeZepeda08/Chess-Python.git
```

> OR download the project files from my [website](https://jaimezepeda.vercel.app/projects)

2. **Navigate to the Directory**: change to the directory containing the game code:

```
cd Chess
```

3. **Run the Game**: execute the main python file to play the game:

```
python3 main.py
```

## Game Features

### Single Player and Multiplayer

Users are able to choose between playing against a friend on the same device or against the computer by navigating to the settings tab and selecting the corresponding option.

### Board Customization

Users have the ability to choose between 4 different board color patterns: brown, black, blue, and green

### Special Rules

Besides the normal rules of chess, there are a couple optional ones I implemented:

#### Portals

If selected, two doors will appear on the board. If a player moves a piece to a tile with a door, it will be teleported to the other one. These doors get relocated after being used.

#### Danger Tiles

If selected, an exclamation mark will appear at a random tile at the start of every turn. If a player moves a piece to that position, it will be lost.
