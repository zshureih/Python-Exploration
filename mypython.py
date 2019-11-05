# Zeyad Shureih

# mypython.py creates three files with ten random characters
# then 2 random numbers (1-42) and the product of the two numbers

import string
import random

def main():

    fileNames = ["abcdefg", "hungryHippos", "statistical mechanics of learning"]

    for i in range(0, 3):
        print(fileNames[i])
        f = open(fileNames[i], "w")

        # write 10 random letters
        randomLetters = [] 
        for j in range(0, 10):
            if j == len(randomLetters) - 1:
                randomLetters.append('\n')
            else:
                randomLetters.append(random.choice(string.ascii_lowercase))
            f.write(randomLetters[j])    
                
        f.close()
    
    randomNums = [random.randint(1, 42), random.randint(1, 42)]
    print(randomNums[0])
    print(randomNums[1])
    print(randomNums[0]*randomNums[1])