dial = 50
password = 0

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        direction = line[0]
        steps = int(line[1:])
        if direction == "R":
            dial = (dial + steps) % 100
        else:
            dial = (dial - steps) % 100
        if dial == 0:
            password += 1
print(password)
