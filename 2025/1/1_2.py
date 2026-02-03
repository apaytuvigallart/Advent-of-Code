dial = 50
password = 0

with open("input.txt") as f:
    for line in f:
        direction, steps = line[0], int(line[1:])

        # Calculate how many times it hits 0 in this sequence
        if direction == "R":
            for i in range(steps):
                dial = (dial + i) % 100
                if dial == 0:
                    password += 1
        else:
            for i in range(steps):
                dial = (dial - i) % 100
                if dial == 0:
                    password += 1

print(password)
