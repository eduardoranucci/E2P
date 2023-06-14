import openpyxl as xl
import os

if os.path.exists(r'.\base.txt'):
    os.remove(r'.\base.txt')

excel = xl.load_workbook(r'base.xlsx')
df = excel.active
espacos = ' ' * 100

for cell in df['A:A']:

    linha = cell.row
    if cell.row == 1:
        continue
    try:
        data = cell.value.strftime('%d%m%Y')
    except AttributeError:
        continue
        
    debito = (str(df[f'B{linha}'].value).replace('None', '') + espacos)[:10]
    credito = (str(df[f'C{linha}'].value).replace('None', '')  + espacos)[:10]
    valor = (str(df[f'D{linha}'].value).replace('None', '')  + espacos)[:8]
    historico = (str(df[f'E{linha}'].value).replace('None', '')  + espacos)[:40]
    item_debito = (str(df[f'F{linha}'].value).replace('None', '')  + espacos)[:11]
    item_credito = (str(df[f'G{linha}'].value).replace('None', '')  + espacos)[:11]
    classe_debito = (str(df[f'H{linha}'].value).replace('None', '')  + espacos)[:10]
    classe_credito = (str(df[f'I{linha}'].value).replace('None', '')  + espacos)[:10]
    entidade_05_debito = (str(df[f'J{linha}'].value).replace('None', '')  + espacos)[:12]
    entidate_06_credito = (str(df[f'K{linha}'].value).replace('None', '')  + espacos)[:12]

    informacoes_pt1 = f"004|{debito}|{credito}|{valor}|{historico}|{data}|{item_debito}|{item_credito}|"
    informacoes_pt2 = f"{classe_debito}|{classe_credito}|{entidade_05_debito}|{entidate_06_credito}\n"
    linha_txt = informacoes_pt1 + informacoes_pt2
    
    with open('base.txt', mode='a', encoding='utf-8') as txt:
        txt.write(linha_txt)
        
