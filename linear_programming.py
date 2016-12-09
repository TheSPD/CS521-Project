import triangle_algo_opt_2 as triAlg
import triangle_algo as triAlgOld
from scipy.sparse import csr_matrix
import numpy as np
from time import time

try:
    print 'All the parameters are for a standard form minimization problem'
    n = int(raw_input("Enter the number of unknowns : "))
    m = int(raw_input("Enter number of constraints : "))


    print "Enter c (separated by spaces) : "

    c = [map(float, raw_input().strip().split(' '))]

    if n != len(c[0]):
        raise Exception("Please provide valid input for c")

    print "Enter A (in row major format separated by spaces and new line) : "
    A = [map(float, raw_input().strip().split(' ')) for _ in range(m)]

    if any([False if len(row) == n else True for row in A]):
        raise Exception("Please provide valid input for A")        

    print "Enter b (separated by spaces) : "

    b = [map(float, raw_input().strip().split(' '))]

    if m != len(b[0]):
        raise Exception("Please provide valid input for b")

    print 'Processing...'

    c = np.array(c, np.float64).T
    A = np.array(A, np.float64)
    b = np.array(b, np.float64).T

    # m = 2
    # n = 2
    # c = np.array([[1, 2]]).T
    # A = np.array([[1, 2],[3, 4]])
    # b = np.array([[5, 6]]).T

    zeroMM = np.zeros((m, m))
    zeroNN = np. zeros((n, n))
    zeroMN = np.zeros((m, n))
    zeroNM = np. zeros((n, m))

    negIdenN = -np.identity(n)
    negIdenM = -np.identity(m)

    
    A_prime = np.concatenate((-A, zeroMM), axis=1)
    A_prime = np.concatenate((A_prime, np.concatenate((zeroNN, A.T), axis=1)))
    A_prime = np.concatenate((A_prime, np.concatenate((c.T, -b.T), axis=1)))
    A_prime = np.concatenate((A_prime, np.concatenate((-c.T, b.T), axis=1)))
    A_prime = np.concatenate((A_prime, np.concatenate((negIdenN, zeroNM), axis=1)))
    A_prime = np.concatenate((A_prime, np.concatenate((zeroMN, negIdenM), axis=1)))

    b_prime = np.concatenate((-b, c))
    b_prime = np.concatenate((b_prime, np.zeros((2+m+n, 1))))

    epsilon = 0.1
    B = np.concatenate((A_prime.T, np.zeros((m+n, 1))), axis=1)
    B = np.concatenate((B, np.concatenate((b_prime.T+epsilon, np.ones((1,1))), axis = 1)))

    p = np.zeros((m+n+1,1))
    t0=time()   
    insideOrNot , result, counter = triAlgOld.triangle_algo(B.T.tolist(), p.T.tolist()[0], 0.001, len(p.T.tolist()[0]))
    print "Old Time taken %f seconds" % (time()-t0)
    y = [ -1*result[i]/result[len(result)-1] for i in range(len(result))]
    print insideOrNot , result, counter, y
    print 'Unknowns are : ', y[:n]

    p = np.zeros((m + n + 1, 1))
    t0=time()
    insideOrNot , result, counter = triAlg.triangle_algo(csr_matrix(B.T, dtype=np.float32), csr_matrix(p.T[0], dtype=np.float64), 0.001)
    print "New Time taken %f seconds" % (time() - t0)
    y = [-1 * result[i] / result[len(result) - 1] for i in range(len(result))]
    print insideOrNot , result, counter, y
    print 'Unknowns are : ', y[:n]


except Exception as e:
    print e
    exit()

