# AoC day 12
def day12(input):
    
    def cpy(cmd):
        regs[cmd[2]] = getVal(cmd[1])
        
    def jnz(cmd, linker):
        if (getVal(cmd[1]) != 0):
            return linker + getVal(cmd[2])
        else:
            return linker + 1

    def inc(cmd):
        regs[cmd[1]] += 1

    def dec(cmd):
        regs[cmd[1]] -= 1
    
    def getVal(v):
        if (v in regs):
            return regs[v]
        else:
            return int(v)

    linker = 0
    regs = {r: 0 for r in 'abcd'}
    regs['c'] = 1
    end = len(input)
    
    while (linker < end):
        cmd = input[linker].split(' ')
        
        if (cmd[0] == 'cpy'):
            cpy(cmd)
            linker += 1
        elif (cmd[0] == 'jnz'):
            linker = jnz(cmd, linker)
        elif (cmd[0] == 'inc'):
            inc(cmd)
            linker += 1
        elif (cmd[0] == 'dec'):
            dec(cmd)
            linker += 1
        else:
            print("Invalid command")


    return regs['a']

input = """cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 14 c
cpy 14 d
inc a
dec d
jnz d -2
dec c
jnz c -5"""

print(day12(input.split('\n')))