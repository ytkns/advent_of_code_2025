with open("input.txt") as data:
    content = data.read().strip()

ranges = content.split(",")
result = 0

for r in ranges:
    if "-" not in r:
        continue
    start, end = map(int, r.split("-"))
    
    for id in range(start, end+1):
        s = str(id)
        if( s[:len(s)//2] == s[len(s)//2:] ):
            result += id

print(result)

