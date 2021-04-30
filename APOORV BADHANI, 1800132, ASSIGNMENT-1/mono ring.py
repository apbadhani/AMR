import numpy as np
import math
#Matrix Generator
def Matgen(x,y,n):
    Y = []
    i = 0
    while i < n:
        X = []
        j = 0
        while j<n:
            X.append(0)
            j = j + 1
        Y.append(X)
        i = i + 1
    for i in range(n):
        for j in range(n):
            if (i == j):
                Y[i][j] = x
                if i == n-1:
                    break

                else:
                    Y[i+1][j] = y
                if j == n-1:
                    break
                else:
                    Y[i][j+1] = y
    Y[0][n-1] = y
    Y[n-1][0] = y
    return Y


#Density function
def Density(x,y,n1,n2):
    X = []
    Y = []
    j = n1
    while j<n2:
        A = Matgen(x,y,i)
        a,b = np.linalg.eig(A)          #Function for eigenvalue and eigenvectors
        wid = max(a) - min(b)
        X.append(i)
        Y.append(wid)
        j+=1
#prints maximum and minimum eigenvalues of the matrix used
def giveigen(x,y,n):
    Y = Matgen(x,y,n)
    w, v = np.linalg.eig(Y)
    print("max eigenvalue is: ", max(w),"  " "min eigenvalue is: ", min(w))

#Max and Min eigenvalues of the matrix used in the graph
giveigen(8,0.2,1000)
giveigen(8,0.2,500)
giveigen(8,0.2,200)
giveigen(8,0.3,1000)
giveigen(8,0.4,1000)
giveigen(8,0.5,1000)

