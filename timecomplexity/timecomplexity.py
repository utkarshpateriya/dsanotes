# Given an integer A, you need to find the count of it's factors.
# Factor of a number is the number which divides it perfectly leaving no remainder.
# Example : 1, 2, 3, 6 are factors of 6

def factorsfind(A):
    count = 0
    for i in range(1,int(A**0.5)+1):        
        if A%i == 0:
            if i*i == A:
                count+=1
            else:                
                count+=2
    return count

print(factorsfind(int(36)))