# sum of first n natural numbers
N = 5

def recursive(n):
    if n == 1:
        return 1
    return recursive(n-1) + n
# print(towerOfHanoi(4,"A","C","B"))

def sumOfDigits(A,p=1):
    p*=10
    if A%p == A:
        return A
    return sumOfDigits(A%p,p) + A
# print(sumOfDigits(54))

# according to scalar sumOfDigits
def digitsSum(A):
    if A == 0:
        return 0
    return (A%10 + int(digitsSum(int(A//10))))

# def digitsSum(n):
#     if n == 0: 
#         return 0
#     return (n % 10 + digitsSum(int(n / 10))) 

def kthsymbol(A,B):
    if A == 1:
        return '0'
    if A == 2:
        return '01'
    return kthsymbol(A-1)
