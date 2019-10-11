def buka(File):
    f = open(File)
    l = f.readlines()
    data = []
    for i in l:
        data.append(i.strip('\n'))
    f.close()
    return data
def permute(l,head=[],t=[]):
    sz = len(l)
    if sz == 1:
        result = head+l
        t.append(result)
    else:
        for i in range(sz):
            new_head = head.copy()
            new_head.append(l[i])
            new_l = l.copy()
            new_l.pop(i)
            permute(new_l,new_head)
    return t
def proses(data):
    result = []
    for i in range(len(data)):
        p = []
        #mengubah string menjadi list agar bisa digunakan fungsi permute
        for j in range(len(data[i])):
            p.append(data[i][j])
        #melakukan permutasi dengan funsi permute
        perm = permute(p)
        hp = []
        #mengubah list hasil permute menjadi string dan ditampung di pariabel hp
        for j in range(len(perm)):
            e = ''
            for k in range(len(perm[j])):
                e += perm[j][k]
            hp.append(e)
        r = 0
        for j in range(len(hp)):
            if int(data[i]) < int(hp[j]):
                r += 1
        result.append(r)
    return (result)
buka = buka('soal2.txt')
print(proses(buka))