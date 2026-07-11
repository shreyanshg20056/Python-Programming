# die rolling game
import random
print("Welcome to the game of rolling the dice")
while True:
    choice = input("Press 'Enter' to roll the dice or 'q' to quit")
    if choice == 'q':
        print("Thanks for playing the game,bye!!")
        break
    elif choice == '':
        number = random.randint(1,6)
        print(f"Your number is {number}")
    else:
        print('Invalid Input!!')
print("Game Over")