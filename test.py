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

