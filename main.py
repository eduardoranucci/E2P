import openpyxl as xl

planilha = xl.load_workbook(r'base.xlsx')
df = planilha.active

debito, credito, valor, hist, data = [], [], [], [], []

for column in df['A:E']:
    
    for cell in column:

        match cell.column:

            case 1:
                debito.append(cell.value)

            case 2:
                credito.append(cell.value)

            case 3:
                valor.append(cell.value)

            case 4:
                hist.append(cell.value)

            case 5:
                data.append(cell.value)

espaco = " " * 9
linha = []

i = 0
while i < len(debito): 

    deb = f'{debito[i]}{" " * 40}'
    cred = f'{credito[i]}{" " * 40}'
    val = f'{valor[i]}{" " * 40}'
    ht = f'{hist[i]}{" " * 40}'
    dt = f'{data[i]}{" " * 40}'

    linha.append(f'001{" " * 6}{deb[:11]}{espaco}{cred[:11]}{espaco}{val[:8]}   {espaco}{ht[:40]}{dt[:8]}\n')
    i = i + 1


with open('base.txt', mode='w+') as txt:

    for i in linha:
        txt.write(i)

exit()