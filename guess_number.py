Actual_number=20
guess=int(input("guess the number: "))
turns=0
No_of_turns=3
while guess != Actual_number and turns < No_of_turns:
    print("wrong guess!!")
    turns+=1
    guess=int(input("guess the number: "))
if guess == Actual_number:
    print("Congratulations! You guessed the number.")
else:
    print("Sorry, that's not the correct number.")