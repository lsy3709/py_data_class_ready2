import xlwt
import csv
import os

csvFileList1 = ["CSV/singerA.csv"]
csvFileList2 = ["CSV/singerB.csv"]

xlsFileName1= "Excel/singerA_Test.xls"
xlsFileName2 = "Excel/singerB_Test.xls"

def csvToxlsFunc(csvFileNameList,xlsFileName) :
    outWorkbook = xlwt.Workbook()

    for csvFileName in csvFileNameList :
        rowCount = 0
        with open(csvFileName, "r") as inFp:
            csvReader = csv.reader(inFp)
            header_list = next(csvReader)
            outSheet = outWorkbook.add_sheet(os.path.basename(csvFileName))
            for col in range(len(header_list)) :
                outSheet.write(rowCount, col, header_list[col])
            for row_list in csvReader:
                rowCount += 1
                for col in range(len(row_list)):
                    if row_list[col].isnumeric() :
                        outSheet.write(rowCount, col, float(row_list[col]))
                    else :
                        outSheet.write(rowCount, col, row_list[col])

    outWorkbook.save(xlsFileName)
    print("Save. OK~")    

if __name__ == "__main__" :
   csvToxlsFunc(csvFileList1,xlsFileName1)


