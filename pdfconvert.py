# -*- mode: python -*-
# -*- encoding: utf-8 -*-


from fpdf import FPDF
from docx2pdf import convert
import sys
import pandas as pd
import pdfkit

def get_options():
    return {
        'encoding': 'UTF-8',
        'enable-local-file-access': True
    }
def convertXlsPDF(file):
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    df = pd.read_excel(file)
    df.to_html( file.replace(".xlsx","") + ".html")
    pdfkit.from_file(file.replace(".xlsx","") + ".html" ,  file.replace(".html","") + ".pdf", configuration=config, options=get_options(), verbose=True)

def convertDoctoPDF(file):
    convert(file)

def main(nameFile):
    pdf = FPDF()  
    pdf.add_page()
    pdf.set_font("Arial", size = 10)
    f = open(nameFile, "r", encoding="utf-8")
    for x in f:
        pdf.cell(0, 5, txt = x, ln = 1)
  
    pdf.output(nameFile.replace(".txt","") + ".pdf")               

if __name__ == "__main__":
    for param in sys.argv: 
            if param.endswith('.docx'):
                convertDoctoPDF(param)
            elif param.endswith(".xlsx"):
                 #convertXlsPDF(param)
                 pass    
            elif param.endswith(".exe"):
                 continue    
            else:
                main(param)
        
    