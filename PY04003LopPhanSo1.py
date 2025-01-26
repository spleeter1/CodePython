import math
class PSo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def rutGonMau(self):
        return int(self.y/math.gcd(self.x,self.y))
    def rutGonTu(self):
        return int(self.x/math.gcd(self.x,self.y))

a = input().split()
pso = PSo(int(a[0]),int(a[1]))
print(str(pso.rutGonTu())+"/"+str(pso.rutGonMau()))