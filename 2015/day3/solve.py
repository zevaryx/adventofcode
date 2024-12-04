with open("input.txt") as f:
    data = f.read()
    
visited = [[0,0],]
unique = [[0,0],]

santa = [[0,0],]
robo_santa = [[0,0],]
second_unique = [[0,0],]

for idx, char in enumerate(data):
    
    modifier = [0, 0]
    if char == "^":
        modifier = [0, 1]
    elif char == "v":
        modifier = [0, -1]
    elif char == ">":
        modifier = [1, 0]
    elif char == "<":
        modifier = [-1, 0]
    else:
        print(f"Invalid character {char}")
    cur_pos = visited[-1].copy()
    cur_pos = [cur_pos[0] + modifier[0], cur_pos[1] + modifier[1]]
    if cur_pos not in unique:
        unique.append(cur_pos)
    visited.append(cur_pos)
    if idx % 2 == 0:
        cur_pos = santa[-1].copy()
        cur_pos = [cur_pos[0] + modifier[0], cur_pos[1] + modifier[1]]
        santa.append(cur_pos)
    else:
        cur_pos = robo_santa[-1].copy()
        cur_pos = [cur_pos[0] + modifier[0], cur_pos[1] + modifier[1]]
        robo_santa.append(cur_pos)
    if cur_pos not in second_unique:
        second_unique.append(cur_pos)

print(f"{len(unique)=}")
print(f"{len(second_unique)=}")