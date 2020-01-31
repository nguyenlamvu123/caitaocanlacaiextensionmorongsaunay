from xlrd import open_workbook
book = open_workbook('Book.xlsx')
##class linhnhixinhdep :
for sheet in book.sheets():
        for rowidx in range(sheet.nrows):
            row = sheet.row(rowidx)
            for colidx, cell in enumerate(row):
                if cell.value == 'school':
                    q,qq,qqq= sheet.name, colidx, rowidx

