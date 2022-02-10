
from fpdf import FPDF

pdf= FPDF()

pdf.add_page()

pdf.set_font('arial')

arquivo = input('Digite o nome do arquivo com extensão')
nome = input('Digite o novo nome do arquivo')
with open(f'{arquivo}','r') as a:
    for i in a:
        t = f'{i}'
        pdf.multi_cell(200,10, txt=f'{t}', border=0, fill=0,split_only=False)
        
pdf.output(f'{nome}.pdf')       