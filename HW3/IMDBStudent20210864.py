import sys
def countGenre(file1, file2):
    f = open(file1, "rt")
    ip = f.read()
    f.close()

    genre = list()
    gcnt = list()
    result = dict()

    rows = ip.split('\n')
    for row in rows:
        fields = row.split("::")
        cnt = 0
        for i in fields:
            if cnt == 2:
                if "|" in i:
                    field = i.split("|")
                    for j in field:
                        if j not in genre:
                            genre.append(j)
                else:
                    if i not in genre:
                        genre.append(i)
            cnt += 1

    for g in genre:
        count = 0
        for row in rows:
            fields = row.split("::")
            cnt = 0
            for i in fields:
                if cnt == 2:
                    if "|" in i:
                        field = i.split("|")
                        for j in field:
                            if j == g:
                                count += 1

                    else:
                        if i == g:
                            count += 1
                cnt += 1
        result[g] = count

    f = open(file2, "wt")
    for key, value in result.items():
        f.write(key)
        f.write(" ")
        f.write(str(value))
        f.write("\n")

    f.close()

    f = open(file2, "rt")
    ip = f.read()
    f.close()
    rows = ip.split('\n')

a, b, c = sys.argv
countGenre(b, c)
