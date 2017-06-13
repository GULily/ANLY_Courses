#!/usr/bin/python3.4

from mrjob.job import MRJob
from mrjob.protocol import TextProtocol
import re
import statistics as stat
# WORD_RE = re.compile(r"\w.+")


class Links(MRJob):
    OUTPUT_PROTOCOL = TextProtocol

    def mapper(self, _, line):
        line = line.strip().split(",")
        for index, word in enumerate(line):
            hour = line[0][11:13]
            if re.fullmatch(r"3", word):  # if it has hop3
                timediff = int(line[index+3]) - int(line[index-1])
                yield hour, timediff

    def reducer(self, hour, values):
        valueList = []
        valueList.extend(values)
        if len(valueList) > 1:
            yield hour, str(stat.stdev(valueList))
        else:
            yield hour, "0"


if __name__ == '__main__':
    Links.run()
