with open('input.txt') as lines:
    tab = [] 
    for line in lines:
        line = line.strip()
        if not line:
            continue
        tab.append(list(line))
        
rows = len(tab)
cols = len(tab[0])
    
def is_to_remove(row, col):
    if(tab[row][col] != '@'): return False
    neighbours=0
    up = -1
    down = 1
    left = -1
    right = 1

    if (row == 0): up = 0
    if (col == 0): left = 0
    if (row == rows-1): down = 0
    if (col == cols-1): right = 0

    for i in range(up, down+1):
        for j in range(left, right+1):
            if tab[row+i][col+j] == '@':
                if(i==0 and j==0): continue
                neighbours += 1
    return (neighbours < 4)

to_remove = 0

while(True):
    taken = []
    for r in range(rows):
        for c in range(cols):
            if is_to_remove(r,c):
                taken.append((r,c))
    
    if not taken: break

    for (r,c) in taken:
        tab[r][c] = '.'
        to_remove+=1
    
print(to_remove)
