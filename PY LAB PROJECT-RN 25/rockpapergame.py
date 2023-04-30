import time

print("Welcome to the game \n")
time.sleep(1)

t1 = time.time()

player1_choice = input("Player 1, please choose rock, paper, or scissor: ")
time.sleep(.5)
player2_choice = input("Player 2, please choose rock, paper, or scissor: ")

time.sleep(1)

print("\nCalculating results...\n")
time.sleep(2)

if (player1_choice == "rock" and player2_choice == "scissor") or (player1_choice == "paper" and player2_choice == "rock") or (player1_choice == "scissor" and player2_choice == "paper"):
  print("Player 1 wins!")
elif (player1_choice == player2_choice):
  print("It's a tie!")
else:
  print("Player 2 wins!")