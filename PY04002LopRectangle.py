class Rectangle:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def perimeter(self):
        return self.x+self.y+self.x+self.y
    def area(self):   
        return self.x*self.y     
    def color(self):
        return self.z[0].upper() + self.z[1:].lower()
if __name__ == '__main__':
    arr = input().split()
    if int(arr[0]) >0 and int(arr[1]) > 0:     
        r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
        print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
    else:
        print("INVALID")