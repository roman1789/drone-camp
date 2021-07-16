import random
bounds=False
while bounds==False:

    low=int(input("what lowest number you would like to guess from?"))
    high=int(input("what is the highest number you would like to geuss to?"))
    if low<high:
        bounds=True

random_number=random.randint(low,high)

wrong=True
while wrong==True:
    print(f"guess the number between {low} and {high}!")

    guess=int(input("type your guess here!"))

    if guess > random_number:
        print(f"{guess} is greater than the number i am thinking of!")
        if guess < high:
            high=guess

    elif guess < random_number:
        print(f"{guess} is less than the number i am thinking of!")
        if guess>low:
            low=guess

    else:
        print(f"congrats! {guess} is the number i was thinking of!")
        wrong=False

 