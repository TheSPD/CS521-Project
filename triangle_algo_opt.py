import numpy as np
from scipy.sparse import csr_matrix
from time import time

def triangle_algo(S, p, epsilon):
    # Step 0 : Initialize the p' and v O(m*n)
    dist_values = [np.linalg.norm(v - p) for v in S]
    prime_index = np.argmin(dist_values)
    p_prime = S[prime_index][:]
    vertex = p_prime[:]
    alphas = [(1 if prime_index == v else 0) for v in range(len(S))]
    counter = 0

    while(True):
        counter += 1
        # Step 1 : Check if this p_prime is a 
        # epsilon-approximate solution or a witness
        # print "Distance difference : ", np.linalg.norm(p - p_prime) - epsilon * np.linalg.norm(p - vertex)
        if np.linalg.norm(p - p_prime) < epsilon * np.linalg.norm(p - vertex):
            return True, alphas, counter
        else:
            pivots = [v for v in S if (np.linalg.norm(p_prime - v) > np.linalg.norm(p - v))]
            if len(pivots) == 0:
                return False, p_prime, counter
            else:
                # could be changed here
                vertex = pivots[0]
                vertex_index = [i for i in range(len(S)) if (S[i] == vertex).all()][0]
                # print pivots, vertex

        #Step 2 : Compute the step size
            alpha = (p - p_prime).T.dot(vertex - p_prime)/(np.linalg.norm(vertex - p_prime)**2)            
            alphas = np.array([((1 - alpha) * alphas[i] + alpha) if vertex_index == i else (1 - alpha) * alphas[i] for i in range(len(alphas))])

            # p_prime = csr_matrix(alphas).dot(csr_matrix(S)).toarray()[0]
            p_prime = alphas.dot(S)
