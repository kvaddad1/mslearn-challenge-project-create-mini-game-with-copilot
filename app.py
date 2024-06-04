import random

# Initialize a rock, paper, scissors game where the player can play against the computer; Define the choices available: rock, paper, scissors; Prompt the player to enter their choice from rock, paper, or scissors and convert it to lowercase to handle case insensitivity; Check if the user's input is valid. If not, prompt the user again until a valid choice is made; Let the computer randomly select its choice from rock, paper, or scissors; Compare the player's and computer's choices according to the rules: Rock beats scissors, scissors beat paper, and paper beats rock; Announce the result of the round: win, lose, or tie; Ask the player if they want to play another round. If yes, repeat the game; otherwise, end the game; Display the final scores after the game ends.
choices = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0

while True:
    # Prompt the player for their choice
    player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    # Check if the player's input is valid
    if player_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    # Let the computer randomly select its choice
    computer_choice = random.choice(choices)

    # Compare the player's and computer's choices
    if player_choice == computer_choice:
        result = "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        result = "win"
        player_score += 1
    else:
        result = "lose"
        computer_score += 1

    # Announce the result of the round
    print(f"You chose {player_choice}. The computer chose {computer_choice}. You {result}!")

    # Ask the player if they want to play another round
    play_again = input("Do you want to play another round? (yes/no): ").lower()
    if play_again != "yes":
        break

# Display the final scores
print(f"Final scores: Player {player_score} - Computer {computer_score}")