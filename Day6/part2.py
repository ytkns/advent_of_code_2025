with open("input.txt") as f:
    lines = f.read().splitlines()


width = max(len(line) for line in lines)
grid = [list(line.ljust(width)) for line in lines]

rows = len(grid)
cols = width
result = 0


