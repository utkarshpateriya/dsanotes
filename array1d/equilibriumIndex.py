A = [-7, 1, 5, 2, -4, 3, 0]

def sumOfArray(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

def equilibriumIndex(arr):
    arrsum = sumOfArray(arr)
    lsum = 0 
    count = 0
    rsum = arrsum
    for i in range(len(arr)):
        rsum -= arr[i]
        if lsum == rsum:
            count += 1
        lsum += arr[i]
    return count

print(equilibriumIndex(A))