f = open("새파일일.txt","a")

for i in range(11,21):
    data = f'{i} 번째 입니다. \n'
    f.write(data)

f.close()
