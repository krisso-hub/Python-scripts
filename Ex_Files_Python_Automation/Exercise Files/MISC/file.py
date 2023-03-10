# this program open file and read through it and split the into two files of pass and fail
f = open('inputFile.txt', 'r')
passfile = open('passfile.txt', 'w')
failfile = open('failfile.txt', 'w')
for line in f:
    line_split = line.split()
    if line_split[2] == "P":
        print(passfile.write(line))
    else:
        print(failfile.write(line))
    
f.close()
passfile.close()
failfile.close()
  