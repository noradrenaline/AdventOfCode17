def check_passphrase(words):
    for a in range(len(words)):
        for b in range(a + 1, len(words)):
            if words[a] == words[b]:
                return 1
    return 0


with open('day4.txt') as f:
    total_passphrases= 0
    invalid_passphrases = 0
    for line in f:
        total_passphrases += 1
        invalid_passphrases += check_passphrase(line.split())
    print total_passphrases - invalid_passphrases
