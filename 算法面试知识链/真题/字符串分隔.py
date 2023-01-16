import sys

def splitWords(words):
    if len(words)>8:
        print(words[0:8])
        splitWords(words[8:])
    elif len(words)<=8:
        print(words+(8-len(words))*'0')





if __name__=="__main__":
    for line in sys.stdin:
        words =line.strip()
        try:
            splitWords(words)
        except:
            break