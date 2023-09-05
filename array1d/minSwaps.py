A = [1,12,10,3,14,10,5]
B = 8
def minSwaps(A, B):
        n=len(A)
        count = 0
        for i in range(0, n) :
            if (A[i] <= B) :
                count = count + 1
        bad = 0
        for i in range(0, count) :
            if (A[i] > B) :
                bad = bad + 1
        ans = bad
        j = count
        for i in range(0, n) :

            if(j == n) :
                break
            if (A[i] > B) :
                bad = bad - 1
            if (A[j] > B) :
                bad = bad + 1
            ans = min(ans, bad)
    
            j = j + 1
    
        return ans

print(minSwaps(A, B))