def buka(File):
    f = open(File)
    l = f.readlines()
    data = []
    for i in l:
        data.append(i.rstrip().split(' '))
    f.close()
    return data
def proses(data):
    result = []
    for i in range(len(data)):
        r = 0
        for j in range(len(data[i])):
            if data[i][j] != 'B':
                r += int(data[i][j])
            else:
                r -= int(data[i][j-1])
        result.append(r)
    return result
buka = buka('soal1.txt')
print(proses(buka))