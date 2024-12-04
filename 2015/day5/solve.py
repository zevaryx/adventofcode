import re

with open("input.txt") as f:
    data = f.readlines()
    
def nice_string(inp: str) -> bool:
    inp = inp.strip()
    
    vowel_finder = re.search(r"(.*[aeiou]){3}", inp) is not None
    bad_combos = re.search(r"ab|cd|pq|xy", inp) is None
    duplicate = re.search(r"(.)\1", inp) is not None
        
    return vowel_finder and bad_combos and duplicate

def nice_string_2(inp: str) -> bool:
    inp = inp.strip()
    
    doubles = re.search(r"(..).*\1", inp) is not None
    palins = re.search(r"(.).\1", inp) is not None
    
    return doubles and palins

nice_count = sum([nice_string(x) for x in data])

print(f"{nice_count=}")

nice_count_2 = sum([nice_string_2(x) for x in data])

print(f"{nice_count_2=}")