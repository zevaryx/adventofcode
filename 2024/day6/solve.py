original_map: list[list[str]] = []
start = [-1, 0]
for line in open("input.txt"):
    row = list(line.strip())
    original_map.append(row)
    if "^" in row:
        start[0] = row.index("^")
    elif start[0] == -1:
        start[1] += 1

map_h = len(original_map)
map_w = len(original_map[0])

# For calculating directional changes
dmap = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
# Print lookups for the output
pmap = {0: "|", 1: "-"}

def navigate(original_map: list[list[str]], save: bool = True, map_name: str = "output.txt") -> tuple[bool, int]:
    """
    Navigate the map.
    
    Args:
        save: Whether to save the final map, default `True`
        map_name: What to save the map as, default `output.txt`
    
    Returns:
        If the guard escaped and the number of unique steps
    """
    # Make a full copy
    guard_map = [[y for y in x] for x in original_map]
    d = 0 #N=0, E=1, S=2, W=3
    pos = [start[0], start[1]]
    last_spot = "."
    escaped = False
    looped = False
    steps = 0
    while True:
        dir_change = False
        new_pos = [pos[0] + dmap[d][0], pos[1] + dmap[d][1]]
        if new_pos[0] < 0 or new_pos[0] > map_w - 1 or new_pos[1] < 0 or new_pos[1] > map_h:
            # We have left the map and bound checked our next calculations
            if last_spot in "|-" or dir_change:
                guard_map[pos[0]][pos[1]] = "+"
            elif d % 2 == 0:
                guard_map[pos[0]][pos[1]] = "|"
            else:
                guard_map[pos[0]][pos[1]] = "-"
            escaped = True
            break
        turn_count = 0
        try:
            while guard_map[new_pos[0]][new_pos[1]] == "#":
                # We need to turn right
                dir_change=True
                d = (d + 1) % 4
                new_pos = [pos[0] + dmap[d][0], pos[1] + dmap[d][1]]
                turn_count += 1
                if turn_count == 4:
                    # Loop! We've gone full circle
                    # This can only occur in 1 unique circumstance
                    looped = True
                    break
        except:
            # This rarely happens when you try to turn on the edge
            # I could fix this but this also works
            escaped = True
        if not looped and not escaped:  
            if last_spot in "|-+" and last_spot != pmap[d%2] or dir_change: 
                guard_map[pos[0]][pos[1]] = "+"
            else:
                guard_map[pos[0]][pos[1]] = pmap[d%2]
            pos = new_pos
            last_spot = guard_map[pos[0]][pos[1]]
            guard_map[pos[0]][pos[1]] = "^"
        steps += 1
        if steps >= map_h * map_w * 10:
            # Naive loop check
            looped = True
            break

    unique = sum(x.count("-") + x.count("|") + x.count("+") for x in guard_map)
    if save:
        # We're saving the map
        guard_map[start[0]][start[1]] = "^"
        path = "\n".join(["".join([x for x in row]) for row in guard_map])
        with open(map_name, "w+") as f:
            f.write(path)
    
    return (escaped, unique)

_, steps = navigate(original_map, map_name="output.part1.txt")
print("Part 1:", steps)

total_looped = 0
attempts = 0
max_tries = (map_w-1) * (map_w-1)
for y in range(map_h - 1):
    for x in range(map_w - 1):
        attempts += 1
        print(f"\rLooking for loops: {attempts:6}/{max_tries}", end="")
        new_map = [[y for y in x] for x in original_map]
        if new_map[y][x] in "^#":
            # No overwrites!
            continue
        new_map[y][x] = "#"
        escaped, _ = navigate(new_map, save=False)
        if not escaped:
            total_looped += 1
print("\nPart 2:", total_looped)