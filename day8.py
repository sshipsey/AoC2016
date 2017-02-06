import re

class Board:
    def __init__(self):
        self.screen = [[False for x in range(50)] for y in range(6)]
        
        # Test Screen
        #self.screen = [[False for x in range(7)] for y in range(3)]
    
    def toString(self):
        rstr = ''
        for r in self.screen:
            rstr += ''.join(['#' if x else '.' for x in r]) + '\n'
        return rstr
    
    def rotateBoard(self, deg):
        if deg not in [0, 90, 180, 270, 360]: return
        
        if deg > 0: 
            self.screen = [list(x) for x in zip(*self.screen[::-1])]
            self.rotateBoard(deg - 90)

    def turnOn(self, w, h):
        for y in range(h): 
            for x in range(w):   
                self.screen[y][x] = True

    def rotateSlice(self, axis, rowcol, distance):
        if (axis == 'x'):
            self.rotateBoard(90)
            self.screen[rowcol] = rotateList(self.screen[rowcol], -distance)
            self.rotateBoard(270)
        elif (axis == 'y'):
            self.screen[rowcol] = rotateList(self.screen[rowcol], distance)

def rotateList(list, n):
    return list[-n:] + list[:-n]

def getLineType(str):
    if (str.startswith('rect')): return 0
    elif (str.startswith('rotate')): return 1
    else: return -1

def day8(input):
    keypad = Board()

    for l in input.split('\n'):
        if (getLineType(l) == 0):
            m = re.match('rect (\d+)x(\d+)', l).groups()
            keypad.turnOn(int(m[0]), int(m[1]))
        elif (getLineType(l) == 1):
            m = re.match('rotate (row|column) (x|y)=(\d+) by (\d+)', l).groups()
            keypad.rotateSlice(m[1], int(m[2]), int(m[3]))
        else:
            print("Error, invalid line")

    print(keypad.toString())

    return sum((row.count(True) for row in keypad.screen))


testInput = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1"""

input = """rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 6
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 5
rect 2x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 4
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 7
rect 3x1
rotate row y=0 by 3
rect 1x1
rotate row y=0 by 3
rect 1x2
rotate row y=1 by 13
rotate column x=0 by 1
rect 2x1
rotate row y=0 by 5
rotate column x=0 by 1
rect 3x1
rotate row y=0 by 18
rotate column x=13 by 1
rotate column x=7 by 2
rotate column x=2 by 3
rotate column x=0 by 1
rect 17x1
rotate row y=3 by 13
rotate row y=1 by 37
rotate row y=0 by 11
rotate column x=7 by 1
rotate column x=6 by 1
rotate column x=4 by 1
rotate column x=0 by 1
rect 10x1
rotate row y=2 by 37
rotate column x=19 by 2
rotate column x=9 by 2
rotate row y=3 by 5
rotate row y=2 by 1
rotate row y=1 by 4
rotate row y=0 by 4
rect 1x4
rotate column x=25 by 3
rotate row y=3 by 5
rotate row y=2 by 2
rotate row y=1 by 1
rotate row y=0 by 1
rect 1x5
rotate row y=2 by 10
rotate column x=39 by 1
rotate column x=35 by 1
rotate column x=29 by 1
rotate column x=19 by 1
rotate column x=7 by 2
rotate row y=4 by 22
rotate row y=3 by 5
rotate row y=1 by 21
rotate row y=0 by 10
rotate column x=2 by 2
rotate column x=0 by 2
rect 4x2
rotate column x=46 by 2
rotate column x=44 by 2
rotate column x=42 by 1
rotate column x=41 by 1
rotate column x=40 by 2
rotate column x=38 by 2
rotate column x=37 by 3
rotate column x=35 by 1
rotate column x=33 by 2
rotate column x=32 by 1
rotate column x=31 by 2
rotate column x=30 by 1
rotate column x=28 by 1
rotate column x=27 by 3
rotate column x=26 by 1
rotate column x=23 by 2
rotate column x=22 by 1
rotate column x=21 by 1
rotate column x=20 by 1
rotate column x=19 by 1
rotate column x=18 by 2
rotate column x=16 by 2
rotate column x=15 by 1
rotate column x=13 by 1
rotate column x=12 by 1
rotate column x=11 by 1
rotate column x=10 by 1
rotate column x=7 by 1
rotate column x=6 by 1
rotate column x=5 by 1
rotate column x=3 by 2
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 49x1
rotate row y=2 by 34
rotate column x=44 by 1
rotate column x=40 by 2
rotate column x=39 by 1
rotate column x=35 by 4
rotate column x=34 by 1
rotate column x=30 by 4
rotate column x=29 by 1
rotate column x=24 by 1
rotate column x=15 by 4
rotate column x=14 by 1
rotate column x=13 by 3
rotate column x=10 by 4
rotate column x=9 by 1
rotate column x=5 by 4
rotate column x=4 by 3
rotate row y=5 by 20
rotate row y=4 by 20
rotate row y=3 by 48
rotate row y=2 by 20
rotate row y=1 by 41
rotate column x=47 by 5
rotate column x=46 by 5
rotate column x=45 by 4
rotate column x=43 by 5
rotate column x=41 by 5
rotate column x=33 by 1
rotate column x=32 by 3
rotate column x=23 by 5
rotate column x=22 by 1
rotate column x=21 by 2
rotate column x=18 by 2
rotate column x=17 by 3
rotate column x=16 by 2
rotate column x=13 by 5
rotate column x=12 by 5
rotate column x=11 by 5
rotate column x=3 by 5
rotate column x=2 by 5
rotate column x=1 by 5"""

print(day8(input))