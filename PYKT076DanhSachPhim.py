from datetime import datetime
def xulyIndex(s):
    return int(s[(len(s) - 2) :])
class Movie:
    def __init__(self,ma,types,date,name,espi):
        self.ma = "P00"+ '{:01d}'.format(ma+1)
        self.types = types
        self.date =  datetime.strptime(date,'%d/%m/%Y')
        self.name    = name
        self.espi  = espi
def formattedDate(tmp):
    tmp = str(tmp)[:10]
    tmp = tmp. split('-')
    tmp = ''+tmp[2] + "/"+tmp[1]+'/'+tmp[0]
    return tmp
types = [0]
n,m = map(int,input().split())
for i in range(n):
    types.append(input())
movies = []
for i in range(m):
    tl = input()
    date = input()
    name = input()
    espi = int(input())
    idx = xulyIndex(tl)
    movies.append(Movie(i,types[idx],date,name,espi))
movies.sort(key=lambda x: (x.date,x.name,-x.espi))
for movie in movies:
    
    print(f"{movie.ma} {movie.types} {formattedDate(movie.date)} {movie.name} {movie.espi}")