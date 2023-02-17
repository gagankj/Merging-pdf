from PyPDF2 import PdfMerger
import os

pdfs = os.listdir("importos")

merger = PdfMerger() 
for pdf in pdfs:
    merger.append(pdf)
merger.write("result.pdf")
merger.close()