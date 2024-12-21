from collections import deque


def update_verifier(update, violations):
    violation_nums = set()
    for page in update:
        if page in violation_nums:
            return 0, page
        elif page in violations.keys():
                violation_nums.update(violations[page])

    middle_index = int(len(update)/2)
    return update[middle_index], -1

def fix(broken, violations):
    bb_list = broken[0].copy()
    invalids = [broken[1]]
    fixed = False
    while not fixed:
        bb_list.remove(invalids[-1])
        mid, pg = update_verifier(bb_list, violations)
        fixed = pg == -1
        if not fixed:
            invalids.append(pg)

    for value in invalids:
        for i in range(len(bb_list)):
            bb_list_ = bb_list.copy()
            bb_list_.insert(i, value)
            mid, pg = update_verifier(bb_list_, violations)
            if pg == -1:
                bb_list = bb_list_
                break
    middle_index = int(len(bb_list)/2)
    return bb_list[middle_index]
    

f = open('input.txt')
data = f.read().splitlines()
ssind = data.index('')

violations = {}
for i in range(ssind):
    req = [int(val) for val in data[i].split('|')]
    if not req[1] in violations.keys():
        violations[req[1]] = [req[0]]
    else:
        violations[req[1]].append(req[0])

total_valids = 0
broken = []
for update in data[ssind+1 : ]:
    upt = [int(val) for val in update.split(',')]
    mid, pg = update_verifier(upt, violations)
    if mid == 0:
        broken.append((upt, pg))
    total_valids += mid
    
    
print(total_valids)


total_invalids = 0
for b in broken:
    total_invalids += fix(b, violations)
    
print(total_invalids)