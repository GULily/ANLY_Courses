#!/usr/bin/python3.4
#
# Template to compute the number of distinct IP addresses 
#

from mrjob.job import MRJob
import re
from mrjob.protocol import TextProtocol

# WORD_RE = re.compile(r"\d+\.\d+\.\d+\.\d+")


class DistinctIPAddresses(MRJob):
    OUTPUT_PROTOCOL = TextProtocol

    def mapper(self, _, line):
        for word in line.strip().split(","):
            if re.search(r"\d+\.\d+\.\d+\.\d+", word):
                yield word, 1

    def reducer(self, word, counts):
        yield word, str(sum(counts))


if __name__ == '__main__':
    DistinctIPAddresses.run()
