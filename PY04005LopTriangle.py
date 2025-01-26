# import math

# class Point:
#     def __init__(self,x,y):
#         self.x = (x)
#         self.y = (y) 
#     def distance(self, p2):
#         return math.sqrt(math.pow((self.x - p2.x),2) + math.pow((self.y - p2.y),2))
#         # return "{:.4f}".format(res)
# class Triangle:
#     def __init__(self,p1,p2,p3):
#         self.p1 = Point(p1.x,p1.y)
#         self.p2 = Point(p2.x,p2.y)
#         self.p3 = Point(p3.x,p3.y)
#     def c1(self):
#         return self.p1.distance(self.p2)
#     def c2(self):
#         return self.p1.distance(self.p3)
#     def c3(self):
#         return self.p2.distance(self.p3)
#     def cvi(self):
#         return "{:.3f}".format(self.c1() + self.c2() + self.c3())
#     def kt(self):
#         if self.c1()+self.c2()<=self.c3() or self.c2()+self.c3()<=self.c1() or self.c1()+self.c3()<=self.c2():
#             return False
#         return True
# if __name__ == '__main__':
#     t = int(input())
#     test_cases = []
#     while t > 0:
#         a, b, c, d, e, f = map(float, input().split())
#         p1 = Point(a, b)
#         p2 = Point(c, d)
#         p3 = Point(e, f)
#         test_cases.append((p1, p2, p3))
#         t -= 1
    
#     for test_case in test_cases:
#         tri = Triangle(*test_case)
#         if tri.kt():
#             print(tri.cvi())
#         else:
#             print('INVALID')
