def process_file(filename):
    with open(filename,'r') as f:
        data = {line.strip().lower() for line in f}

    emails= sorted(data)
    for x in emails:
        print(x)

filename = "CONTACT.in"
process_file(filename)