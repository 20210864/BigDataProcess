def uberInfo(file1, file2):
    from datetime import datetime, date

    f = open(file1, "rt")
    ip = f.read()
    f.close()

    uList = list()
    rows = ip.split('\n')
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    for row in rows:
        fields = row.split(",")
        count = 0
        for i in fields:
            if count == 0:
                f1 = i
            elif count == 1:
                f2 = i
            elif count == 2:
                f3 = i
            else:
                f4 = i
            count += 1

        a = f2.split("/")
        year = int(a[2])
        mon = int(a[0])
        d = int(a[1])
        day = date(year, mon, d).weekday()
        uList.append([f1, days[day], f3, f4])

    f = open(file2, "wt")
    cnt = 0
    for row in rows:
        f.write(uList[cnt][0])
        f.write(",")
        f.write(uList[cnt][1])
        f.write(" ")
        f.write(uList[cnt][2])
        f.write(",")
        f.write(uList[cnt][3])
        f.write("\n")
        cnt += 1

    f.close()

a, b = input().split()
uberInfo(a, b) 
