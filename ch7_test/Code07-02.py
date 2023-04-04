import xlrd

# workbook = xlrd.open_workbook('Excel/singer.xls')
# workbook = xlrd.open_workbook('Excel/singerCSV.xls')
# workbook = xlrd.open_workbook('Excel/outSinger1.xls')
# workbook = xlrd.open_workbook('Excel/outSinger2.xls')
# workbook = xlrd.open_workbook('Excel/outSinger3.xls')
workbook = xlrd.open_workbook('Excel/singerA_Test.xls')
sheetCount = workbook.nsheets

wsheetList = workbook.sheets()
for worksheet in wsheetList :
    print('** 워크시트의 이름 : %s' % (worksheet.name) )
    for row in range(worksheet.nrows) :
        for col in range(worksheet.ncols) :
            print("%s" % worksheet.cell_value(row, col), end = '\t')
        print()
    print()