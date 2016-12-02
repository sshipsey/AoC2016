input = [l for l in open('input.txt', 'r').read().split('\n')]
x,y = 0,2
inv = [(0,0),(1,0),(3,0),(4,0),(0,1),(4,1),(0,3),(0,4),(1,4),(3,4),(4,4),(4,3)]

for v in input:
    for m in v:
        if (m == 'L'):
            x -= 1
            if ((x,y) in inv or x < 0):
                x += 1
        if (m == 'R'):
            x += 1
            if ((x,y) in inv or x > 4):
                x -= 1
        if (m == 'D'):
            y += 1
            if ((x,y) in inv or y > 4):
                y -= 1
        if (m == 'U'):
            y -= 1
            if ((x,y) in inv or y < 0):
                y += 1

    print(x, y)
