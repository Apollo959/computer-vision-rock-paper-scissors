import cv2
from keras.models import load_model
import numpy as np
import random
import time

# Determine player choices
def get_computer_choice(options):
    """Picks a random choice for the computer player"""
    options = ["Rock","Paper","Scissors"]
    return random.choice(options)

def get_prediction(prediction):
    """Converts the keras model prediction value into the corrosponding choice, or Neutral if none were detected"""
    prediction_max_index = prediction[0].argmax(axis=0)
    labels = ["Neautral","Rock","Paper","Scissors"]
    result = labels[prediction_max_index]
    return result

# Game logic
def get_winner(human_choice):
    """Compares the results of each players choice then prints and returns the winner"""
    computer_choice = get_computer_choice()
    print(f"Computer picked {computer_choice}")
    if computer_choice == human_choice:
        print("It's a draw!")
        return "none"
    elif human_choice == "Neautral":
        print("Couldn't determine humans choice")
        return "none"
    elif computer_choice == "Rock" and human_choice == "Scissors" or computer_choice == "Scissors" and human_choice == "Paper" or computer_choice == "Paper" and human_choice == "Rock":
        print(f"{computer_choice} beats {human_choice}: COMPUTER WINS!")
        return "computer"
    else:
        print(f"{human_choice} beats {computer_choice}: HUMAN WINS!")
        return "user"

def game_round():
    """Initializes a single game of rps, including the camera prediction, countdown, and game winner"""
    model = load_model('keras_model.h5', compile=False)
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    start_time = time.time()
    max_time = 5
    time_counter = 0
    while True:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data, verbose = 0)
        cv2.imshow('frame', frame)
        # Start of timer
        time_passed = time.time() - start_time
        if time_passed > time_counter:
            time_counter = time_counter + 1
            print((max_time - time_counter) + 1) 
        if time_passed > max_time:
            # Game starts
            human_choice = get_prediction(prediction)
            winner = get_winner(human_choice)
            return winner
        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

#score tracking
computer_wins = 0
user_wins = 0

# Play three games
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