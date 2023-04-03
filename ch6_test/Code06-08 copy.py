import csv

with open("CSV/singerA.csv", "r") as inFpA :
    with open("CSV/singerB.csv", "r") as inFpB:
        with open("CSV/singerSum2.csv", "w", newline='') as outFp:
            csvReaderA = csv.reader(inFpA)
            csvReaderB = csv.reader(inFpB)
            csvWriter = csv.writer(outFp)
            header_list = next(csvReaderA)
            header_list = next(csvReaderB)
            csvWriter.writerow(header_list)

            for row_list in csvReaderA:
                if int(row_list[-2] )>= 165 :
                     row_list[-2] = row_list[-2] + 'cm'
                     csvWriter.writerow(row_list)
            for row_list in csvReaderB:
                  if int(row_list[-2] )>= 165 :
                     row_list[-2] = row_list[-2] + 'cm'
                     csvWriter.writerow(row_list)

print('Save. OK~')