with open("input.txt") as f:
    data = f.readlines()
    list1 = sorted([int(x.strip().split("   ")[0]) for x in data])
    list2 = sorted([int(x.strip().split("   ")[1]) for x in data])

distance = 0
simularity = 0

for idx in range(len(list1)):
    distance += abs(list1[idx] - list2[idx])
    simularity += list1[idx] * list2.count(list1[idx])

print(distance)
print(simularity)
