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

    region = [i[0] for i in uList]
    region = set(region)

    for r in region:
        c = []
        for u in uList:
            if r == u[0]:
                c.append(u[1])
        c = list(set(c))
        uDict[r] = c

    result = list()

    for ud in uDict:
        for uv in uDict[ud]:
            vehicles = 0
            trips = 0
            for i in uList:
                if ud == i[0] and uv == i[1]:
                    vehicles += int(i[2])
                    trips += int(i[3])

            result.append([ud, uv, vehicles, trips])

    f = open(file2, "wt")
    cnt = 0
    for row in rows:
        for frr in result:
            fc = 0
            for fr in frr:
                f.write(str(fr))
                if fc == 1:
                    f.write(" ")
                elif fc == 3:
                    f.write("\n")
                else:
                    f.write(",")
                fc += 1
        cnt += 1

    f.close()

a, b, c = sys.argv
uberInfo(b, c)

