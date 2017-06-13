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
            for word in words:
                if re.search("\[\d\d\/\w\w\w\/\d\d\d\d", word):
                    year = word[8:12]
                    mon = word[4:7]
                    month = "65536"
                    if mon == "Jan": month = "01"
                    elif mon == "Feb": month = "02"
                    elif mon == "Mar": month = "03"
                    elif mon == "Apr": month = "04"
                    elif mon == "May": month = "05"
                    elif mon == "Jun": month = "06"
                    elif mon == "Jul": month = "07"
                    elif mon == "Aug": month = "08"
                    elif mon == "Sep": month = "09"
                    elif mon == "Oct": month = "10"
                    elif mon == "Nov": month = "11"
                    elif mon == "Dec": month = "12"
                    print("Month:" + year + "-" + month + "\t" + "1")
    except EOFError:
        return None


if __name__ == "__main__":
    main(sys.argv)