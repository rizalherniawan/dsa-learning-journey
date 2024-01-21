def removeDuplicates(str: str):
    x = {}
    res = ""
    for i in str:
        if i not in x:
            x[i] = i
            res += i
    
    return res

print(removeDuplicates("HappyNewYear"))