        
nums = [6,1,2,3,4]

def check(nums):
    n = len(nums)
    i = n-2
    j = n-1
    swaps = 0
    if nums[0] > nums[-1]:
        while i >= 0:
            if nums[i]<nums[j]:
                j-=1
                i-=1
                swaps+=1
            elif nums[i]>nums[j]:                
                return swaps+1
            else:
                return 0
    else:
        i=0
        j=1
        while j<n:
            if nums[i]<nums[j]:
                i+=1
                j+=1
        return 0
    return -1

print(check(nums))