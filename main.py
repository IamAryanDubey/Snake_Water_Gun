import random

def winner(computer, player):
    if computer == player:
        print("It's a draw.")
        return 0
    elif (computer == 0 and player == 1) or (computer == 1 and player == 2) or (computer == 2 and player == 0):
        print("You win!")
        return 1
    else:
        print("Computer wins.")
        return -1

player_score = 0
computer_score = 0

for round in range(10):
    computer = random.randint(0, 2)
    player = int(input("Enter 0 for snake, 1 for water, and 2 for gun: "))

    score = winner(computer, player)
    
    print("You:", player)
    print("Computer:", computer)

    if score == 1:
        player_score += 1
    elif score == -1:
        computer_score += 1

    print(f"Score after round {round + 1}: Player {player_score} & Computer {computer_score}\n")

print("Final Score:")
print(f"Player: {player_score}")
print(f"Computer: {computer_score}")

if player_score > computer_score:
    print("You won the game!")
elif player_score < computer_score:
    print("Computer won the game!")
else:
    print("The game is a draw!")
