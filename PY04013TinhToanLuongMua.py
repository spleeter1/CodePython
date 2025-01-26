def convertTime(time):
    if type(time) == int:
        return time
    return int(time[0:2])*60+int(time[3:5])
class TerminalMeasure:
    def __init__(self,idcode,name,strt,fin,rainfall):
        self.name = name
        self.strt = convertTime(strt)
        self.fin = convertTime(fin)
        self.rainfall = rainfall
        self.idcode = "T"+str(idcode+1).zfill(2)

    def calcRainFall(self):
        timeFinish = convertTime(self.fin)
        timeStrt = convertTime(self.strt)
        ans = self.rainfall/(timeFinish - timeStrt)*60
        ans = "{:.2f}".format(ans)
        return ans
    
    def displayRainFall(self):
        print(self.idcode +" "+ self.name +" "+ self.calcRainFall())

Terminal = []
name_to_id = {}

cnt = 0
n = int(input())
for i in range(n):
    name = input()
    strt = input()
    fin = input()
    rainfall = float(input())

    if name in name_to_id:
        idcode = name_to_id[name]
        Terminal[idcode].rainfall += rainfall
        Terminal[idcode].fin += convertTime(fin)
        Terminal[idcode].strt += convertTime(strt)
    else:
        idcode = len(name_to_id)
        name_to_id[name] = idcode
        Terminal.append(TerminalMeasure(idcode,name,strt,fin,rainfall))

for i in range (len(Terminal)):
    Terminal[i].displayRainFall()

# 10
# Dong Anh
# 07:30
# 08:00
# 60
# Cau Giay
# 07:45
# 08:12
# 50
# Soc Son
# 08:00
# 09:15
# 78
# Dong Anh
# 18:50
# 20:00
# 88
# Cau Giay
# 19:01
# 20:00
# 77
# Soc Son
# 19:06
# 20:21
# 66
# Dong Anh
# 21:00
# 21:40
# 49
# Cau Giay
# 21:50
# 22:20
# 68
# Dong Anh
# 22:15
# 23:45
# 30
# Cau Giay
# 22:50
# 23:45
# 35