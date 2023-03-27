def countLetter(text, targetChar):
    letterCount = 0
    for eachChar in text:
        if eachChar == targetChar:
            letterCount += 1
    return letterCount

print(countLetter('danny', 'n'))