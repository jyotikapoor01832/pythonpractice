import random
target=random.randint(1,100)
                       
while True:
    Userchoice=input("Guess the target: or quit :")
    if (Userchoice=="quit"):
        break

    Userchoice=int(Userchoice)
    if Userchoice==target:
        print("Success: Correct Guess!!")
        break
    elif Userchoice>target:
        print("Number is too big.Choose a smaller guess..")
    else:
        print("Number is too small. Choose a bigger guess..")