import random
num=random.randint(1,100)
guesses=0
guess=-1
while(num!=guess):
    guesses+=1
    guess=int(input("guess a number:"))
    if guess==num:
        print(f"you have guessed the correct number {num} in {guesses} guesses")
        break
    elif guess>num:
        print("enter lower number please")
    else:
        print("enter higher number please")
