t = int(input())

for _ in range(t):
    n = int(input())
    
    # 1. Count total digits using integer division
    num = n
    count = 0
    while num > 0:
        count = count + 1
        num = num // 10
        
    # 2. Add 9 for each full digit-length smaller than count
    total = 0
    for i in range(1, count):
        total = total + 9
        
    # 3. Find the divisor x (10^(count-1))
    x = 1
    for i in range(1, count):
        x = x * 10
        
    # 4. Extract the leading digit and add it to total
    result = n // x
    print(result + total)
        
        
        
    
        
    
    