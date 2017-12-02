checksum = 0
with open("day2.txt") as f:
    for line in f:
        row = [int(x) for x in line.rstrip().split('\t')]
        checksum += max(row) - min(row)
print checksum
