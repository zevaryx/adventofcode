import re

with open("input.txt") as f:
    data = f.readlines()
    
parser = re.compile(r"(?P<name>[\w]*) .* (?P<speed>[\d]*) .* (?P<time>[\d]+) .* (?P<rest>[\d]+) .*")

seconds = int(input("Enter seconds from prompt: "))

reindeer = []

for line in data:
    match = parser.match(line)
    if not match:
        print(f"LINE DOES NOT MATCH: {line}")
        exit(1)
    name, speed, time, rest = match.groups()
    reindeer.append({"name": name, "speed": int(speed), "time": int(time), "rest": int(rest), "score": 0, "distance": 0, "resting": False, "run_left": int(time), "rest_left": int(rest)})
    
farthest = []

while seconds > 0:
    seconds -= 1
    max_distance = 0
    for deer in reindeer:
        if not deer["resting"]:
            deer["distance"] += deer["speed"]
            deer["run_left"] -= 1
            if deer["run_left"] == 0:
                deer["resting"] = True
        else:
            deer["rest_left"] -= 1
            if deer["rest_left"] == 0:
                deer["run_left"] = deer["time"]
                deer["rest_left"] = deer["rest"]
                deer["resting"] = False
        max_distance = max(max_distance, deer["distance"])
        
    for deer in reindeer:
        if deer["distance"] == max_distance:
            deer["score"] += 1
            
print("Part 1:", max(reindeer, key=lambda x: x["distance"])["distance"])
print("Part 2:", max(reindeer, key=lambda x: x["score"])["score"])
