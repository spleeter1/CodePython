t=int(input())
for i in range(t):
    day,month=map(int,input().split())
    if(month==1):
        if day>=1 and day<=19:
            print("Ma Ket")
        elif day>=20 and day<=31:
            print("Bao Binh")
    elif month==2:
        if day>=1 and day<=18:
            print("Bao Binh")
        elif day>=19 and day<=28:
            print("Song Ngu")
    elif month==3:
        if day>=1 and day<=20:
            print("Song Ngu")
        elif day>=21 and day<=31:
            print("Bach Duong")
    elif month==4:
        if day>=1 and day<=19:
            print("Bach Duong")
        elif day>=20 and day<=30:
            print("Kim Nguu")
    elif month==5:
        if day>=1 and day<=20:
            print("Kim Nguu")
        elif day>=21 and day<=31:
            print("Song Tu")
    elif month==6:
        if day>=1 and day<=20:
            print("Song Tu")
        elif day>=21 and day<=30:
            print("Cu Giai")
    elif month==7:
        if day>=1 and day<=22:
            print("Cu Giai")
        elif day>=23 and day<=31:
            print("Su Tu")
    elif month==8:
        if day>=1 and day<=22:
            print("Su Tu")
        elif day>=23 and day<=31:
            print("Xu Nu")
    elif month==9:
        if day>=1 and day<=22:
            print("Xu Nu")
        elif day>23 and day<=30:
            print("Thien Binh")
    elif month==10:
        if day>=1 and day<=22:
            print("Thien Binh")
        elif day>=23 and day<=31:
            print("Thien Yet")
    elif month==11:
        if day>=1 and day<=22:
            print("Thien Yet")
        elif day>=23 and day<=30:
            print("Nhan Ma")
    elif month==12:
        if day>=1 and day<=21:
            print("Nhan Ma")
        if day>=22 and day<=31:
            print("Ma Ket")
