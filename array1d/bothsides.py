# You are given an integer array A of size N.

# You have to perform B operations. In one operation, you can remove either the leftmost or the rightmost element of the array A.

# Find and return the maximum possible sum of the B elements that were removed after the B operations.

# NOTE: Suppose B = 3, and array A contains 10 elements, then you can:

# Remove 3 elements from front and 0 elements from the back, OR
# Remove 2 elements from front and 1 element from the back, OR
# Remove 1 element from front and 2 elements from the back, OR
# Remove 0 elements from front and 3 elements from the back.

def pickbothsides(self, A, B):
    N = len(A)
    currSum = 0
    for i in range(B):
        currSum += A[i]
    inc = N-1
    exc = B-1
    maxSum = currSum
    while inc >= 0 and exc >= 0:
        currSum += A[inc]
        inc -=1
        currSum -= A[exc]
        exc -= 1
        maxSum = max(maxSum, currSum)
    return maxSum

print(pickbothsides([5, -2, 3 , 1, 2],3))