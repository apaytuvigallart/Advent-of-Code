result = []
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        left = int(line.split("-")[0])
        right = int(line.split("-")[1])
        while left <= right:
            s = str(left)
            first, second = s[: len(s) // 2], s[len(s) // 2 :]
            if first == second:
                result.append(left)
            left += 1
print(sum(result))
