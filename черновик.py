import wget
import xlrd

url = 'https://stepik.org/media/attachments/lesson/245267/salaries.xlsx'
wget.download(url)

wb = xlrd.open_workbook('salaries.xlsx')
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])

dict_s = {}
dict_j = {}

for rownum in range(1, 8):
    dict_s[sh.row_values(rownum)[0]] = sh.row_values(rownum)[1:]

for colnum in range(1, 8):
    dict_j[sh.col_values(colnum)[0]] = sh.col_values(colnum)[1:]

for region, salaries in dict_s.items():
    dict_s[region] = sorted(salaries)[3]
    print(region, dict_s[region])

print(max(dict_s, key=dict_s.get))
