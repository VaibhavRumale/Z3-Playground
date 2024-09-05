from z3 import *

N = 9

X = [[Int(f'x_{i}_{j}') for j in range(N)] for i in range(N)]

s = Solver()

for i in range(N):
    for j in range(N):
        s.add(And(X[i][j] >= 1, X[i][j] <= 9))

for i in range(N):
    s.add(Distinct(X[i]))

for j in range(N):
    s.add(Distinct([X[i][j] for i in range(N)]))

for i in range(0, N, 3):
    for j in range(0, N, 3):
        s.add(Distinct([X[i + k // 3][j + k % 3] for k in range(N)]))

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

for i in range(N):
    for j in range(N):
        if puzzle[i][j] != 0:
            s.add(X[i][j] == puzzle[i][j])

if s.check() == sat:
    m = s.model()
    r = [[m.evaluate(X[i][j]) for j in range(N)] for i in range(N)]
    for row in r:
        print(row)
else:
    print("No solution exists")

