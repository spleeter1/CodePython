def heSo(x):
    tmp = int(x[1:3])
    if 1<=tmp<=3:
        if x[0] == 'A': return 10
        elif x[0] == 'B': return 10
        elif x[0] == 'C' :return 9
        elif x[0] == 'D' : return 8
    elif 4<= tmp<= 8:
        if x[0] == 'A': return 12
        elif x[0] == 'B': return 11
        elif x[0] == 'C' :return 10
        elif x[0] == 'D' : return 9
    elif 9<= tmp <= 15:
        if x[0] == 'A': return 14
        elif x[0] == 'B': return 13
        elif x[0] == 'C' :return 12
        elif x[0] == 'D' : return 11
    elif 16 <= tmp:
        if x[0] == 'A': return 20
        elif x[0] == 'B': return 16
        elif x[0] == 'C' :return 14
        elif x[0] == 'D' : return 13
    
class Employee:
    def __init__(self,ma,name,department,salary):
        self.ma = ma
        self.name = name.strip()
        self.department = department
        self.salary = salary
    def show(self):
        return f"{self.ma} {self.name} {self.department} {self.salary}"
t = int(input())
departments = {}
for _ in range(t):
    pb = list(map(str,input().split()))
    departments[pb[0]] = ' '.join(pb[1:]).strip()
t = int(input())
employees = []
for i in range(0,t):
    ma = input()
    ten = input().strip()
    lcb = int(input())
    ngay = int(input())
    hs = heSo(ma)
    employees.append(Employee(ma,ten,departments[ma[3:]],ngay*hs*lcb*1000))

for nv in employees:
    print(nv.show())