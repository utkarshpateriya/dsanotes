# To find the prefix sum of an array
arr = [3,5,6,7,10,21,0,8]

def prefixSum(A):
    '''
        This function returns the prefix sum array for
        an input array
    '''
    prefixSumArray = []
    prefixSumArray.append(0)
    N = len(A)
    sumTillNow = 0
    for i in range(N):
        prefixSumArray[i] += sumTillNow
        sumTillNow += A[i]
    return prefixSumArray