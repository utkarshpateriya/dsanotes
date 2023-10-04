def isSubsequence(s, t) -> bool:
    if not s:
        return True        
    i = 0                
    for c in t:
        if c == s[i]:
            i += 1
        if i >= len(s):
            break        
    if i == len(s):     
        return True
    
    return False

print(isSubsequence("abc", "ahbgdc"))