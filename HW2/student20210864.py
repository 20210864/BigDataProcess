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
    result = float(midterm*0.3 + final*0.35 + hw*0.34 + attendance*1)
    dic[i] = result
    ws.cell(row = i, column = 7, value = result)

result_dict = dict(sorted(dic.items(), reverse = True, key = lambda x:x[1]))
A_max = (max_st - 1) * 0.3
B_max = (max_st - 1) * 0.4
C_max = (max_st - 1) * 0.3
st_cnt = 1
dict_keys = list(result_dict.keys())
score = list(result_dict.values())
A_st = list()
B_st = list()
C_st = list()
same_dic = dict()
same_keys = list()
i_same = 0
i = 0
same_dic['A'] = 0
same_dic['B'] = 0
same_dic['C'] = 0
while(st_cnt < max_st - 1):
    if result_dict[dict_keys[i]] in score[i+1:]:
        i_same = score.count(result_dict[dict_keys[i]])
        if st_cnt - 1 + i_same <= A_max:
            for k in range(st_cnt, st_cnt + i_same):
                A_st.append(dict_keys[k - 1])
                same_keys.append(dict_keys[k - 1])
            same_dic['A'] = same_keys
            same_dic[score[i]] = i_same
            st_cnt += 1
        elif st_cnt - 1 + i_same <= max_st * 0.7:
            for k in range(st_cnt, st_cnt + i_same):
                B_st.append(dict_keys[k - 1])
                same_keys.append(dict_keys[k - 1])
            same_dic['B'] = same_keys
            same_dic[score[i]] = i_same
        else:
            for k in range(st_cnt, st_cnt + i_same):
                C_st.append(dict_keys[k - 1])
                same_keys.append(dict_keys[k - 1])
            same_dic['C'] = same_keys
            same_dic[score[i]] = i_same
        same_keys.clear()

    else:
        if st_cnt <= A_max:
            A_st.append(dict_keys[i])
        elif st_cnt <= A_max + B_max:
            B_st.append(dict_keys[i])
        else:
            C_st.append(dict_keys[i])
    i = st_cnt
    st_cnt += 1

st_cnt = 1
i = 0
a_list = same_dic['A']
b_list = same_dic['B']
c_list = same_dic['C']
while(st_cnt <= len(A_st)):
    if str(A_st[i]) in str(a_list):
        s_cnt = same_dic[A_st[i]]
        if s_cnt + st_cnt <= len(A_st) * 0.5:
            for a in range(s_cnt):
                ws.cell(row = A_st[i], column = 8, value = "A+")
        else:
            for a in range(s_cnt):
                ws.cell(row = A_st[i], column = 8, value = "A0")
        st_cnt += s_cnt
    else:
        if st_cnt <= len(A_st) * 0.5:
            ws.cell(row = A_st[i], column = 8, value = "A+")
        else:
            ws.cell(row = A_st[i], column = 8, value = "A0")
    i = st_cnt
    st_cnt += 1
st_cnt = 1
i = 0
while(st_cnt <= len(B_st)):
    if str(B_st[i]) in str(b_list):
        s_cnt = same_dic[B_st[i]].value
        if s_cnt + st_cnt <= len(B_st) * 0.5:
            for a in range(s_cnt):
                ws.cell(row = B_st[i], column = 8, value = "B+")
        else:
            for a in range(s_cnt):
                ws.cell(row = B_st[i], column = 8, value = "B0")
        st_cnt += s_cnt
    else:
        if st_cnt <= len(B_st) * 0.5:
            ws.cell(row = B_st[i], column = 8, value = "B+")
        else:
            ws.cell(row = B_st[i], column = 8, value = "B0")
    i = st_cnt
    st_cnt += 1
st_cnt = 1
i = 0
while(st_cnt <= len(C_st)):
    if str(C_st[i]) in str(c_list):
        s_cnt = same_dic[C_st[i]].value
        if s_cnt + st_cnt <= len(C_st) * 0.5:
            for a in range(s_cnt):
                ws.cell(row = C_st[i], column = 8, value = "C+")
        else:
            for a in range(s_cnt):
                ws.cell(row = C_st[i], column = 8, value = "C0")
        st_cnt += s_cnt
    else:
        if st_cnt <= len(C_st) * 0.5:
            ws.cell(row = C_st[i], column = 8, value = "C+")
        else:
            ws.cell(row = C_st[i], column = 8, value = "C0")
    i = st_cnt
    st_cnt += 1

wb.save(filename = dest_filename)
