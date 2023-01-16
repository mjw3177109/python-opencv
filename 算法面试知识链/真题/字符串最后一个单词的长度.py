
import sys


def countWordNumber(words):
    if len(words ) <1:
        return "invaild words"
    if len(words) >= 5000:
        return "invaild words"
    finallword = words.split(" ")[-1].strip()
    print(len(finallword))
    return len(finallword)


if __name__ == '__main__':
    for line in sys.stdin:
        countWordNumber(line)




