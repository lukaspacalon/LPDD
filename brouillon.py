import os
# a = [[0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0],
#      [0, 2, 2, 1, 1, 0],
#      [0, 2, 1, 1, 1, 0],
#      [0, 2, 1, 1, 1, 0],
#      [0, 0, 0, 0, 0, 0]]
# a.append("0")
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if a[i][j] == 0:
#             print("?", end=' ')
#         if a[i][j] == 1:
#             print("f", end=' ')
#         if a[i][j] == 2:
#             print("e", end=' ')
#     print()

a = [[0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0]]
a[3][3] = 1
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
