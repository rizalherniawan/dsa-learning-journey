def characterReplacement(s: str, k: int) -> int:
    my_dict = {}
    max_val = 0
    temp = 0
    maxf = 0
    start_index = 0
    for i in range(len(s)):
        if s[i] not in my_dict:
            my_dict[s[i]] = 1
        else:
            my_dict[s[i]] += 1
        maxf = max(maxf, my_dict[s[i]])

        while (i - start_index + 1) - maxf > k:
            my_dict[s[start_index]] -= 1
            start_index += 1
        
        max_val = max(max_val, i - start_index + 1)
    return max_val

s = "ABAB"
k = 2
print(characterReplacement(s,k))
            
