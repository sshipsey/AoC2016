import itertools

def atob(a):
    b = a[::-1]
    b = "".join([str(int(not int(c))) for c in b])
    return "".join([a, "0", b])

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.zip_longest(fillvalue=fillvalue, *args)

def compress(groups):
    a = []
    for g in groups:
        if (all(x==g[0] for x in g)):
            a.append('1')
        else:
            a.append('0')
    return "".join(a)
        
    
def day16(diskContents, diskLength):
    disk = len(diskContents)
    
    while (disk <= diskLength):
        diskContents = atob(diskContents)
        disk = len(diskContents)
        
    diskContents = diskContents[:diskLength]
    pairs = grouper(diskContents, 2)
    
    checksum = compress(pairs)
    
    while(len(checksum) % 2 == 0):
        checksum = compress(grouper(checksum, 2))
        
    return checksum

input = "10001110011110000"
print(day16(input, 272), day16(input, 35651584))