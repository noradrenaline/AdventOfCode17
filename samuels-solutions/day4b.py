import collections

def check_passphrase(words):
    for a in range(len(words)):
        for b in range(a + 1, len(words)):
            if len(words[a]) == len(words[b]):
                x = sorted(list(words[a]))
                y = sorted(list(words[b]))
                invalid = 1
                for i, j in zip(x, y):
                    if i != j:
                        invalid = 0
                if invalid == 1:
                    return 1
    return 0


with open('day4.txt') as f:
    total_passphrases= 0
    invalid_passphrases = 0
    for line in f:
        total_passphrases += 1
        invalid_passphrases += check_passphrase(line.split())
    print total_passphrases - invalid_passphrases
