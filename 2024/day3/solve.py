import re

with open("input.txt") as f:
    commands = f.read()
    
command = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|(do(?:n't)?\(\))")

def search(ignore_switches: bool = True):
    total = 0
    do = True
    for match in command.findall(commands):
        if match[2] == 'do()':
            do = True
            continue
        elif match[2] == "don't()":
            do = False
            continue
        if do or ignore_switches:
            total += int(match[0]) * int(match[1])
    return total
        
print(search())
print(search(False))