with open("input.txt") as lines:
    tab = [] 
    for line in lines:
        line = line.strip()
        if not line:
            continue
        tab.append(line)

count = 0
pos = []
pos.append(len(tab[0])//2)  

for row in range(len(tab)):
    for col in range(len(tab[0])):
        if (tab[row][col] == '^' and (col in pos)):
            if col+1 not in pos: pos.append(col+1)
            if col-1 not in pos: pos.append(col-1)
            pos.remove(col)
            count+=1
            
print(count)

