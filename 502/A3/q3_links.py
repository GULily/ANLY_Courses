#!/usr/bin/python3.4

from mrjob.job import MRJob
from mrjob.protocol import TextProtocol
import re
import statistics as stat
# WORD_RE = re.compile(r"\w.+")


class Links(MRJob):
    OUTPUT_PROTOCOL = TextProtocol

    def mapper(self, _, line):
        ip = []
        time = []
        line = line.strip().split(",")
        for index, word in enumerate(line):
            if re.search(r"\d+\.\d+\.\d+\.\d+", word):
                ip.append(word)
                time.append(line[index+1])

        for i in range(len(ip)):
            if i > 0:
                timediff = int(time[i]) - int(time[i - 1])
                # if int(time[i]) - int(time[i - 1]) > 0:
                #     timediff = int(time[i])-int(time[i - 1])
                # else:
                #     timediff = 0
                yield ip[i-1] + "->" + ip[i], timediff

    def reducer(self, link, values):
        valueList = []
        valueList.extend(values)
        if len(valueList) > 1:
            yield link, str(len(valueList)) + '\t' + str(stat.stdev(valueList))
        else:
            yield link, str(len(valueList)) + '\t' + "0"


if __name__ == '__main__':
    Links.run()
