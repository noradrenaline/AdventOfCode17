import math

input = 289326

nextsquare = math.ceil(input**(1./2)) 
nextsquare = nextsquare + (1-nextsquare%2)

lastsquare = nextsquare - 2
sideprogress = (input-lastsquare**2)%(nextsquare-1)

base = (nextsquare-1)/2
additional = abs((nextsquare-1)/2 - sideprogress)

distance = base+additional
print distance
