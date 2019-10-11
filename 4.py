def buka(File):
    f = open(File)
    l = f.readlines()
    data = []
    for i in l:
        data.append(i.strip('\n'))
    f.close()
    return data
def proses(data):
    result = []
    for i in range(len(data)):
        kata = ''
        for j in range(len(data[i])):
            if len(data[i]) != j + 1:
                if data[i][j] != data[i][j + 1]:
                    kata += data[i][j]
            else:
                kata += data[i][j]
        result.append(kata)
    return result
buka = buka('soal4.txt')
print(proses(buka))