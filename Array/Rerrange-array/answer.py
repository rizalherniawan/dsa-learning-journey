def reArrange(arr, N):
    move = 1
    for i in range(0, N):
        if arr[i] % 2 == i % 2:
            if move <= i:
                move = i + 1
            continue
        else:
            while (arr[move] % 2) != (i % 2):
                move += 1
            temp = arr[i]
            arr[i] = arr[move]
            arr[move] = temp
    return arr
    


arr = [9,3,8,8]
print(reArrange(arr, len(arr)))
    





            
            