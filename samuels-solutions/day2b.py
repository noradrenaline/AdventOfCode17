checksum = 0
def result(row):
    for a in row:
        for b in row:
            if a % b == 0 and a is not b:
                return a / b
with open("day2.txt") as f:
    for line in f:
        checksum += result([int(x) for x in line.rstrip().split('\t')])
print checksum
