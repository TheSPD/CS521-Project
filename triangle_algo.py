import numpy as np
import math


##
#distance
#Calculates the distance between two vectors of dimension n
#Could also go for np.linalg.norm(v1-v2) but used this to optimize the process later
#@params
#n - Dimensions of the vector
#v1 - Vector 1
#v2 - Vector 2
##
def distance(n,v1,v2):
	if len(v1) != len(v2):
		return null
	else:
		distance = 0
		for i in range(n):
			distance += (v1[i] - v2[i])**2
		distance = math.sqrt(distance)
		return distance

def diff(n,v1,v2):
	if len(v1) != len(v2):
		return null
	else:
		v = []
		for i in range(n):
			v.append((v1[i] - v2[i]))
		return v

def inner_prod(n, v1, v2):
	if len(v1) != len(v2):
		return null
	else:
		prod = 0
		for i in range(n):
			prod += v1[i] * v2[i]
		return prod

def triangle_algo(S, p , epsilon, dim):
	# Step 0 : Initialize the p' and v O(m*n)
	dist_values = [distance(dim, v, p) for v in S]
	prime_index = dist_values.index(min(dist_values))
	p_prime = S[prime_index][:]
	vertex = p_prime[:]
	alphas = [(1 if prime_index == v else 0 ) for v in range(len(S)) ]
	print vertex

	while(True):
		#Step 1 : Check if this p_prime is a epsilon-approximate solution or a witness
		print "Distance difference : ", distance(dim, p, p_prime) - epsilon * distance(dim, p, vertex)
		if distance(dim, p, p_prime) < epsilon * distance(dim, p, vertex):
			return True, alphas
		else:
			pivots = [v for v in S if (distance(dim,p_prime,v) > distance(dim,p,v))]
			if len(pivots) == 0:
				return False, p_prime
			else:
				vertex = pivots[0]
				vertex_index = S.index(vertex)

		#Step 2 : Compute the step size
			alpha = inner_prod(dim, diff(dim, p, p_prime), diff(dim, vertex, p_prime))/(distance(dim, vertex, p_prime)**2)
			# print alphas, alpha
			alphas = [((1-alpha)*alphas[i] + alpha) if vertex_index == i else (1-alpha)*alphas[i] for i in range(len(alphas))]
			# print alphas
			p_prime = []
			for i in range(dim):
				p_prime.append(0)
				for j in range(len(S)):
					p_prime[i] += alphas[j] * S[j][i]
			print p_prime

# v1 = [1,1]
# v2 = [4,1]
# v3 = [3,3]

# S = [v1,v2,v3]

#inside the triangle
# p = [3,2]

#outside the triangle
# p = [4,2]
# 

v1 = [0,0,0]
v2 = [0,4,0]
v3 = [4,0,0]
v4 = [4,4,0]
v5 = [0,0,4]
v6 = [0,4,4]
v7 = [4,0,4]
v8 = [4,4,4]

S = [v1,v2,v3,v4,v5,v6,v7,v8]

p = [5,5,4]

epsilon = 0.01

x,y = triangle_algo(S, p, epsilon, len(p))
print ( x,y )
# sum(y)

# print v1
# print v2
# print v3
# print diff(2, v3, v1)
# print (distance(2, v1, v2))

# v1 = np.array(v1)
# v2 = np.array(v2)
# v3 = np.array(v3)
# print v1
# print v2
# print v3
# print (v3-v1)