# Computer Vision RPS
For this project we will be creating a version of the classic game of rock, paper, scissors using computer vision models to identify the users choice through their webcam.

# Milestone 2
To start we created a github environment and used teachable machine to create a model.
* Were using a Keras model identify different hand positions for the game.
* This is stored in the keras_model.h5 and labels.txt files.

# Milestone 3
I created a requirements.txt file based on the dependencies of the conda environment through pip.

# Milestone 4
I create a new file called 'manual_rps.py' which simulates a game of rock paper scissors using python functions.
* This imports the 'random' module to generate the computers choice from a list of options using the get_computer_choice(options) function.
* There is a get_user_choice() function which prompts the user for an input of either Rock, Paper, or Scissors.
* The get_winner function then compares these choices and declares a winner.
* The game is initiated by a play() function, which wraps these previous functions together.