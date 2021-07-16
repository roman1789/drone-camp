name=input("What is your name?")

old_age=int(input("what age do you want to calculate from?"))

age=int(input("how old are you right now?"))

years_until_age= old_age - age
if age<old_age:
    print(f"{name} has {years_until_age} years until he is {old_age} years old")

elif age>old_age:
    years_until_age = (old_age - age) *-1
    print(f"{name} is {years_until_age} over {old_age}")

else:
    print(f"you are {old_age}!")
