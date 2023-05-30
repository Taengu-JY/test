f = open("새파일일.txt", 'r')
line = f.readline()
print(line)
line = f.readline()
print(line)
line = f.readline()
print(line)

lines = f.readlines()

for l in lines:
    print(l)


f.close()
