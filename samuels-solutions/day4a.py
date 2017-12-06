def check_passphrase(words):
    for a in range(len(words)):
        for b in range(a + 1, len(words)):
            if words[a] == words[b]:
                return 1
    return 0


with open('day4.txt') as f:
    total = 0
    for line in f:
        total += check_passphrase(line.split())
    print total
