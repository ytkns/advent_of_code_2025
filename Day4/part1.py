with open('input.txt') as lines: 
    tab = [] 
    for line in lines:
        line = line.strip()
        if not line:
            continue
        tab.append(line)

rolls = 0
rows = len(tab)
cols = len(tab[0])
    
for row in range(rows):
    for col in range(cols):
        if(tab[row][col] == '@'):
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
            if (neighbours < 4): rolls += 1

print(rolls)
