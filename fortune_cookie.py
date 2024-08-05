import random


#This simple program emulates a fortune cookie🍪
def fortune_cookie():
    cookie = random.randint(1, 8)

    if cookie == 1:
        print("Don't pursue happiness – create it.")
    elif cookie == 2:
        print("All things are difficult before they are easy.")
    elif cookie == 3:
        print("The early bird gets the worm, but the second mouse gets the cheese.")
    elif cookie == 4:
        print("Someone in your life needs a letter from you.")
    elif cookie == 5:
        print("Don't just think. Act!")
    elif cookie == 6:
        print("Your heart will skip a beat.")
    elif cookie == 7:
        print("The fortune you search for is in another cookie.")
    elif cookie == 8:
        print("Help! I'm being held prisoner in a Chinese bakery!")


fortune_cookie()
fortune_cookie()
fortune_cookie()
