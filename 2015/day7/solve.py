import re

with open("input.txt") as f:
    data = f.readlines()
    
parser = re.compile(r"(?P<reg_1>[a-z]{1,}|\d{1,})? ?(?P<op>[A-Z]{1,})? ?(?P<reg_2>[a-z]{1,}|\d{1,})? ?-> (?P<dest>[a-z]{1,})")
check_int = re.compile(r"^\d*$")

commands = {}
registers = {}
ops = {
    "NOT": lambda _, y: ~y,
    "OR": lambda x, y: x | y,
    "AND": lambda x, y: x & y,
    "XOR": lambda x, y: x ^ y,
    "RSHIFT": lambda x, y: x >> y,
    "LSHIFT": lambda x, y: x << y,
}

for line in data:
    line = line.strip()
    match = parser.match(line)
    if not match:
        print(f"LINE DID NOT MATCH: {line}")
        exit(1)
    reg_1 = match.group("reg_1")
    op = match.group("op")
    reg_2 = match.group("reg_2")
    dest = match.group("dest")
    commands[dest] = {"reg_1": reg_1, "reg_2": reg_2, "op": op}

    
def solve_for(dest: str) -> int:
    global registers
    data = commands[dest]
    if dest not in registers:
        reg_1 = data.get("reg_1")
        reg_1_value = None
        reg_2 = data.get("reg_2")
        reg_2_value = None
        op = data.get("op")
        if reg_1 and check_int.match(reg_1):
            reg_1_value = int(reg_1)
        elif reg_1:
            reg_1_value = registers.get(reg_1, solve_for(reg_1))
        if reg_2 and check_int.match(reg_2):
            reg_2_value = int(reg_2)
        elif reg_2:
            reg_2_value = registers.get(reg_2, solve_for(reg_2))
        if op:
            registers[dest] = ops[op](reg_1_value, reg_2_value)
        else:
            registers[dest] = reg_1_value
    return registers[dest]

a = solve_for("a")
print(f"{a=}")

commands["b"] = {"reg_1": str(a), "reg_2": None, "op": None}
registers = {}
b_a = solve_for("a")
print(f"{b_a=}")