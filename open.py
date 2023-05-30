f = open("새파일일.txt", 'w')
for i in range(1,11):
    data = "%d 번째 줄입니다. \n" %i
    f.write(data)

f.close()