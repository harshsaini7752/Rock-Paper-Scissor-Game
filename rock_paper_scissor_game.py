import random
choices = ["r","p","s"]
emoji = {"r":"👊","p":"✋","s":"✌️"}
while True:
    user_choice = input("Rock ,Paper, Scissor(r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid Choice")
        continue
    computer_choice = random.choice(choices)

    print(f"you chose {emoji[user_choice]}")
    print(f"computer chose{emoji[computer_choice]}")

    if computer_choice == user_choice:
        print("Tie!")

    elif(computer_choice == "r" and user_choice == "p" or
          computer_choice == "p" and user_choice == "s" or
          computer_choice == "s" and user_choice == "r"):
        print("You win!")
    else:
        print("You lose")
    should_play = input("You play more game(y/n): ").lower()
    if should_play == "n":
        print("Thanks to play game")
        break
    else:
        continue