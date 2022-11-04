def countletter(input):
    lettercount = 0
    for i in input:
        if i == " " or i == "?" or i == "!" or i == "." or i == "," or i == "'":
            pass
        else: lettercount += 1
    return lettercount

def countsentence(input):
    sentcount = 0
    for i in input:
        if i == "!":
            sentcount += 1
        elif i == ".": sentcount += 1
        elif i == "?": sentcount += 1
        else: pass
    return sentcount

def countword(input):
    wordcount = 0
    for i in input:
        if i == " ":
            wordcount += 1
        else: pass
    return wordcount + 1

text = input("The text?\n")


letters = countletter(text)

sents = countsentence(text)

words = countword(text)

L = (100 / words) * letters

S = (100 / words) * sents

index = (0.0588 * round(L)) - (0.296 * round(S)) - 15.8

print(round(index))


