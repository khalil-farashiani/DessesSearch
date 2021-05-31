import xlsxwriter
f = open('database.json', 'r')

for i in f:
    if 'H01191' in  i:
        i = i.strip("""\n\t""")
        i = i.strip()
        j = i.split(sep='"')
        x = j[3]
        y = x.split(' ')
        z = y[0]
        y.pop(0)
        y.pop(0)
        y = ' '.join(y)
        print(z)
        print(y)
        workbook = xlsxwriter.Workbook(f'{z}.xlsx')
        worksheet = workbook.add_worksheet()
        row = 0
        col = 0
        worksheet.write(row, col, 'name')
        worksheet.write(row, col+1, 'code')
        worksheet.write(row, col+2, 'more enformation')
        worksheet.write(row+1, col, y)
        worksheet.write(row+1, col+1, z)
        worksheet.write(row+1, col+2, 'https://www.kegg.jp/entry'+y)
        workbook.close()