with open('input.txt') as lines:
    pos = 50
    count = 0
   
    for line in lines:
        line = line.strip()
        if not line:
            continue
        dir = line[0]
        dist = int(line[1:])
       
        if dir == 'R':
            count += (pos+dist) // 100
            pos = (pos+dist) % 100
        
        else:
            if pos-dist <= 0: 
                count = count + (dist-pos) // 100
                if pos != 0: count += 1
                pos = (100 - ((dist - pos) % 100)) % 100
                
            else:
                pos -= dist
            
    print(count)



        