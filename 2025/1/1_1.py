dial = 50
password = 0

with open("input.txt") as f:
    for line in f:
        direction, steps = line[0], int(line[1:])

        # Calculate how many times it finishes at 0
        if direction == "R":
            dial = (dial + steps) % 100
        else:
            dial = (dial - steps) % 100
        if dial == 0:
            password += 1
print(password)
