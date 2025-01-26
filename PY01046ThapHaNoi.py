def thn(n,A,B,C):
    if n==1:
        print(A, '->' ,C)
        return
    thn(n-1,A,C,B)
    print(A, '->' ,C)
    thn(n-1,B,A,C)
    #print(B, '->' ,C)

n = int(input())
thn(n,'A','B','C')
    
    