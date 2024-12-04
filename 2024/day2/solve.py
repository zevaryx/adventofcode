with open("input.txt") as f:
    data = [[int(x) for x in y.split(" ")] for y in f.readlines()]

def is_safe(row):
    gaps = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    if set(gaps) <= {1, 2, 3} or set(gaps) <= {-1, -2, -3}:
        return True
    return False

safe_count = sum([is_safe(row) for row in data])
print(safe_count)

safe_count = sum([any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in data])
print(safe_count)