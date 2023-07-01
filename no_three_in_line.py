import sys
from z3 import *

def solve(n, count):
    model = Solver()

    # making variables for every index of matrix
    points = [[Int(f'x_{i}_{j}') for j in range(n)] for i in range(n)]
   
    # values of variables can be only 0 (point not placed) or 1 (point placed)
    for i in range(n):
        for j in range(n):
            model.add(Or(points[i][j] == 0, points[i][j] == 1))

    # there can be 2 points at maximum for every row and column
    for i in range(n):
        for j in range(n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    model.add(Or(points[i][j] != 1, points[i][k] != 1, points[i][l] != 1))
                    model.add(Or(points[j][i] != 1, points[k][i] != 1, points[l][i] != 1))

    # only 2 points at maximum on every diagonal
    for d in range(-(n-1), n):
        diag = [points[i][i-d] for i in range(n) if 0 <= i-d < n]
        model.add(Sum(diag) <= 2)


    # sum of all values in matrix (== number of placed point, since every placed point has value 1)
    sum_points = Int('sum_points')
    model.add(sum_points == Sum([points[i][j] for i in range(n) for j in range(n)]))
    # making sure to place given number of points
    model.add(sum_points == count)


    if model.check() == sat:
        result = model.model()

        # matrix for printing the result
        result_matrix = [[0 for j in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(n):
                result_matrix[i][j] = result[points[i][j]]

        # printing the result
        for i in range (0, n):
            for j in range (0, n):
                print(result_matrix[i][j], end =" ")
            print("\n", end="")
    else:
        print("Pro velikost " + str(n) + "x" + str(n) + " nelze umistit " + str(count) + " bodu na mrizku.")



if (len(sys.argv) != 3):
    print("Program se spousti s 2 argumenty prikazove radky, kde prvni je velikost mrizky a druha je pocet bodu ktere chceme umistit.")
    print("Priklad: python3 no_three_in_line.py 5 10")
    exit(0)

n = int(sys.argv[1])  # matrix size
count = int(sys.argv[2])  # number of points to place

solve(n, count)