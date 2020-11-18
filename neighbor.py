import sys

distances = []
s = []
f = open(sys.argv[1])
nameline = f.readline().split()
names = [ nameline[i + 1] for i in range(0, len(nameline) - 1) ]
for i in range (0, len(names)):
	row = f.readline()
	rowList = row.split()
	distances.append([float(x) for x in rowList[1:]])
	s.append(sum([float(x) for x in rowList[1:]]) / (len(names) - 2))

for i in range (0, len(names)):
	print("S(%s): %.4f" %(names[i], s[i]))

closePair = (0, 0, float('inf'))

for i in range (0, len(names)):
	for j in range (0, i):
		print("M(%s)(%s): %.4f" %(names[i], names[j], distances[i][j] - s[i] - s[j]))
		if (distances[i][j] - s[i] - s[j] < closePair[2]):
			closePair = (i, j, distances[i][j] - s[i] - s[j])

print("Closest pair: %s%s: %.4f" %(names[closePair[0]], names[closePair[1]], closePair[2]))
print("S(%s)(U): %.4f" %(names[closePair[0]], (distances[closePair[0]][closePair[1]] + s[closePair[0]] - s[closePair[1]]) / 2))
print("S(%s)(U): %.4f" %(names[closePair[1]], (distances[closePair[0]][closePair[1]] - s[closePair[0]] + s[closePair[1]]) / 2))

output = open(sys.argv[2], "w")
nameline=["X"]
for i in range (0, len(names)):
	if (i != closePair[0] and i != closePair[1]):
		nameline.append("	" + names[i])
nameline.append("	U")
output.write("".join(nameline) + "\n")

lastrowcol = ["U"]

for i in range (0, len(names)):
	if (i != closePair[0] and i != closePair[1]):
		line = [names[i]]
		for j in range (0, len(names)):
			if (j != closePair[0] and j != closePair[1]):
				line.append("	" + str(distances[i][j]))
		entry = str((distances[i][closePair[0]] + distances[closePair[1]][i] - distances[closePair[0]][closePair[1]])/2)
		lastrowcol.append("	" + entry)
		line.append("	" + entry)
		output.write("".join(line) + "\n")

lastrowcol.append("	0.0")
output.write("".join(lastrowcol) + "\n")

