f = open("inputFile.txt", "r")
count = 0
for line in f:
    line_split = line.split()
    if line_split[2] == "F":

        print(str(count) +" " + line)
        count +=1
f.close()