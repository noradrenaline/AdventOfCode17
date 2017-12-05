dist = 0
n = 1
num = 277678
while num > (n+2)**2:
    n += 2
    dist +=2
n = n**2
if n != num:
    dist += 2
    lower_limit = dist / 2
    upper_limit = dist
    vel = 1
    while n != num:
        n += 1
        if dist == upper_limit:
            vel = -1
        elif dist == lower_limit:
            vel = 1
        dist += vel
print dist
