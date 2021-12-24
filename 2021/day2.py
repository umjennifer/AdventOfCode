# part 2

file = open('input.txt', 'r')
lines = file.readlines()

position = 0
depth = 0
aim = 0

for line in lines:
    line = line.rstrip("\n")
    print(line.split())
    for word in line.split():
        instruction = line.split()[0]
        delta = int(line.split()[1])

    if instruction == "forward":
        position += delta
        depth = depth + (aim * delta)
    elif instruction == "down":
        aim += delta
    else:
        aim -= delta

print("position=", position, "depth=", depth, "position*depth=", position*depth)


# part 1
#
# file = open('input.txt', 'r')
# lines = file.readlines()
#
# position = 0
# depth = 0
#
# for line in lines:
#     line = line.rstrip("\n")
#     print(line.split())
#     for word in line.split():
#         instruction = line.split()[0]
#         delta = int(line.split()[1])
#
#     if instruction == "forward":
#         position += delta
#     elif instruction == "down":
#         depth += delta
#     else:
#         depth -= delta
#
# print("position=", position, "depth=", depth, "position*depth=", position*depth)
