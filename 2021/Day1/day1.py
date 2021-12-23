file = open('input.txt', 'r')
lines = file.readlines()
lines = [int(line) for line in lines]

window_increased = 0;
for i, line in enumerate(lines[:len(lines)-3]):
    first_window = lines[i]
    second_window = lines[i+3]
    if second_window > first_window:
        window_increased += 1

print("window_increased", window_increased)
