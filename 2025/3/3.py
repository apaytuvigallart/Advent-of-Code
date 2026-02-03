result = []
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        length = len(line)
        higher = 0
        for i in range(length):
            for j in range(i + 1, length):
                number = int(line[i] + line[j])
                if number > higher:
                    higher = number
        result.append(higher)
print(sum(result))
