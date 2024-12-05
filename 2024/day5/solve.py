rules = []
updates = []

with open("input.txt") as f:
    for line in f.readlines():
        if "|" in line:
            rules.append([int(line.split("|")[0]), int(line.split("|")[1])])
        elif "," in line:
            updates.append([int(x) for x in line.strip().split(",")])
      
def solve():
    part1 = 0
    part2 = 0
    for update in updates:
        solution = update.copy()
        for page in update:
            for rule in rules:
                if rule[0] == page and rule[1] in update:
                    page_idx = solution.index(rule[0])
                    dep_idx = solution.index(rule[1])
                    if page_idx > dep_idx:
                        solution.pop(page_idx)
                        solution.insert(dep_idx, page)
        if update == solution:
            part1 += solution[len(solution) // 2]
        else:
            part2 += solution[len(solution) // 2]
    print(part1)
    print(part2)
    
solve()
        