import re

with open("input.txt") as f:
    data = f.readlines()
    
lights = [[0]*1000 for i in range(1000)]

def run_command(cmd: str, brightness: bool = False):
    match = re.match(r"(?P<command>[a-z ]*) (?P<start>\d{1,},\d{1,}) through (?P<end>\d{1,},\d{1,})", cmd)
    start = [int(x) for x in match.group("start").split(",")]
    end = [int(x) for x in match.group("end").split(",")]
    command = match.group("command")
    for x in range(start[0], end[0]+1, 1):
        for y in range(start[1], end[1]+1, 1):
            if command == "turn on":
                if brightness:
                    lights[x][y] = lights[x][y] + 1
                else:
                    lights[x][y] = 1
            elif command == "turn off":
                if brightness:
                    lights[x][y] = max(lights[x][y] - 1, 0)
                else:
                    lights[x][y] = 0
            elif command == "toggle":
                if brightness:
                    lights[x][y] = lights[x][y] + 2
                else:
                    lights[x][y] = (lights[x][y] + 1) % 2
            else:
                print(f"Unknown command: {command}")
                exit(1)
                
for line in data:
    run_command(line)

print(f"lights_on={sum(x >= 1 for row in lights for x in row)}")

lights = [[0]*1000 for i in range(1000)]
for line in data:
    run_command(line, True)
    
print(f"brightness={sum(x for row in lights for x in row)}")