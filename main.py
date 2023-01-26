from random import randint
import time

rps = ["Rock", "Paper", "Scissors"]
computer = rps[randint(0, 2)]

choice = (input("a. Rock, b. Paper, c. Scissors. Chose your choice(enter the letter only): "))

computer_score = 0
player_score = 0
player = False

while player == False:
  if choice == "a" and computer == 1:
    print("Paper covers rock. You lose!")
    print(computer)
    computer_score + 1
    print("computer score = ", computer_score)
  elif choice == "a" and computer == 2:
    print("Rock crushes scissors. You win!")
    print(computer)
    player_score + 1
    print("your score = ", player_score)
  elif choice == "b" and computer == 0:
    print("Paper covers rock. You win!")
    print(computer)
    player_score + 1
    print("your score = ", player_score)
  elif choice == "b" and computer == 2:
    print("Scissors cut paper. You lose!")
    print(computer)
    computer_score + 1
    print("computer score =", computer_score)
  elif choice == "c" and computer == 0:
    print("Rock crushes scissors. You lose!")
    print(computer)
    computer_score +1
    print("computer score =", computer_score)
  elif choice == "c" and computer == 1:
    print("Scissors cut paper. You win!")
    print(computer)
    player_score + 1
    print("your score = ", player_score)
  elif choice == "a" and computer == 0:
    print("It's a tie! Play again.")
    print(computer)
    rps = ["Rock", "Paper", "Scissors"]
    computer = (randint[0, 2]) 
    choice = (input("a. Rock, b. Paper, c. Scissors. Chose your choice(enter the letter only): "))
  elif choice == "b" and computer == 1:
    print("It's a tie! Play again.")
    print(computer)
    rps = ["Rock", "Paper", "Scissors"]
    computer = (randint[0, 2]) 
    choice = (input("a. Rock, b. Paper, c. Scissors. Chose your choice(enter the letter only): "))
  elif choice == "c" and computer == 2:
    print("It's a tie! Play again.")
    print(computer)
    rps = ["Rock", "Paper", "Scissors"]
    computer = (randint[0, 2]) 
    choice = (input("a. Rock, b. Paper, c. Scissors. Chose your choice(enter the letter only): "))


    