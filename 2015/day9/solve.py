from itertools import permutations

places = set()
distances = {}
for line in open('input.txt'):
    (source, _, dest, _, distance) = line.split()
    places.add(source)
    places.add(dest)
    distances.setdefault(source, {})[dest] = int(distance)
    distances.setdefault(dest, {})[source] = int(distance)

shortest = 1_000_000_000
longest = 0
for items in permutations(places):
    dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
    shortest = min(shortest, dist)
    longest = max(longest, dist)

print("shortest: %d" % (shortest))
print("longest: %d" % (longest))