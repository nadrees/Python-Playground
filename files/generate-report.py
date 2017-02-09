import zipfile, os, shutil, csv, xlsxwriter

file = './cm08FEB2017bhav.csv.zip'

dataDir = './data'

os.mkdir(dataDir)

filesExtracted = []

with open(file, 'rb') as fh, zipfile.ZipFile(fh) as zipFileHandler:
    for filename in zipFileHandler.namelist():
        zipFileHandler.extract(filename, dataDir)
        filesExtracted.append(dataDir + '/' + filename)

allRows = []

for filename in filesExtracted:
    with open(filename, 'r', newline='') as fh:
        lineReader = csv.reader(fh)
        next(lineReader, None)
        for row in lineReader:
            symbol = row[0]
            close = row[5]
            prevClose = row[7]
            tradedQty = float(row[9])
            pctChange = float(close)/float(prevClose) - 1
            allRows.append([symbol, pctChange, tradedQty])

shutil.rmtree(dataDir)

allRows = sorted(allRows, key=lambda x: x[2], reverse=True)

outputExcelFile = 'out.xlsx'

with xlsxwriter.Workbook(filename=outputExcelFile) as workbook:
    worksheet = workbook.add_worksheet(name='Summary')

    worksheet.write_row('A1', ['Top Traded Stocks'])
    worksheet.write_row('A2', ['Stock', '% Change', 'Value Traded (INR)'])

    for rowNum in range(5):
        row = allRows[rowNum]
        worksheet.write_row('A' + str(rowNum + 3), row)
