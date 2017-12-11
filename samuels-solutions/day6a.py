import collections

with open('day6.txt') as f:
    memory_banks = [int(i) for i in f.read().split()]
    states = collections.defaultdict(int)
    cycles = 0
    total_blocks = [sum(i for i in memory_banks)]
    while True:
        states['-'.join(map(str,memory_banks))] += 1
        if max(states.values()) > 1:
            print cycles
            exit()
        max_bank = 0
        max_blocks = 0
        for index in range(len(memory_banks)):
            if memory_banks[index] > max_blocks:
                max_bank = index
                max_blocks = memory_banks[index]
        memory_banks[max_bank] = 0
        while max_blocks > 0:
            max_bank += 1
            memory_banks[max_bank % len(memory_banks)] += 1
            max_blocks -= 1
        cycles += 1
