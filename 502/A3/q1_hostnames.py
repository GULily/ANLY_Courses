#!/usr/bin/python3.4


from mrjob.job import MRJob
import re
from mrjob.protocol import TextProtocol

# WORD_RE = re.compile(r"\w.+")


class DistinctHostnames(MRJob):
    OUTPUT_PROTOCOL = TextProtocol

    def mapper(self, _, line):
        for word in line.strip().split(","):
            if re.search(r"^[a-z]+", word):
                yield word, 1

    def reducer(self, word, counts):
        yield word, str(sum(counts))


if __name__ == '__main__':
    DistinctHostnames.run()
