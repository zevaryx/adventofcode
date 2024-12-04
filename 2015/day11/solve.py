import re

inp = "vzbxkghb"

def check_password(pwd: str) -> bool:
    if any(x in pwd for x in "oil"):
        return False
    if len(re.findall(r"(.)\1", pwd)) < 2:
        return False
    
    for i in range(len(pwd)-2):
        if ord(pwd[i])+1 == ord(pwd[i+1]) and ord(pwd[i])+2 == ord(pwd[i+2]):
            return True
        
    return False

def solve(pwd: str) -> str:
    inp = pwd
    while not check_password(inp):
        inp = list(inp)
        for idx in range(len(inp)-1, -1, -1):
            if inp[idx] == "z":
                inp[idx] = "a"
            else:
                inp[idx] = chr(ord(inp[idx])+1)
                break
        inp = "".join(inp)
    return inp
            
new_pwd = solve(inp)
print(new_pwd)

new_pwd = list(new_pwd)
for idx in range(len(new_pwd)-1, -1, -1):
    if new_pwd[idx] == "z":
        new_pwd[idx] = "a"
    else:
        new_pwd[idx] = chr(ord(new_pwd[idx])+1)
        break
new_pwd = "".join(new_pwd)

print(solve(new_pwd))