import sys

def countNumberOfChar(strs, char):
    if len(strs) < 1 or len(strs) > 1000:
        print("your words is over the range")
        return "invalid words"
    number = 0
    for i in strs:
        if i == char:
            number += 1

    print(number)


if __name__ == "__main__":
    strs = str(input()).upper()
    char = input().upper()
    #print(strs.count(char))
    countNumberOfChar(strs, char)





