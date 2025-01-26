def xulyIndex(s):
    return int(s[(len(s) - 2) :])
class Student:
    def __init__(self,ma,ten,team,trg):
        self.ma = "C0"+ '{:02d}'.format(ma+1)
        self.ten = ten
        self.team = team
        self.trg = trg
school = [0]
for _ in range(int(input())):
    school.append((input(),input()))
students = []
for i in range(int(input())):
    name = input()
    team = input()
    idx = xulyIndex(team)
    students.append(Student(i,name,school[idx][0],school[idx][1]))
students.sort(key=lambda x: x.ten)
for student in students:
    print(f"{student.ma} {student.ten} {student.team} {student.trg}")
