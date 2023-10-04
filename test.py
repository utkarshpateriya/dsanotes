A = [2,6,9,4,10]

def countTriplets(A):
    # write your code here
    # return the number of triplets in an array such that
    # i<j<k and A[i]<A[j]<A[k]
    n = len(A)
    triplets = 0
    for i in range(1,n):
        count_left = 0
        count_right = 0
        for j in range(i):
            if A[j]<A[i]:
                count_left+=1
        for j in range(i+1,n):
            if A[j]>A[i]:
                count_right+=1        
        triplets += count_right*count_left
    return triplets
    
# print(countTriplets(A))

# find closest power of two less than or equal to n
def closestPowOfTwo(n):
    res = 0
    for i in range(n,0,-1):
        if ((i & (i-1)) == 0):
            res = i
            break
    return res

# print(closestPowOfTwo(100))

A = [4,3,3,3,4,3,4,4,4,3]

def majorityElement(A):
    h = {}
    n = len(A)
    for i in range(n):
        if A[i] in h:
            h[A[i]]+=1
        else:
            h[A[i]]=1
    
    for key, value in h.items():
        if value > n/2:
            return key
    return -1

# print(majorityElement(A))

A = [2,3,2,3,2,3,2,3,2,5,4,2]

# Moore's Voting Algorithm
def mooremajurityelement(A):
    n = len(A)
    potential_candidate = A[0]
    frequency = 1
    for i in range(1,n):
        if frequency == 0:
            potential_candidate = A[i]
        elif A[i] == potential_candidate:
            frequency += 1
        else:
            frequency -= 1
    count = 0
    for i in range(n):
        if A[i]==potential_candidate:
            count+=1
    if count > n/2:
        return potential_candidate
    return -1

# print(mooremajurityelement(A))

def solution(A):
    h = {}
    for i in A:
        if i in h:
            h[i]+=1
        else:
            h[i] = 1
    
    min_cost = float('inf')
    for coin in h:
        cost = 0
        for other_coin in h:
            if coin == other_coin:
                continue
            diff = abs(other_coin - coin)
            if diff%2==0:
                cost+=0
            else:
                cost+=(diff*h[other_coin])
        min_cost = min(min_cost, cost)
    return min_cost

# print(solution([1,3,1,3,9,6,3,6,1]))

def combinationSum4(nums, target: int) -> int:
    nums.sort()
    h = {}
    def helper(k):
        if k in h:
            return h[k]
        if k == 0:
            return 1
        if k < nums[0]:
            return 0
        count = 0
        for num in nums:
            if k-num < 0:
                break
            count += helper(k-num)
        h[k] = count
        return count
    return helper(target)

# print(combinationSum4([1,2,3],4))

def groupThePeople(A):
    res = []
    h = {}
    n = len(A)
    for i in range(n):
        if A[i] in h:
            if len(h[A[i]]) == h(A[i]):
                res.append(h[A[i]])
                del h[A[i]]
                h[A[i]] = [i]
                continue
            h[A[i]].append(i)
        else:
            h[A[i]] = [i]


# print(groupThePeople([3,3,3,3,3,1,3]))

def maxValue(n, arr) -> int:
    # code here
    geekvalue = float('-inf')
    for i in range(n):
        left_max = 0
        right_max = 0
        for j in range(i):
            left_max = max(left_max, arr[j]-arr[i])
        for j in range(i+1, n):
            right_max = max(right_max, arr[j])
        geekvalue = max(geekvalue, left_max*right_max)
    return geekvalue

# print(maxValue(3, [4,2,3]))

s = "  ab"

def myAtoi(s):
        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i+=1
        positive = 0
        negative = 0
        if i<n and s[i] == '+':
            positive += 1
            i+=1
        if i<n and s[i] == '-':
            negative += 1
            i+=1

        ans = 0

        while i<n and '0' <= s[i] <= '9':
            ans = ans * 10 + (ord(s[i])-ord('0'))
            i+=1
        
        if negative > 0:
            ans = -ans

        if positive > 0 and negative > 0:
            return 0
        
        max_size = 2**31 -1
        min_size = -2**31

        if ans > max_size:
            ans = max_size
        
        if ans < min_size:
            ans = min_size
        
        return int(ans)

print(ord('4') - ord('0'))