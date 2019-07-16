import random



def getRandomNumber(low, high):
    randomNumber = random.randint(low, high)
    print(randomNumber)

def main():

    low = 30
    high = 100
    getRandomNumber(low, high)

if __name__ == "__main__":
    main()