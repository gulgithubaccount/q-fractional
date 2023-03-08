import numpy as np


def dis(patterns, unknown_pattern):
    """
    patterns = [
        P1 = [[1,2],[3,4],...,[]],
        P2 = [[],[],...,[]],
        ...
        Pn = [[],[],...,[]],
    ]

    unknown pattern = [[1,2],[3,4],...,[]]
    """
    l = len(patterns)
    dis = np.zeros((l))

    for i in range(l):
        temp = 0
        for j in range(len(unknown_pattern)):
            temp += patterns[i][j][0] * np.log(
                patterns[i][j][0] / (1 / 2 * (patterns[i][j][0] + unknown_pattern[j][0])))
            + patterns[i][j][1] * np.log(patterns[i][j][1] / (1 / 2 * (patterns[i][j][1] + unknown_pattern[j][1])))
            + unknown_pattern[j][0] * np.log(
                unknown_pattern[j][0] / (1 / 2 * (patterns[i][j][0] + unknown_pattern[j][0])))
            + unknown_pattern[j][1] * np.log(
                unknown_pattern[j][1] / (1 / 2 * (patterns[i][j][1] + unknown_pattern[j][1])))
        dis[i] = temp
    return dis


def switch(pattern, beta):
    """
    switch from a q-fractional fuzzy set to a T2FS
    """
    for i in range(len(pattern)):
        temp = pattern[i][0]
        pattern[i][0] = pattern[i][0] - beta * (1 - (pattern[i][0] + pattern[i][1]) / 2)
        pattern[i][1] = pattern[i][1] - beta * (1 - (temp + pattern[i][1]) / 2)

    return pattern

# Example 1
patterns = [
    [[1,1], [1, 0.5], [0.8, 1]],
    [[0.8, 1], [1, 0.7], [0.8, 1]],
    [[0.9, 1], [0.7, 1], [1, 1]]
]
unknown_pattern = [[0.5, 1], [1, 1], [1, 0.7]]

print("----------------Distances for the raw data-------------------")
distances = dis(patterns, unknown_pattern)
print(distances)
print("----------------Distances for the raw data-------------------")

for j in range(len(patterns)):
    patterns[j] = switch(patterns[j], 1).copy()

unknown_pattern_switched = switch(unknown_pattern, 1)

print("----------------Distances for the switched data-------------------")
print(dis(patterns, unknown_pattern))
print("----------------Distances for the switched data-------------------")

print("----------------Switched patterns-------------------")
print(patterns)
print("----------------Switched patterns-------------------")

print("----------------Switched unknown patterns-------------------")
print(unknown_pattern)
print("----------------Switched unknown patterns-------------------")

