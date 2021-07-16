name=input("what is your name?")

age=int(input("how old are you?"))

yearstoage=age-30

if age>30:
    yearstoage=age-30
    print(f"You are {yearstoage}from 30!")


elif age<30:
    yearstoage=30-age
    print(f"You are {yearstoage} from 30!")

else:
    print("You are 30!")