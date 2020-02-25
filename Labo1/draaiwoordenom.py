zin = input("Geef een zin in:\n")

def omkeren(input):
    splitWords = input.split(" ")
    splitWords = splitWords[::-1]

    output =' '.join(splitWords)

    return output

print(omkeren(zin))