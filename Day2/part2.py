with open("input.txt", "r") as data:
    content = data.read().strip()

ranges = content.split(",")
result = 0

def is_invalid(id):
    s = str(id)
    for i in range(1, len(s) // 2 + 1):
        if(len(s) % i == 0): 
            if (s[:i] * (len(s) // i) == s):
                return True
    return False
    
for r in ranges:
    if "-" not in r:
        continue
    start, end = map(int, r.split("-"))
    
    for id in range(start, end+1):
        if is_invalid(id): result += id
                    
print(result)