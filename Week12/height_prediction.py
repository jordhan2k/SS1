######### LINEAR REGRESSION ########

from __future__ import print_function
import numpy as np
import  matplotlib.pyplot as plt

#### LEARNING BY FORMULA
#w = ((XX^T)t))Xy

# Declare training data
# height (cm), (n x 1) matrix (input data)
# .T : transpose of a matrix, input matrix X is of size (nx1)
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# weight (kg)
y = np.array([ 49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])

# weight = w_1 * (height) + w_0

##############
#Building Xbar
one = np.ones((X.shape[0], 1))
# each point is one row
Xbar = np.concatenate((one, X), axis = 1) # concatenate 2 matrix by y axis (vertical merge)
# Xbar is  a matrix with first column filled with 1
# second column filled with x1 values
######
# Calculating weights of fitting line
# A = XX^T
A = np.dot(Xbar.T, Xbar)
# b = Xy (Xbar.T , y)
b = np.dot(Xbar.T, y)
# w = ((XX^T)^tXy
w = np.dot(np.linalg.pinv(A), b)

w_0, w_1 = w[0], w[1]

##############
y1 = w_0 + w_1 * 155
y2 = w_0 + w_1 * 160

print('w_0 (bias b): ', w_0)
print('w_1: ', w_1)
print('Input 155cm, true output 52kg, predicted output %.2fkg.'%(y1) )
print('Input 160cm, true output 56kg, predicted output %.2fkg.'%(y2) )


