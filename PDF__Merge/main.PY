from PyPDF2 import PdfWriter

merger = PdfWriter()
pdfs =[]
n = int(input("how many yoiu wannna merge?\n"))
for i in range(n):
    name =input(f"enter the name of {i+1} pdf : ")

    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf1.pdf")
merger.close()    