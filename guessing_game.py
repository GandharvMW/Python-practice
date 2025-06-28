import random

secret_number=random.randint(1,100)
attempts=0 




while True:
    guess=int(input("guess the number:"))
    attempts+=1
    if guess > secret_number:
        print("too high")

    elif guess < secret_number:
        print("too low")

    else:
        print(f"Congratulations you got it correct  in {attempts} attempts")
        break
    if attempts==10:
        print("game over!")
        print('play again!')
        break