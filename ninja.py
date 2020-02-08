class Maze:
    def __init__(self,size,wall,start,target):
        self.size = size
        self.wall = wall
        self.start = start
        self.target = target
        self.postart = []
        self.posend = []
        self.labirin = []
        self.peta = []

        self.buat_labirin()
        self.titik()
        self.floodfill(self.postart)
        self.solve
    
    def buat_labirin(self):
        count = []
        for i in range(0,self.size**2,self.size):
            a = []
            for j in range(i+1,i+self.size+1):
                a.append(j)
            count.append(a)
        for i in range(len(count)):
            for j in range(len(count[i])):
                if count[i][j] in wall:
                    count[i][j] = 0
        self.labirin = count

    def titik(self):
        lab = self.labirin
        copy = []
        l = len(lab)
        for i in range(l):
            a = []
            for j in range(l):
                if lab[i][j] == self.start and len(self.postart) < 2:
                    a.append('S')
                    self.postart.append(i)
                    self.postart.append(j)
                elif lab[i][j] == self.target:
                    a.append('E')  
                    self.posend.append(i)
                    self.posend.append(j)  
                elif lab[i][j] != 0 and lab[i][j] != 'S' and lab[i][j] != 'E':
                    a.append(' ')
                else:
                    a.append(0)
            copy.append(a)
        self.peta = copy
        return copy

    def floodfill(self,now,a=0):
        a += 1
        i = now[0]
        j = now[1]
        lab = self.peta
        if lab[i-1][j] == ' ':
            lab[i-1][j] = a
            self.floodfill([i-1,j],a)
        if lab[i+1][j] == ' ':
            lab[i+1][j] = a
            self.floodfill([i+1,j],a)
        if lab[i][j+1] == ' ':
            lab[i][j+1] = a
            self.floodfill([i,j+1],a)
        if lab[i][j-1] == ' ':
            lab[i][j-1] = a
            self.floodfill([i,j-1],a)

    def solve(self):
        result = []
        end = self.posend
        lab = self.peta
        a = 0
        i = end[0]
        j = end[1]
        if lab[i-1][j] != 0:
            i -= 1
            a = lab[i][j]
        elif lab[i+1][j] != 0:
            i += 1
            a = lab[i][j]
        elif lab[i][j+1] != 0:
            j += 1
            a = lab[i][j]
        elif lab[i][j-1] != 0:
            j -= 1
            a = lab[i][j]
        result.append(self.labirin[i][j])
        for h in range(a-1):
            if lab[i-1][j] == a-1:
                i -= 1
                a -= 1
                result.insert(0,self.labirin[i][j])
            elif lab[i+1][j] == a-1:
                i += 1
                a -= 1
                result.insert(0,self.labirin[i][j])
            elif lab[i][j+1] == a-1:
                j += 1
                a -= 1
                result.insert(0,self.labirin[i][j])
            elif lab[i][j-1] == a-1:
                j -= 1
                a -= 1
                result.insert(0,self.labirin[i][j])
        return result

wall = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,24,27,31,32,36,40,41,43,44,45,49,54,56,57,58,60,61,63,67,68,69,70,71,72,74,75,76,80,81,83,85,87,91,92,96,98,99,100,101,105,107,108,109,112,114,120,121,123,124,125,127,131,134,135,136,137,139,140,141,142,143,147,149,154,159,160,161,163,165,166,167,169,170,172,174,176,178,179,180,181,183,185,190,192,196,197,199,200,201,206,207,210,212,213,214,217,220,221,222,223,224,230,231,232,237,238,240,241,245,246,247,248,250,252,254,255,260,261,263,268,270,275,277,278,279,280,281,283,284,285,290,291,292,293,297,300,301,305,307,308,309,310,313,316,317,318,320,321,322,323,325,332,333,334,338,340,341,343,345,347,349,350,352,356,357,358,360,361,365,368,369,374,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400]
print(Maze(20,wall,23,298).solve())