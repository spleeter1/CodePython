# import math
# class PSo:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def rutGon(self):
#         gcd = math.gcd(self.x,self.y)
#         x = self.x/gcd
#         y = self.y/gcd
#         return self
#     def quyDong(self,p2):
#         msc = math.lcm(self.y,p2.y)
#         ts = msc//self.y * self.x + msc//p2.y * p2.x
#         kqTu = ts//math.gcd(ts,msc)
#         kqMau = msc//math.gcd(msc,ts)
#         res = PSo(kqTu,kqMau)
#         return res.rutGon()
# a, b, c, d = map(int, input().split())
# pso = PSo(a,b)
# p2 = PSo(c,d)
# ans = pso.quyDong(p2)
# print(str(ans.x)+ "/"+str(ans.y))
import math

class fract:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def reduce(self):
        gcd = math.gcd(self.tu, self.mau)
        self.tu //= gcd
        self.mau //= gcd
        return self

    def add(self, a):
        mau = self.mau * a.mau // math.gcd(self.mau, a.mau)
        res = fract(self.tu * mau // self.mau + a.tu * mau // a.mau, mau)
        return res.reduce()

a, b, c, d = map(int, input().split())

A = fract(a, b)
B = fract(c, d)

C = A.add(B)

print(str(C.tu) + '/' + str(C.mau))