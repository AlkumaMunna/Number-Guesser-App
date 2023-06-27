import random
correct_answer = random.randint(1,50)

for i in range(5):
    user_input = int(input("Chance left {} \nGuess a number between 1 to 50: ".format(5-i)))

    if user_input < correct_answer and i<4:
        print("Correct answer is greater!")
    elif user_input > correct_answer and i<4:
        print("Correct answer is smaller!")
    elif user_input == correct_answer:
        print("You Win!")
        break
    else:
        print("You lose!")
        break


