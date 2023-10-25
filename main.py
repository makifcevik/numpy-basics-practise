import numpy as np

# creating randomized arrays
array1 = np.random.randint(1, 10, size=(3, 3))
array2 = np.random.randint(1, 10, size=(3, 3))
print(f"array1 :\n{array1}")
print(f"array2 :\n{array2}")

# basic element-wise operations
array3 = array1 + array2
print(f"array1 + array2 :\n{array3}")
array3 = array1 - array2
print(f"array1 - array2 :\n{array3}")
array3 = array1 * array2
print(f"array1 * array2 :\n{array3}")
array3 = array1 / array2
print(f"array1 / array2 :\n{array3}")

# mean and median
array1 = np.random.randint(0, 8, size=10)
array1.sort()
mean = np.mean(array1)
median = np.median(array1)
print(f"array : {array1}\nmean : {mean}\nmedian : {median}")

# reshaping an array
array1 = np.array([element for element in range(12)])
array1 = np.reshape(array1, (3, 4))
print(array1)

# accessing elements
print(array1[1, 2])
print(array1[2, 0])
print(array1[0, -1])

# array slicing
array1 = np.random.randint(0, 100, size=21)
print(array1[:5])  # first 5 elements
print(array1[-5:])  # last 5 elements
print(array1[int(len(array1) / 2)])  # middle element

print(array1)

# basic statistics
array1 = np.random.random(size=15)
minimum = array1.min()
maximum = array1.max()
standard_deviation = array1.std()
print(f"array: {array1}\nmin: {minimum}\nmax: {maximum}\nstandard deviation: {standard_deviation}")

# array concatenation
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
horizontal_concat = np.concatenate((array1, array2), axis=1)  # axis = 1 for horizontal concatenation
vertical_concat = np.concatenate((array1, array2), axis=0)  # axis = 0 for vertical concatenation
print(f"horizontal concatenation:\n{horizontal_concat}")
print(f"vertical concatenation:\n{vertical_concat}")

# filtering arrays
array1 = np.array([1, 2, 3, 4, 5])
print(f"array: {array1}")
x_filter = [True, False, False, False, True]
array1 = array1[x_filter]
print(f"filtered array: {array1}")

array1 = np.random.randint(0, 20, size=10)
even_numbers = array1[array1 % 2 == 0]
print(f"array: {array1}")
print(f"only even numbers array: {even_numbers}")

# element-wise operations
array1 = np.random.randint(0, 10, size=10)
squared_numbers = np.square(array1)
square_root_numbers = np.sqrt(array1)
print(f"array: {array1}")
print(f"squared numbers: {squared_numbers}")
print(f"square root numbers: {square_root_numbers}")

# reshape and transpose
array1 = np.array([element for element in range(12)])
print(f"array:\n {array1}")
array1 = np.reshape(array1, newshape=(3, 4))
print(f"3x4 shaped array:\n{array1}")
array1 = np.transpose(array1)
print(f"transposed array:\n{array1}")

# basic matrix operations
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(array1, array2)
elementwise_product = array1 * array2
print(f"array1:\n{array1}")
print(f"array2:\n{array2}")
print(f"matrix product:\n{matrix_product}")
print(f"element-wise product:\n{elementwise_product}")
