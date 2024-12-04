from hashlib import md5

def get_hash(inp: str, modifier: int, zero_count = 5) -> bool:
    h = md5()
    h.update(f"{inp}{modifier}".encode("UTF8"))
    return h.hexdigest().startswith("0" * zero_count)

inp = "bgvyzdsv"
modifier = 0

while not get_hash(inp, modifier):
    modifier += 1
    
print(f"five_zero={modifier}")

modifier = 0
while not get_hash(inp, modifier, zero_count=6):
    modifier += 1
    
print(f"six_zero={modifier}")