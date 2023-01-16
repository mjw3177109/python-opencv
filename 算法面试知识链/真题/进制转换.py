
import sys






for line in sys.stdin:
    words= line.strip()
    try:
        changeres=int(words,16)
        if 1<=changeres<=2**31-1:
            print(changeres)
    except:
        break

