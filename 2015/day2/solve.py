with open("input.txt") as f:
    data = f.readlines()

wrapping_paper = 0
ribbon = 0

for line in data:
    l, w, h = [int(x) for x in line.split("x")[:3]]
    lw = 2*l*w
    lh = 2*l*h
    wh = 2*w*h
    smallest = min(lw, lh, wh) / 2
    wrapping_paper += lw + lh + wh + smallest
    ribbon += sum(sorted([l*2, w*2, h*2])[:2]) + (l*w*h)
    
print(f"{wrapping_paper=}")
print(f"{ribbon=}")
    