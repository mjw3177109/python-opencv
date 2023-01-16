import random
import sys


def removeDuplicateAndSort(newlist):
    #     newset=set()
    #     for i in range(number):
    #         randomNumber= random.randint(1,500)
    #         print(randomNumber)
    #         newset.add(randomNumber)

    # newlist=list(newset)
    newlist.sort()
    for h in newlist:
        print(h)


if __name__ == "__main__":
    number = int(float(input()))
    newset = set()
    if number < 1 or number > 1000:
        print("invaid number")
    else:
        for line in sys.stdin:
            randnumber = int(float(line))
            if 1 <= randnumber <= 500:
                newset.add(randnumber)

        newlist = list(newset)
        removeDuplicateAndSort(newlist)