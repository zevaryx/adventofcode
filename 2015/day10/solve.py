inp = "3113322113"

def do_loop(src, count=40):
    inp = src
    outp = ""
    for _ in range(count):
        idx = 0
        for i in range(len(inp)):
            if i < idx:
                continue
            counter = 0
            while inp[i] == inp[idx]:
                counter += 1
                idx += 1
                if idx == len(inp):
                    break
            outp += f"{counter}{inp[i]}"
        inp = outp
        outp = ""
    return inp
        
print("40:", len(do_loop(inp)))
print("50:", len(do_loop(inp, 50)))