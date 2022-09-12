import random
YourMom = True
listOfResponses = ("It is Certain", "Yes", "Maybe?", "You may rely on it", "Ask again later", "Are you kidding", "FACT", "umm, I think so")

UserInput = input("Ask me a question ").lower()
while YourMom: 
    if UserInput == "no":
        confirmInput = input("You sure you want to quit??: ")
        if confirmInput == "yes":
            print("Okay Bye")
            YourMom = False
            
        

    else:
        print(random.choice(listOfResponses))
        UserInput = input("Ask me a question ").lower()
