import random
computer = random.randint(0,2)

def winner(compter,player):
  if computer == player
    print("Its a draw.")
    return 0
  elif(comp == 0 and user ==1):
    print("Computer wins.")
    return -1
    
  elif(comp == 1 and user ==2):
    print("Computer wins.")
    return -1
    
  elif(comp == 2 and user == 0):
    print("Computer wins.")
    return -1

player = int(input("Enter 0 for snake, 1 for water and 2 for gun:"))

score = winner(computer,player)

print("You:", player)
print("Computer:",computer)

if(score == 0):
  print("Its a draw")
elif (score == -1):
  print("You Lose")
else:
  print("You Won")
