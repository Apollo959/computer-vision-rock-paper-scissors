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


# Milestone 5
The 'camera_rps.py' file is the latest version of the rps game, this has multiple new features which allow the user to seamlessly play the game until they or the computer get 3 wins in total.

## Player & Computer Choice Functions
There are two functions that contribute towards determining the players choices.
The below picks a random choice from the options list object.

        get_computer_choice(options)


The next function converts the numeric values from the computer vision prediction into a choice: 

        get_prediction(prediction)

This returns the following depending on what is predicted:
* Rock
* Paper
* Scissors
* Neutral (if nothing is shown)

## Game Logic Functions
This section has 3 functions, the first determines the winner based on both players choices and can be called like this:

        get_winner(computer_choice, human_choice)

A winner will be announced in the console, and one of the following options will be returned based on the result.

The final function is to start one round of the game which contains all the logic for initiating the computer vision system. It starts a 5 second timer while the camera is running so the user can make a decision at the correct time, and then returns the winner of the round. It does not take any arguments.

        game_round()

Both of these functions return the following based on who won that particular rouund
* user
* computer
* none

This output is then used in the final stage of the script which is added to continue the game at the users page until a player has won 3 times.

        while True:
            print("Starting Round:")
            winner = game_round()
            if winner == "user":
                user_wins = user_wins + 1
                print(f"User has {user_wins} wins")
            elif winner == "computer":
                computer_wins = computer_wins + 1
                print(f"Computer has {computer_wins} wins")
            if computer_wins == 3:
                print("GAME OVER: COMPUTER WON 3 GAMES")
                break
            if user_wins == 3:
                print("CONGRATULATIONS: HUMAN WON 3 GAMES")
                break
            input("Press Enter to continue...")

At the end of each round the user is prompted to hit enter to continue to the next round until the game is over.