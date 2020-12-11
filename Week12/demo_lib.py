import numpy as np


# create a 1-dimension array
a = np.array([12,23,34])

print(type(a))

# a tuple containing the size of the array in each dimension.
print(a.shape)

a[0] = 45

print(a)

# create a 2-dimension array

b = np.array([[3, 56, 342], [423, 343, 23]])
print(b.shape)

print(b[0, 0], b[0, 1])

# Fill a matrix size 2x2 with 0
c = np.zeros((2,2))
print(c)

# Fill a matrix size 1x2 with 1
d = np.ones((1,2))
print(d)

# Fill a matrix size 2x2 with 10
e = np.full((2,2), 10)
print(e)

# create a identity matrix of size 5x5
f = np.eye(5)
print(f)


############# ARRAY INDEXING ##############


# Slide
ab = np.array([[1,2,3,5], [5,6,7,8], [1,4,3,2]])
ba = ab[:2, 1:4]
print(ba)

ad = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(ad)
row_r1 = ad[1, :] # Lấy ra hàng thứ 2 trong a, output array 1 chiều
row_r2 = ad[1:2, :] # Lấy ra hàng thứ 2 trong a, output array 2 chiều
print(row_r1, row_r1.shape) # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape) # Prints "[[5 6 7 8]] (1, 4)"


############ Addition in numpy #############
x = np.array([[1,2], [3,4]], dtype = np.float64)
y = np.array([[2,5], [5,9]], dtype = np.float64)

print(x + y)
print(np.add(x, y))




