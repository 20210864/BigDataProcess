def uberInfo(file1, file2):
    from datetime import datetime, date
    f = open(file1, "rt")
    ip = f.read()
    f.close()

    rows = ip.split('\n')
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    f = open(file2, "wt")

    for row in rows:
        fields = row.split(",")
        f.write(fields[0])
        f.write(",")
        a = fields[1].split("/")
        year = int(a[2])
        mon = int(a[0])
        d = int(a[1])
        day = date(year, mon, d).weekday()
        f.write(days[day])
        f.write(" ")
        f.write(fields[2])
        f.write(",")
        f.write(fields[3])
        f.write("\n")

    f.close()

    f = open(file2, "rt")
    ip = f.read()
    f.close()
    rows = ip.split('\n')

    for row in rows:
        print(row)

a, b = input().split()
uberInfo(a, b)
