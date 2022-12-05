from operator import indexOf

elves = []

with open("data.txt", "r") as data:
    calories = 0

    for line in data.readlines():
        if line != '\n':
            calories += int(line)
        else:
            elves.append(calories)
            calories = 0

print(max(elves))