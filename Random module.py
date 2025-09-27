import random

#exercise 1
print("Guess the number")
number_random=random.randint(1, 20)
user=int(input("guess the number" ))

if user == number_random :
    print("You guessed it! ")
elif user> number_random :
    print("Too high")
elif user< number_random :
    print("Too low")
else:
    print("Unknown")

#exercise 2
items =["apple","banana","cherry","orange"]
fruit=random.choice(items)

guess=input("chosse the fruit ")

if guess ==fruit :
    print("correct")
else:
    print("wrong")

#exercise 3
pick=["rock","paper","scissors"]
user_guess=input("chosse the right one ").lower()
computer=random.choice(pick)
if user_guess ==computer :
    print("it's a draw")
elif user_guess =="rock" and computer =="scissors":
    print("you win")
elif user_guess =="scissors" and computer =="paper":
    print("you win")
elif user_guess =="paper" and computer =="rock":
    print("you win")
else :
    print("you lose")

