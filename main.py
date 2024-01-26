import os
import PyPDF2

merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir('pdfs_mesclar')

for arquivo in lista_arquivos:
    if ".pdf" not in arquivo:
        continue
    merger.append(f'pdfs_mesclar/{arquivo}')

merger.write('pdfs_mesclar/arquivo_final.pdf')
