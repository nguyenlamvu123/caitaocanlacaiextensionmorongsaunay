from django.shortcuts import render
import openpyxl
from xlrd import open_workbook

def index(request):
    if "GET" == request.method:
        return render(request, 'django_import_export/index.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]
        print(worksheet)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
        return render(request, 'django_import_export/index.html', {"excel_data":excel_data})

def linhnhixinhdep(request):
    book = open_workbook('Book.xlsx')
    for sheet in book.sheets():
        for rowidx in range(sheet.nrows):
            row = sheet.row(rowidx)
            for colidx, cell in enumerate(row):
                if cell.value == 'school':
                    q,qq,qqq= sheet.name, colidx, rowidx
