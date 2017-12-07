with open ("input.txt","r") as myfile:
	data = myfile.read().strip()
lstr = len(data)
sum = 0
offset = lstr/2
for i in range (0,lstr):
	char1 = int(data[i])
	char2 = int(data[(i+offset)%lstr])
	if char1==char2:
		sum += char1

print "answer: " + str(sum)



