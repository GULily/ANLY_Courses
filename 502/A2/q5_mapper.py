#!/usr/bin/env python34

#
# Placeholder
#
import sys
import re

def main(argv):
    try:
        for line in sys.stdin:
            line = line.rstrip()
            words = line.split()
            for index, word in enumerate(words):
                if re.search("\[\d\d\/\w\w\w\/\d\d\d\d", word):
                    url = words[index+3]
                    print("URL:" + url + "\t" + "1")
    except EOFError:
        return None


if __name__ == "__main__":
    main(sys.argv)