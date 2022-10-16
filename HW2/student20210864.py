#!/usr/bin/python3

from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

wb = load_workbook(filename = 'student.xlsx')
dest_filename = 'student.xlsx'
ws = wb.active
ws.title = "Sheet1"

dic = dict()
max_st = ws.max_row - 1
score = list()

for i in range(2, max_st + 2):
    midterm = ws.cell(row = i, column = 3).value
    final = ws.cell(row = i, column = 4).value
    hw = ws.cell(row = i, column = 5).value
    attendance = ws.cell(row = i, column = 6).value
    result = float(midterm*0.3 + final*0.35 + hw*0.34 + attendance*1)
    dic[i] = result
    score.append(result)
    ws.cell(row = i, column = 7, value = result)

result_dict = dict(sorted(dic.items(), reverse = True, key = lambda x:x[1]))

A_max = max_st * 0.3
B_max = max_st * 0.4
C_max = max_st * 0.3
st_cnt = 1

dict_keys = result_dict.keys()
dict_keys = list(dict_keys)
print(result_dict)
print(score[1:])
A_st = list()
B_st = list()
C_st = list()

for i in range(max_st - 1):
    if dict_keys[i] in score:
        i_same = score.count(dic[i].value)

        if i_same <= A_max:
            for k in range(st_cnt, st_cnt + i_same):
                A_st.append(dict_keys[k])
        elif A_max < i_same <= A_max + B_max:
            for k in range(st_cnt, st_cnt + i_same):
                B_st.append(dict_keys[i])
        else:
            for k in range(st_cnt, st_cnt + i_same):
                C_st.append(dict_keys[i])
        
    else:
        if st_cnt <= A_max:
            A_st.append(dict_keys[i]) 
        elif A_max < st_cnt <= A_max + B_max:
            B_st.append(dict_keys[i]) 
        else:
            C_st.append(dict_keys[i])
    st_cnt += 1
    
    for j in A_st:
        for a in range(int(len(A_st) * 0.5)):
            ws.cell(row = result_dict[j], column = 8, value = "A+")
        
        for a in range(int(len(A_st) * 0.5)):
            ws.cell(row = result_dict[j], column = 8, value = "A0")
    
    for j in B_st:
        for a in range(int(len(B_st) * 0.5)):
            ws.cell(row = result_dict[j], column = 8, value = "B+")
        
        for a in range(int(len(B_st) * 0.5)):
            ws.cell(row = result_dict[j], column = 8, value = "B0")

    
    for j in C_st:
        for a in range(int(len(C_st) * 0.5)):
            ws.cell(row = result_dict[j], column = 8, value = "C+")
        
        for a in range(int(len(C_st) * 0.5)):
            ws.cell(row = result_dict[j], column = 8, value = "C0")

wb.save(filename = dest_filename)
