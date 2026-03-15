with open('input.txt') as lines:

    result = 0 
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        max1 = max(int(i) for i in line[:len(line)-1])
        idx_max1 = line.index(str(max1))
        
        max2 = max(int(i) for i in line[idx_max1+1:])    
        
        result += int(str(max1) + str(max2))
    
    print(result)
