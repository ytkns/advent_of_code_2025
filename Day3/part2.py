with open('input.txt') as lines:

    def max_joltage(line):

        max_jol = []
        max_jol_str = ""

        idx = 0

        for j in range(0, 12):
            curr_digit = max(int(i) for i in line[idx : len(line)-11+j])
            max_jol.append(curr_digit)
            idx = line.index(str(curr_digit), idx) + 1

        for k in max_jol:
            max_jol_str += str(k)
        
        return int(max_jol_str)

    result = 0 
    for line in lines:
        line = line.strip()
        if not line:
            continue
        result += max_joltage(line)
    
    print(result)