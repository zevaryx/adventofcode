with open("input.txt") as f:
    data = f.read()
    
floor = data.count("(") - data.count(")")
print(f"{floor=}")

floor = 0
for idx, char in enumerate(data):
    floor += 1 if char == "(" else -1
    if floor == -1:
        idx += 1
        print(f"{idx=}")
        break