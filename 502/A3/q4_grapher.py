#!/usr/lib/env python35

import matplotlib.pyplot as plt

hour = []
stdev = []
with open("q4_hop23.txt", 'r') as f:
    for line in f:
        line = line.rstrip()
        word = line.split()
        hour.append(int(word[0]))
        stdev.append(float(word[1]))
    # x = np.arange(len(hour))
    plt.plot(hour, stdev)
    plt.title("A bar chart of the standard deviation in a day")
    plt.xticks(hour)
    plt.xlabel("hour")
    plt.ylabel("stdev")
    plt.legend()
    plt.show()
    # plt.savefig("q4_graph.png")
    # plt.savefig("q4_graph.pdf")
