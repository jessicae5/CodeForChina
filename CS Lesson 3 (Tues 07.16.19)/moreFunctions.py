


# 1
# 2
# 3
# 4
# 5



import random

def printLowToHigh(a, b):
    for i in range(a, b + 1):
        print(i)

    # for i in range(b - a + 1):
    #     print(a + i)

def getRandomNumber(low, high):
    print("get random number is called")
    value = random.randint(low, high)
    return value

def addValues(x, y, z):
    theSum = x + y + z
    return theSum * theSum

def main():

    low = 10
    high = 100
    # randomValue = getRandomNumber(low, high)

    # printLowToHigh(10, 15)

    answer = addValues(10, 30, 12)
    print(answer)

    # print(addValues(10, 30, 12))

if __name__ == "__main__":
    main()