from re import search
from collections import Counter

def isMatch(str, chk):
    c = Counter( str )
    d = sorted( {(c[a] * -1, a) for a in str} )
    return chk == ''.join( [x[1] for x in d[:5]] ) 

def part1(input):
    total = 0

    for l in input:
        name = ''.join( l.split('-')[:-1] )

        value = int( search('\d+(?=\[)', l).group(0) )

        checksum = l[l.find('[') + 1 : l.find(']')]

        if (isMatch(name, checksum)):
            total += value

    return total
    

def part2(input):
    for l in input:
        sentence = l.split('-')[:-1]
        value = int( search('\d+(?=\[)', l).group(0) )

        newName = ' '.join([''.join([chr(((ord(char) - 97 + value) % 26) + 97) for char in word]) for word in sentence])
        
        if ('northpole' in newName.lower()):
            print(newName)
            return value

input = [v for v in open('input.txt', 'r').read().split('\n')]

print(part1(input))
print(part2(input))