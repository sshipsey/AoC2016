i = [l for l in open('input.txt', 'r').read().split(', ')]
x, y = 0, 0
d = 1
vis = [(0,0)]
for v in i:
    t = v[0]
    if (t == 'R'):
        d += 1
    if (t == 'L'):
        d -= 1
    if (d < 1):
        d = 4
    if (d > 4):
        d = 1
    if (d == 1):
        for _ in range(int(v[1:])):
            y += 1
            if ((x,y) in vis):
                print(abs(x) + abs(y))
            vis.append((x,y))
    if (d == 2):
        for _ in range(int(v[1:])):
            x += 1
            if ((x,y) in vis):
                print(abs(x) + abs(y))
            vis.append((x,y))
    if (d == 3):
        for _ in range(int(v[1:])):
            y -= 1
            if ((x,y) in vis):
                print(abs(x) + abs(y))
            vis.append((x,y))
    if (d == 4):
        for _ in range(int(v[1:])):
            x -= 1
            if ((x,y) in vis):
                print(abs(x) + abs(y))
            vis.append((x,y))
        