def getCount(inputStr):
    num_vowels = 0
    for a in inputStr.lower():
        if a in "aeiou":
            num_vowels +=1
    
    return num_vowels

print(getCount("consider"))