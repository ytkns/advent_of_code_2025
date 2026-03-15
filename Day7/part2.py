with open("input.txt") as lines:
    tab = []
    for line in lines:
        line = line.strip()
        if line:
            tab.append(line)

tab[0] = tab[0].replace('S', '.')
ways = [[0] * len(tab[0]) for _ in range(len(tab))]
ways[0][len(tab[0]) // 2] = 1

for row in range(len(tab) - 1):
    for col in range(len(tab[0])):
        if ways[row][col] > 0:
            if tab[row][col] == '.':
                ways[row+1][col] += ways[row][col]
            elif tab[row][col] == '^':
                if col - 1 >= 0:
                    ways[row+1][col-1] += ways[row][col]
                if col + 1 < len(tab[0]):
                    ways[row+1][col+1] += ways[row][col]

suma = sum(ways[len(tab[0])])
print(suma)
