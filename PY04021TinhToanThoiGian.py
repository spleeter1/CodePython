def convertTime(time):
    if type(time) == int:
        return time
    return int(time[0:2])*60+int(time[3:5])
def convertTimeText(n):
    hour = int(n/60)
    minute = n - hour*60
    return str(hour)+" "+"gio"+" "+str(minute)+" "+"phut" 
n = int(input())
gamers = []
for i in range(n):
    ma = input()
    ten = input()
    vao = input()
    ra = input()
    kq = convertTime(ra) - convertTime(vao)
    gamers.append((ma,ten,kq))

gamers.sort(key = lambda x: -x[2])
for gamer in gamers:
    print(gamer[0],gamer[1],convertTimeText(gamer[2]))
