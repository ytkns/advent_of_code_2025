with open("input.txt") as f:
    blocks = f.read().strip().split("\n\n")

ranges = [tuple(map(int, r.split("-"))) for r in blocks[0].splitlines()]
fresh = 0

ranges.sort(key=lambda x: x[0])

changing=True
while changing:
    i=0
    while i < (len(ranges)-1):
        if ranges[i][1] >= ranges[i+1][0]:
            ranges[i:i+2] = [(ranges[i][0], max(ranges[i][1], ranges[i+1][1]))]      
        else: 
            i+=1  
            changing = False
            
for r in ranges:
    fresh += r[1]-r[0]+1

print(fresh)
