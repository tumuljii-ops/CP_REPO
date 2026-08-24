t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Check if original array works
    ans = True
    curr_sum = 0
    for i in range(n):
        if arr[i] == curr_sum:
            ans = False
            break
        curr_sum += arr[i]
        
    if ans:
        print("YES")
        print(*arr)  # Prints space-separated elements
        continue
    
    # Sort array to reorder
    arr.sort()
    
    i = 0
    j = n - 1
    array = []
    
    # Two-pointer rearrangement (fixing duplicate middle element bug)
    while i <= j:
        if i == j:
            array.append(arr[i])
        else:
            array.append(arr[j])
            array.append(arr[i])
        i += 1
        j -= 1
        
    # Check rearranged array
    answer = True
    curr_sum = 0
    for k in range(n):
        if curr_sum == array[k]:
            answer = False
            break
        curr_sum += array[k]
        
    if answer:
        print("YES")
        print(*array)
    else:
        print("NO")