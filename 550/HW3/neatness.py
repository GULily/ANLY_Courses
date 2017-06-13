def solveWordWrap(l, W, M):
    # n is the size of the list of words
    n = len(l)

    # the number of extra spaces for words from i to j in one line
    extras = [[float('Inf') for i in range(n)] for j in range(n)]
    for i in range(n):
        extras[i][i] = M - l[i]
        for j in range(i+1, n):
            extras[i][j] = extras[i][j-1] - l[j] - 1

    # the cost for words from i to j in a one line
    lc = [[float('Inf') for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i, n):
            if extras[i][j] < 0:
                lc[i][j] = float('Inf')
            elif j == n-1 and extras[i][j] >= 0:
                lc[i][j] = 0
            else:
                lc[i][j] = extras[i][j] ** 3

    # c[j] is the optimized total cost for arranging words from 1 to j
    c = [float('Inf') for i in range(n)]
    start_word = [0 for i in range(n)]
    end_word = [0 for i in range(n)]
    for j in range(n):
        c[j] = lc[0][j]  # update
        end_word[j] = j
        for i in range(j):
            if c[i] + lc[i+1][j] < c[j]:
                c[j] = c[i] + lc[i+1][j]  # update
                # print(c[j], i+1, j)
                start_word[j] = i+1
                end_word[j] = j
    # print("start word:", start_word)
    # print("end word  :", end_word)
    # print("cost:", list(c))
    # print(list(lc))
    # print(list(extras))

    # work backward from start_word and end_word to find
    # the start and end word for each line of the optimal solution
    start = []
    end = []
    start.append(start_word[-1])
    end.append(end_word[-1])
    while start[-1] != 0:
        for index, i in enumerate(end_word):
            if i == start[-1] - 1:
                end.append(i)
                start.append(start_word[index])
    # print("start:", start)
    # print("end  :", end)

    for i in range(len(start)-1, -1, -1):
        s = start[i]
        e = end[i]
        for w in range(s, e + 1):
            print(W[w], end=" ")
        print()

    return print("\nM:",M, "\nPenalty of the optimal solution:", c[-1], "\n")

# simple test
# text = "AAA BB CC ddddd AAA BB CC ddddd"
# text = text.split(" ")
# L=[]
# W=[]
# for index, word in enumerate(text):
#     L.append(len(word))
#     W.append(word)
#     print(index, W[index], L[index])
#
# M = 12
# solveWordWrap(L, W, M)



text = "Buffy the Vampire Slayer fans are sure to get their fix with the DVD release of the show's first season. " \
       "The three-disc collection includes all 12 episodes as well as many extras. There is a collection of interviews " \
       "by the show's creator Joss Whedon in which he explains his inspiration for the show as well as comments on the " \
       "various cast members. Much of the same material is covered in more depth with Whedon's commentary track for the " \
       "show's first two episodes that make up the Buffy the Vampire Slayer pilot. The most interesting points of Whedon's " \
       "commentary come from his explanation of the learning curve he encountered shifting from blockbuster films like Toy " \
       "Story to a much lower-budget television series. The first disc also includes a short interview with David Boreanaz " \
       "who plays the role of Angel. Other features include the script for the pilot episodes, a trailer, a large photo gallery " \
       "of publicity shots and in-depth biographies of Whedon and several of the show's stars, including Sarah Michelle Gellar, " \
       "Alyson Hannigan and Nicholas Brendon."
text = text.split(" ")
L=[]
W=[]
for index, word in enumerate(text):
    L.append(len(word))
    W.append(word)
    # print(index, word, L[index])

M = 40
solveWordWrap(L, W, M)

M = 72
solveWordWrap(L, W, M)

