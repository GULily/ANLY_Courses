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
            if key.startswith("Month:"):
                word = key[6:]
                if word!=oldWord:
                    if oldWord:
                        print("{} {}".format(oldWord,oldSum))
                    oldWord = word
                    oldSum  = 0
                oldSum += int(value)
    except EOFError:
        pass
    if oldWord:
        print("{} {}".format(oldWord,oldSum))
    return None

if __name__ == "__main__":
    main(sys.argv)