from hashlib import md5

def part1(input):
    index, password = 0, ''
    
    while(len(password) < 8):   
        hash = md5(str.encode(str(input) + str(index))).hexdigest()
        if (hash.startswith('00000')):
            password += str(hash[5])
        index += 1
        
    return password

def part2(input):
    index, password = 0, [None] * 8
    
    while(not all(password)):
        hash = md5(str.encode(str(input) + str(index))).hexdigest()
        if (hash.startswith('00000') and hash[5].isdigit() and int(hash[5]) < 8 and password[int(hash[5])] is None):
            password[int(hash[5])] = hash[6]
        index += 1
        
    return ''.join(password)

def day5(input):
    return part1(input), part2(input)
    
input = open('input.txt', 'r').read()

a = day5(input)
print(str.format('Part 1: {0}\nPart 2: {1}', a[0], a[1]))