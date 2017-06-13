#!/usr/bin/env python34

#
# Placeholder
#
import sys

def main(argv):
    try:
        oldWord   = None
        oldSum    = 0
        for line in sys.stdin:
            (key,value) = line.rstrip().split('\t')
            if key.startswith("URL:"):
                word = key[4:]
                if word!=oldWord:
                    if oldSum > 200000:
                        print("{} {}".format(oldWord,oldSum))
                    oldWord = word
                    oldSum  = 0
                oldSum += int(value)
    except EOFError:
        pass
    if oldSum > 200000:
        print("{}: {}".format(oldWord,oldSum))
    return None

if __name__ == "__main__":
    main(sys.argv)