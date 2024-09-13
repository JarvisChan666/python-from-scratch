import numpy as np

from timeit import default_timer as timer

# a = np.array([1,3,4])

# print(a)
# print(a.shape)
# print(a.dtype)
# print(a.ndim)
# print(a.size)
# print(a.itemsize)

# print(a[1])
# a[0] = 10
# print(a)

# b = a * np.array([3,4,5])

# print(b)

# Difference when add list
l = [1, 2, 4]
a = np.array([1, 2, 3])

# l = l + [4]
l = l * 2
print(l)
# a = a + np.array([4]) # broadcasting [4, 4, 4]
# a = a * 2
# print(a)

# dot = 0

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# a1 = np.array(l1)
# a2 = np.array(l2)

# for i in range(len(l1)):
#     dot += l1[i] * l2[i]
# print(dot)

# dot = np.dot(a1, a2)
# print(dot)

# sum1 = a1 * a2
# dot = np.sum(sum1)
# print(dot)

# dot = a1 @ a2
# print(dot)



# Speed Test Array vs List
# a = np.random.randn(1000)
# b = np.random.randn(1000)

# A = list(a)
# B = list(b)

# T = 1000

# def dot1():
#     dot = 0
#     for i in range(len(A)):
#         dot += A[i] * B[i]
#     return dot

# def dot2():
#     return np.dot(a, b)

# start = timer()
# for t in range(T):
#     dot1()
# end = timer()
# print(end - start)

# start = timer()
# for t in range(T):
#     dot2()
# end = timer()
# print(end - start)


# md array
# a = np.array([1, 2])
# print(a.shape)
# a = np.array([[1, 2], [3, 4]])
# print(a.shape)
# print(a[0][1])
# print(a[:, 0]) # all row, 1st column
# print(a.T)
# print(np.linalg.inv(a))


# Indexing / Slicing / Boolean Indexing
# b = a[0, 1]
# print(b)
# a = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
# b = a[1, 2:]
# print(b)
# b = a[1, -2:]
# print(b)
# b = a[:, -1:]
# print(b)

# bool_idx = a > 2
# # print(a[bool_idx])
# b = np.where(a > 2, a, -1)
# print(b)
# a = np.ascontiguousarray([3,43,54,5, 3, 3, 3])
# b = [1, 3, 5]
# print(a[b])



# Reshaping
# a = np.arange(1, 7)
# b = a.reshape(3, 2)
# print(a)
# print(b)


# Concatenation
# a = np.array([[1, 2], [3, 4]])
# print(a)
# b = np.array([[5, 6]])
# c = np.concatenate((a, b)) # row
# print(c)
# c = np.concatenate((a, b.T), axis = 1) # column
# print(c)

# a = np.array([1, 2, 3, 4])
# b = np.array([5, 6, 7, 8])
# # hstack
# c = np.hstack((a, b))
# print(c)
# # vstack
# c = np.vstack((a, b))
# print(c)



# Broadcasting
# x = np.array([[1, 2, 3], [4, 5, 6], [1, 2, 3], [4, 5, 6]])
# a = np.array([1, 0, 1])
# y = x + a
# print(y)


# Function and axis
a = np.array([[7, 8, 9, 10], [1, 2, 3, 4]])
print(a)
print(a.sum(axis = 1))
print(a.mean(axis = 1))