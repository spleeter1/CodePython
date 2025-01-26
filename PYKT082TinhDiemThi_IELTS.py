def calc(correct_answers):
    if correct_answers >= 39:
        return 9.0
    elif correct_answers >= 37:
        return 8.5
    elif correct_answers >= 35:
        return 8.0
    elif correct_answers >= 33:
        return 7.5
    elif correct_answers >= 30:
        return 7.0
    elif correct_answers >= 27:
        return 6.5
    elif correct_answers >= 23:
        return 6.0
    elif correct_answers >= 20:
        return 5.5
    elif correct_answers >= 16:
        return 5.0
    elif correct_answers >= 13:
        return 4.5
    elif correct_answers >= 10:
        return 4.0
    elif correct_answers >= 7:
        return 3.5
    elif correct_answers >= 5:
        return 3.0
    elif correct_answers >= 3:
        return 2.5
for i in range (int(input())):
    a = input().split()
    a[0] = calc(int(a[0]))
    a[1] = calc(int(a[1]))
    a[2] = float(a[2])
    a[3] = float(a[3])
    x = sum(a)/4
    tmp = x - int(x)
    if tmp >= 0.75:
        x = float(int(x)+1)
    elif tmp >=0.25:
        x = float(int(x)+0.5)
    else:
        x = float(int(x))
    print(x)