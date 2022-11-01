import sys
def uberInfo(file1, file2):
    from datetime import datetime, date

    f = open(file1, "rt")
    ip = f.read()
    f.close()

    uList = list()
    uDict = dict()
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
        key = f1 + "," + days[day]
        if key not in uDict:
            value = f3 + "," + f4
            uDict[key] = value
        else:
            val3, val4 = uDict[key].split(",")
            v3 = int(val3)
            v4 = int(val4)
            v3 += int(f3)
            v4 += int(f4)
            value = str(v3) + "," + str(v4)
            uDict[key] = value

    f = open(file2, "wt")
    for k in uDict:
        f.write(k)
        f.write(" ")
        f.write(uDict[k])
        f.write("\n")
    f.close()

a, b, c = sys.argv
uberInfo(b, c)

