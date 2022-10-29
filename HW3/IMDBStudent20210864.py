def countGenre(file1, file2):
    f = open(file1, "rt")
    ip = f.read()
    f.close()

    genre = list()
    gcnt = list()
    result = dict()
    count = 0

    rows = ip.split('\n')
    for row in rows:
        fields = row.split("::")
        if "|" in fields[2]:
            field = fields[2].split("|")
            for j in field:
                if j not in genre:
                    genre.append(j)
        else:
            if fields[2] not in genre:
                genre.append(fields[2])

    for i in genre:
        for row in rows:
            fields = row.split("::")
            if "|" in fields[2]:
                field = fields[2].split("|")
                for j in field:
                    if j == i:
                        count += 1

            else:
                if fields == i:
                    count += 1

        result[i] = count

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

    for row in rows:
        print(row)

a, b = input().split()
countGenre(a, b)
