import random

def generateOTP(length):

    characters = "0123456789"
    n = len(characters)

    oneTImePassword = ""

    for i in range(1, length+1):
        oneTImePassword += characters[int(random.random()*10) % n]

    return oneTImePassword

if __name__ == '__main__':
    length = 6
    print("Your OTP is - ", generateOTP(length))