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

# Hello from windows