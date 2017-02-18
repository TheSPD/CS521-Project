import numpy as np


def potentialReduction(d, Q, epsilon):
    """Implementation of the potential reduction algorithm"""
    count = 0
    while(True):
        # Step 1 : Given d > 0, compute y and lamda
        e = np.ones((2, 1))
        D = np.diag([x[0] for x in d.tolist()])
        DQDe = D.dot(Q).dot(D.dot(e))
        # print np.linalg.norm((DQDe - e)), count
        if (np.linalg.norm((DQDe - e)) > epsilon):
            D_2 = (D ** -2)
            D_2[D_2 == np.inf] = 0
            y = np.linalg.inv((D_2 + Q)).dot(((d ** -1) - (Q.dot(d))))
            lamda = (y.T.dot((D_2 + Q)).dot(y))[0][0] ** 0.5
        else:
            return d, count

        # Step 2
        if lamda < 1:
            d = d + y
        elif lamda >= 1:
            alpha = 1 / (1 + lamda)
            d = d + alpha * y

        count += 1


# d = np.array([[0.5], [0.5]], dtype=np.float64)
# Q = np.array([[4, -1], [-1, 2]], dtype=np.float64)

# t0 = time()
# d = potentialReduction(d, Q, 0.001)

# print "The Diagonal matrix that scales Q is :"
# print d
