# You can do it. Stay Consistent

'''
Two conditions of DP ~
1 There has to be optimal substructure - solving a problem using
  smaller instances of same problem
2 Overlapping subproblems - Solving a subproblem again and again
Dynamic Programming is mainly an optimization over plain recursion. 
Wherever we see a recursive solution that has repeated calls for same inputs, 
we can optimize it using Dynamic Programming. The idea is to simply store the 
results of subproblems, so that we do not have to re-compute them 
when needed later.
'''

# question 1 - Find the fibbonacci of Nth number


def fib(N):
    '''
    If already solved don't solve it again.
    '''
    dp = [-1]*(N+1)
    def findFibbonacci(N):
        if N <= 1:
            return N
        if dp[N] != -1:
            return dp[N]
        dp[N] = findFibbonacci(N-1) + findFibbonacci(N-2)
        return dp[N]
    return findFibbonacci(N)


print(fib(10))
