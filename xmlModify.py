import os
import xlrd
import xlutils.copy
location = os.path.dirname(__file__)
filename = os.path.join(location, 'test.xls')
rb = xlrd.open_workbook(filename)
wb = xlutils.copy.copy(rb)
ws = wb.get_sheet(0)
ws.write(1, 1, 'changed!')
ws.write(3, 4, "twice changed!")
ws.write(3, 6, "third changed!")
wb.save(filename)
