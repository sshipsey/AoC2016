from hashlib import md5

def part1(input):
    hash = ''
    index = 0
    m = md5()
    password = ''
    
    while(len(password) < 8):
        m.update(str.encode(str(input) + str(index)))
        hash = m.hexdigest()
        if (hash.startswith('00000')):
            password += str(hash[5])
        index += 1
        m = md5()
        
    return ''.join(password)

def part2(input):
    hash = ''
    index = 0
    m = md5()
    password = [None for _ in range(8)]
    
    while(not all(password)):
        m.update(str.encode(str(input) + str(index)))
        hash = m.hexdigest()
        if (hash.startswith('00000')):
            try:
                if (not password[int(hash[5])]):
                    password[int(hash[5])] = hash[6]
            except:
                pass
        index += 1
        m = md5()
        
    return ''.join(password)
    
input = open('input.txt', 'r').read()
print(part1(input))
print(part2(input))