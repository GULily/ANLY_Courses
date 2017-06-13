#!/usr/bin/python3.4

from mrjob.job import MRJob
import re
from mrjob.protocol import TextProtocol


class MultiHostnames(MRJob):
    OUTPUT_PROTOCOL = TextProtocol

    def mapper(self, _, line):
        line = line.strip().split(",")
        for index, word in enumerate(line):
            if re.search(r"\d+\.\d+\.\d+\.\d+", word):
                ip = word
                hostname = line[index-1]
                if re.search(r"^[a-z]+", hostname):
                    yield ip, hostname

    def reducer(self, ip, hostname):
        hostList = []
        hostList.extend(hostname)
        if len(set(hostList)) > 1:
            yield ip, str(set(hostList))


if __name__ == '__main__':
    MultiHostnames.run()
