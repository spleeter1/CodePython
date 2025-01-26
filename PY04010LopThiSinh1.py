class ThiSinh:
    def __init__(self,name,birth,diem1,diem2,diem3):
        self.name = name
        self.birth = birth
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3
    
    def diem(self):
        return float("{:.1f}".format( self.diem1 + self.diem2 + self.diem3))
    def display(self):
        print(self.name+' '+self.birth+' '+str(self.diem()))

# a = input()
# print(a)
name = input()
birth = input()
diem1 = float(input())
diem2 = float(input())
diem3 = float(input())
ThiSinh(name, birth, diem1, diem2, diem3).display()

