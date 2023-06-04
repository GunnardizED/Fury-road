Road Crossing Game

This is a Python script that implements a road crossing game using the turtle module. The goal of the game is for the player to safely cross the road while avoiding moving cars. The game becomes progressively more challenging as the player advances levels.
Prerequisites

    Python 3.x
    turtle module

Installation

    Make sure you have Python 3.x installed on your system.
    No additional package installation is required.

Usage

    Save the script to a file with a .py extension (e.g., road_crossing_game.py).
    Run the script using the following command:

    python road_crossing_game.py

    The game window will appear.
    Use the Up and Down arrow keys to move the player up and down, respectively.
    The player's goal is to safely cross the road without being hit by the moving cars.
    As the game progresses, the cars will move faster and it will become more challenging to avoid them.
    If the player collides with a car, the game ends and a "Game Over" message is displayed.
    If the player successfully crosses the road and reaches the top, the level increases, and the player is placed back at the starting position.
    The game continues until the player is hit by a car.
    After the game ends, you can close the window by clicking on it.

Customization

You can customize the following aspects of the Road Crossing game:

    Window Size: Modify the width and height parameters in the screen.setup() line to change the dimensions of the game window.
    Player Controls: Update the screen.onkey() lines to assign different keys for player controls.
    Speed and Difficulty: Adjust the values in the time.sleep() and car_manager.speed_up() lines to change the game's speed and difficulty.
