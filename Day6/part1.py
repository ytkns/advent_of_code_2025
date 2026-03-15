with open("input.txt", "r") as lines:
    tab = []
    op = []
    for line in lines:
        line = line.strip()
        if line.startswith('+') or line.startswith('*'):
            op = line.split()
        else:
            tab.append(line.split())

transposed = [[tab[i][j] for i in range(len(tab))] for j in range(len(tab[0]))]

result = 0

for i in range(len(transposed)):
    add = 0
    added = False
    multiply = 1
    multiplied = False
    for j in range(len(transposed[0])):
        if op[i] == '+':
            add += int(transposed[i][j])
            added = True
        if op[i] == '*':
            multiply *= int(transposed[i][j])
            multiplied = True
    if(added): result += add
    if(multiplied): result += multiply   

print(result)










with open("input.txt", "r") as lines:
    tab = []
    op = []
    for line in lines:
        line = line.strip()
        if line.startswith('+') or line.startswith('*'):
            op = line.split()
        else:
            width = max(len(line))
            grid = [list(line.ljust(width))]

