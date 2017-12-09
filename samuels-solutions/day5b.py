import collections

jump_map = collections.defaultdict(int)
with open('day5.txt') as f:
    jump_list = [int(i) for i in f.read().split()]
    pos = 0
    steps = 0
    while (pos >= 0 and pos < len(jump_list)):
        jump = jump_list[pos]
        if jump > 2:
            jump_list[pos] -= 1
        else:
            jump_list[pos] += 1
        pos += jump
        steps += 1
    print steps
