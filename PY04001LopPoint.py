import math

class Point:
    def __init__(self,x,y):
        self.x = (x)
        self.y = (y) 
    def distance(self, p2):
        res = math.sqrt(math.pow((self.x - p2.x),2) + math.pow((self.y - p2.y),2))
        #return round(res,4)
        return "{:.4f}".format(res)
    
def Decimal(x):
    return float(x)
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1

