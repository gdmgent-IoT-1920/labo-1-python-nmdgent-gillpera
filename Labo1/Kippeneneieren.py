from random import randint

print("LINGO-BINGO Welkom bij het kip en eieren spel!")

randomNumber = randint(1000, 9999)
# print(randomNumber)

gekozenNummer = int(input("Geef een viercijferig nummer in:\n"))

pogingen = 1

def returnMatches(a,b):
       return list(set(a) & set(b))

while gekozenNummer != randomNumber:
    randomArray = [int(x) for x in str(randomNumber)]
    gekozenArray = [int(y) for y in str(gekozenNummer)]

    chicks = len([i for i, j in zip(randomArray, gekozenArray) if i == j])
    eggs = len(returnMatches(randomArray,gekozenArray)) - chicks


    if eggs < 0:
        eggs = 0
    
    print("U heeft " + str(chicks) + " kippen!")
    print("U heeft " + str(eggs) + " eieren!")

    gekozenNummer = int(input())
    pogingen += 1


print("\nGefeliciteerd! U heeft er " + str(pogingen) + " pogingen over gedaan.\n")