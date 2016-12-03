i = [[int(x) for x in v.split()] for v in open('input.txt', 'r').read().split('\n')]

# Part 1
c = 0
for v in i:
    if (v[0] + v[1] > v[2] and v[1] + v[2] > v[0] and v[0] + v[2] > v[1]):
        c += 1
print(c)

# Part 2
c, x, y, l = 0, 0, 0, []
for x in range(3):
    for y in range(len(i)):
        l.append(i[y][x])
        if (len(l) == 3):
            if (l[0] + l[1] > l[2] and l[1] + l[2] > l[0] and l[0] + l[2] > l[1]):
                c += 1
            l = []
print(c)