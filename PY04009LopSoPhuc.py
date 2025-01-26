class soPhuc:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def add(self,other):
        return soPhuc(self.real+other.real,self.imag+other.imag)
    def mul(self,other):
        real_result =  self.real * other.real - self.imag * other.imag
        imag_result =  self.real * other.imag + self.imag * other.real
        return soPhuc(real_result,imag_result)
    def show(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"
t = int(input())
while(t>0):
    arr = list(map(int,input().split()))
    A = soPhuc(arr[0],arr[1])
    B = soPhuc(arr[2],arr[3])

    C = (A.add(B)).mul(A)
    D = (A.add(B)).mul((A.add(B)))
    t-=1
    print(f"{C.show()}, {D.show()}")                

