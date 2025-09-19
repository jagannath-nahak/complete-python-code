from pypdf import PdfWriter
import os

merger = PdfWriter()
files=sorted([file for file in os.listdir() if file.lower().endswith(".pdf")])

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()