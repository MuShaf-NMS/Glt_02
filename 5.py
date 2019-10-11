def buka(File):
    f = open(File)
    l = f.readlines()
    data = []
    for i in l:
        data.append(i.strip('\n').split(' '))
    f.close()
    return data
def proses(data):
    result = []
    for i in range(len(data)):
        posisi = 0
        for j in range(len(data[i])):
            k = False
            if int(data[i][j]) == 6:
                posisi += int(data[i][j])
                a = j
                k = True
                break
        while k:
            a += 1
            posisi += int(data[i][a])
            if posisi % 7 == 0:
                posisi = 1
            if posisi % 17 == 0:
                posisi = 100
            if posisi == 100:
                break
            if a == len(data[i])-1:
                break
        result.append(posisi)
    return result
b = buka('soal5.txt')
print(proses(b))
