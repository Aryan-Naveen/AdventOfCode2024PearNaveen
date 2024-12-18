import numpy as np

def perform(comm):
    comma = comm.find(',')
    close = comm.find(')')
    if comm[:4] == 'mul(' and comma != -1 and close != -1:
        val1 = comm[4:comma]
        val2 = comm[comma +1:close]
        if val1.isdigit() and val2.isdigit():
            return int(val1) * int(val2)
        
    return 0

def extract_mul(command, active):
    ind = command.find('mul')
    do_ind = command.rfind('do()', 0, ind)
    dont_ind = command.rfind("don't()", 0, ind)
    newcom = command[ind+1:] if ind != -1 else command
    
    val = 0
    if ind != -1:
        if do_ind != -1 and dont_ind != -1:
            active = do_ind > dont_ind
        elif dont_ind != -1:
            active = False
        elif do_ind != -1:
            active = True

        if active:
            mul = command[ind:]
            val = perform(mul)
    
    
    return ind != -1, newcom, val, active


f = open('input.txt')
data = f.read()
active = True

found, com, val, active = extract_mul(data, active)
total = val

while found:
    found, com, val, active = extract_mul(com, active)
    total += val

print(total)

