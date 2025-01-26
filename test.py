test_dict = {'gfg':10,'is': 15,'test':20,'for':10,'geeks':20}
creatSet = set( )
for x in test_dict.values():
    creatSet.add(x)

new_dict = {}
for x in creatSet:
    for key,value in test_dict.items():
        if value == x:
            new_dict[key] = value
            break

print(new_dict)