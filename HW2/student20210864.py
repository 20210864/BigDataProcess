#!/usr/bin/python3

from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

wb = load_workbook(filename = 'student.xlsx')
dest_filename = 'student.xlsx'
ws = wb.active
ws.title = "Sheet1"

dic = dict()
max_st = ws.max_row

for i in range(2, max_st + 1):
    midterm = ws.cell(row = i, column = 3).value
    final = ws.cell(row = i, column = 4).value
    hw = ws.cell(row = i, column = 5).value
    attendance = ws.cell(row = i, column = 6).value
    result = float(midterm*0.3 + final*0.35 + hw*0.34 + attendance*0.01)
    dic[i] = result
    ws.cell(row = i, column = 7, value = result)

result_dict = dict(sorted(dic.items(), reverse = True, key = lambda x:x[1]))

print(result_dict)
dict_keys = result_dict.keys()
dict_keys = list(dict_keys)
print(dict_keys)

st_count = 1
same_cnt = 0
same_isit = 0
same1 = 0
same2 = max_st + 1

for i in range(max_st - 1):
    if i <= max_st - 3:
        a1 = dict_keys[i]
        a2 = dict_keys[i+1]
        while True:
            if result_dict[a1] == result_dict[a2]: 
                same2 = i + 1
                same_cnt += 1
                if same_cnt == 1:
                    same1 = i + 1
            else:
                break
        for j in range(same1, same2+1):
            if j == 15 or j == 30 or j == 50 or j == 70 or j == 85:
                same_isit = 1
                st_count = same2

    elif i == max_st - 2:
       pass 

    else:
        break

    if st_count <= max_st * 0.15:
        if same_isit == 1:
            for k in range(same1, same2):
                ws.cell(row = dict_keys[k - 1], column = 8, value = "A+")
        ws.cell(row = dict_keys[i], column = 8, value = "A+")

    elif max_st * 0.15 < st_count <= max_st * 0.3:
        if same_isit == 1:
            for k in range(same1, same2):
                ws.cell(row = dict_keys[k - 1], column = 8, value = "A0")
        ws.cell(row = dict_keys[i], column = 8, value = "A0")

    elif max_st * 0.3 < st_count <= max_st * 0.5:
        if same_isit == 1:
            for k in range(same1, same2):
                ws.cell(row = dict_keys[k - 1], column = 8, value = "B+")
        ws.cell(row = dict_keys[i], column = 8, value = "B+")

    elif max_st * 0.5 < st_count <= max_st * 0.7:
        if same_isit == 1:
            for k in range(same1, same2):
                ws.cell(row = dict_keys[k - 1], column = 8, value = "B0")
        ws.cell(row = dict_keys[i], column = 8, value = "B0")

    elif max_st * 0.7 < st_count <= max_st * 0.85:
        if same_isit == 1:
            for k in range(same1, same2):
                ws.cell(row = dict_keys[k - 1], column = 8, value = "C+")
        ws.cell(row = dict_keys[i], column = 8, value = "C+")

    else:
        if same_isit == 1:
            for k in range(same1, same2):
                ws.cell(row = dict_keys[k - 1], column = 8, value = "C0")
        ws.cell(row = dict_keys[i], column = 8, value = "C0")
    st_count += 1

wb.save(filename = dest_filename)
