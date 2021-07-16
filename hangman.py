word=input("type the word that you would like the other player to guess")

guess=""


for i in range(len(word)):
    if word[i].isalpha():
        guess+="_"
    else:
        guess+=word[i]

print(guess)

lives=10

while lives>0:
    if "_" not in guess:
        print("congrats! you have guessed the word!")
        break
    
    
    print(guess)
    letter=input("type in your guess here")
    if letter in word:
        newguess=""
        for i in range(len(word)):
            if letter==word[i]:
                newguess+=word[i]
            else:
                newguess+=guess[i]
        guess=newguess
    else:
        lives=lives-1
        print(f"that is not correct! please guess again. you have {lives} lives remaining.")
    
    if lives==0:
        print("game over!")
        break

