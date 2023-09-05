# Given an array of integers A, find and return the product array of the same size where the ith element of the product array will be equal to the product of all the elements divided by the ith element of the array.

# Note: It is always possible to form the product array with integer (32 bit) values. Solve it without using the division operator.

def productArray(A):
    N = len(A)
    product = 1
    for i in range(N):
        product *= A[i]
    res = []
    for i in range(N):
        res.append(product//A[i])
    return res

print(productArray([1, 2, 3, 4, 5]))