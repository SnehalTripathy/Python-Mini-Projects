import PyPDF2

pdf_files = ['Certificate_143.pdf', 'Certificate.pdf']  # Replace with your file paths

merger = PyPDF2.PdfMerger()

for pdf in pdf_files:
    pdffile = open(pdf, 'rb')
    pdfreader = PyPDF2.PdfReader(pdffile) 
    merger.append(pdfreader)

# Writing out the merged PDF
output_filename = 'merged_output.pdf'
merger.write(output_filename)
merger.close()

# print(f"PDFs merged successfully into '{output_filename}'")
