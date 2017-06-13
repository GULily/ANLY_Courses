#!/usr/lib/env python35

# for more information about matplotlib, see:
# http://matplotlib.org/users/pyplot_tutorial.html

import numpy as np
import matplotlib.pyplot as plt
import ast

xpoints = [1, 2, 3]
filenames = ("quazyilx1", "quazyilx2", "quazyilx3")
run1 = []
run2 = []
run3 = []
run4 = []

with open("q2_results.txt", 'r') as f:
    for line in f:
        # if the first character is '{' parse it as a dictionary
        if line[0] == '{':
            entry = ast.literal_eval(line)
            # ASSUMPTION: there are 4 runs,
            # one with 1 master, 2 core nodes;
            # one with 1 master, 3 core nodes;
            # one with 1 master, 3 core nodes + 2 task nodes;
            # one with 1 master, 3 core nodes + 4 task nodes.
            if entry['nodes'] == 2:
                run1.append(entry['seconds'])
            if entry['nodes'] == 3:
                run2.append(entry['seconds'])
            if entry['nodes'] == 5:
                run3.append(entry['seconds'])
            if entry['nodes'] == 7:
                run4.append(entry['seconds'])

    run1_line = plt.plot(xpoints, run1, "rs-", label="run1 (2 core nodes)")
    run2_line = plt.plot(xpoints, run2, "bs-", label="run2 (3 core nodes)")
    run3_line = plt.plot(xpoints, run3, "gs-", label="run3 (3 core nodes + 2 task nodes)")
    run4_line = plt.plot(xpoints, run4, "ys-", label="run4 (3 core nodes + 4 task nodes)")
    plt.title("A comparision of four runs")
    plt.xticks(xpoints, filenames)
    plt.legend()

    # This would display locally:
    plt.show()
    # plt.savefig("q2_plot.png")
    # plt.savefig("q2_plot.pdf")




# question 5: bar chart plot
url = []
hit = []
with open("q5_results2.txt", 'r') as f:
    for line in f:
        line = line.rstrip()
        word = line.split()
        url.append(word[0])
        hit.append(int(word[1]))
    x = np.arange(len(url))
    plt.bar(x, hit)
    plt.title("A bar chart of the top 10 hits")
    plt.xlabel("url")
    plt.ylabel("hits")
    plt.legend()
    plt.show()
    # plt.savefig("q5_plot.png")
    # plt.savefig("q5_plot.pdf")
