# Time complexity is nothing but rate of growth of time with respect to input size

N = 100 #Can be any positive integer

#All the functions defined here:-

#O(N) Example

def iterateN(n):
    for i in range(n):
        print(n)

#Number of iterations
def countIteration(n):
    '''
    This will print the numbers from 0 to 100 i.e 100-0+1 = 101 iterations
    '''
    for i in range(0,100):
        print(i)

def logIterations(n):
    '''
    In this case iterations will be log2(n)
    '''
    for i in range(n):
        i = i/2

#Space Complexity is the rate of growth of memory or space with respect to size
#Amount of extra space taken by the algorithm is space complexity input and output space should not be included

#Check if x is present in given array or not. Return bool
def is_x_present(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return True
    return False

print(is_x_present([1,2,3,4,5,6], 9))
#Here time complexity is O(N) and space complexity is O(1)

# Note:For all online platforms processing speed is 1GHz/sec i.e 10^9 instructions per second.