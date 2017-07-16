#coding=utf-8
import os
import xlrd
import xlwt
import xlutils.*
location = os.path.dirname(__file__)
filename = os.path.join(location, 'test.xls')
wbk = xlrd.open_workbook(filename)
sheet_names = wbk.sheet_names()
#for sheet_name in sheet_names:
sheet1 = wbk.sheet_by_index(0)
print(sheet1.row_values(1))

# new excel
wbk2 = xlwt.Workbook()
sheet_1 = wbk2.add_sheet("sheet_1", cell_overwrite_ok=True)
sheet_2 = wbk2.add_sheet("sheet_2", cell_overwrite_ok=True)
sheet_1.write(0, 0,'this should overwrite1')
sheet_1.write(0, 1, 'qqqqqqq')
sheet_2.write(0, 0, 'this should overwrite2')
sheet_2.write(1, 2, 'bbbbb')
wbk2.save('tests.xls')
print('new excel has finished!')

wbk3 = 


