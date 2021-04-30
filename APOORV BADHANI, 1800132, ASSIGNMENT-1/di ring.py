import math
import numpy as np

#Matrix generator
def Matgen(x, y, z, n):
    Y = []
    i = 0
    while i < n:
        X = []
        j = 0
        while j < n:
            X.append(0)
            j = j + 1
        Y.append(X)
        i = i + 1
    for i in range(n):
        for j in range(n):
            if (i == j):
                Y[i][j] = x
                if i >= n - 1:
                    break
                else:
                    Y[i + 1][j] = y
                if j >= n - 1:
                    break
                else:
                    Y[i][j + 1] = y
    i = 0
    while i < n:
        Y[i][i] = z
        i = i + 2

    Y[0][n - 1] = y
    Y[n - 1][0] = y
    i = 0
    j = 0

    return Y


#prints maximum and minimum eigenvalues of the matrix used
def giveigen(x,y,z,n):
    Y = Matgen(x,y,z,n)
    w, v = np.linalg.eig(Y)
    print("max eigenvalue is: ", max(w),"  " "min eigenvalue is: ", min(w))


#Max and Min eigenvalues of the matrix used in the graph
giveigen(8, -2, 5, 1000)
giveigen(8, -2, 5, 500)
giveigen(8, -2, 5, 200)

giveigen(8, -2.5, 5, 1000)
giveigen(8, -1.5, 5, 1000)
giveigen(8, -0.5, 5, 1000)

