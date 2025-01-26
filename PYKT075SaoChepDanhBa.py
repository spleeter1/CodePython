def get_sort_key(contact):
        name_parts = contact[0].split()
        last_name = name_parts[-1]
        middle_names = " ".join(name_parts[:-1])
        return (last_name, middle_names)
with open("SOTAY.txt",'r') as f:
    data = [line.strip() for line in f]
    idx=0
    ds = []
    
    while idx < len(data):  
        if data[idx].startswith('Ngay'):
            current_date = data[idx].split()[1]
            idx += 1
        else:
            ten = data[idx]
            sdt = data[idx + 1]
            ds.append((ten, sdt, current_date))
            idx += 2
    ds.sort(key=get_sort_key)

    
    for x in ds:
        print(f"{x[0]}: {x[1]} {x[2]}")
            