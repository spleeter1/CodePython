n = input().lower()
if n[len(n) - 3:] == ".py":
    print("yes")
else:
    print("no")