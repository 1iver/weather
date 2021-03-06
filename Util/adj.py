import numpy as np

idx2place = {
    0: "南京博物院",
    1: "江宁织造博物馆",
    2: "南京遇难者同胞纪念馆",
    3: "雨花台",
    4: "牛首山",
    5: "夫子庙",
    6: "中山陵",
    7: "总统府",
    8: "银杏湖乐园",
    9: "红山森林动物园",
}

place2idx = {
    "南京博物院":               0,
    "江宁织造博物馆":           1,
    "南京遇难者同胞纪念馆":      2,
    "雨花台":                  3,
    "牛首山":                  4,
    "夫子庙":                  5,
    "中山陵":                  6,
    "总统府":                  7,
    "银杏湖乐园":               8,
    "红山森林动物园":           9,
}

adj = [
    [0,17,16,19,8.3,7.8,11,20,16,25,23],
    [17,0,3.1,8,8.7,19,5.8,3.9,2.8,38,8.5],
    [16,3.1,0,5.6,7.7,19,3.3,6.9,0.4,37,9.1],
    [19,8,5.6,0,11,19,4.7,11,6,36,13],
    [8.3,8.7,7.7,11,0,12,5.3,12,8,30,15],
    [7.8,19,19,19,12,0,17,26,21,18,28],
    [11,5.8,3.3,4.7,5.3,17,0,8,3,36,11],
    [20,3.9,6.9,11,12,26,8,0,6.1,42,12],
    [16,2.8,0.4,6,8,21,3,6.1,0,37,9],
    [25,38,37,36,30,18,36,42,37,0,44],
    [23,8.5,9.1,13,15,28,11,12,9,44,0],

]

adj = np.array(adj)
print(adj)
print(idx2place)
print(place2idx)