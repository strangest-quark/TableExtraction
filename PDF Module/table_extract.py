"""
It includes the following stages:
1. Load the PDF file using pyPDF module.
2. Give a little preprocessing to reduce noise in the pages. 
3. Iterate through the pages and save all the individual pages.
4. Tabula-py recognises the tables and export it to a csv using pandas.
"""



from tabula import *
import pyPdf,os, time
import pandas as pd

filename = raw_input("Enter the pdf you want to extract the table --> ") + ".pdf"
pdf = pyPdf.PdfFileReader(open(filename, "rb"))
pag_no = pdf.getNumPages()

for i in range(0,pag_no):
    pg = pdf.getPage(i)
    
    writer = pyPdf.PdfFileWriter()

    writer.addPage(pg)
    NewPDFfilename = "Page_"+str(i)+".pdf"
    with open(NewPDFfilename, "wb") as outputStream: 
        writer.write(outputStream)

time.sleep(0.2)

for i in range(0,pag_no):
    convert_into('Page_'+str(i)+'.pdf', 'result_'+str(i)+'.csv', output_format = 'CSV')
    convert_into('Page_'+str(i)+'.pdf', 'result_'+str(i)+'.xml', output_format = 'xml')

for i in range(0,pag_no):
    try:
        df = pd.read_csv("result_"+str(i)+".csv")
        if(df.empty):
            print "yes"
        else:
            print "Table found in -----> PAGE"+str(i+1)+" and stored in -----> result_"+str(i)+".csv"
    except:
        os.remove('/home/Username/Desktop/TableExtraction/Page_'+str(i)+'.pdf')
        os.remove('/home/Username/Desktop/TableExtraction/result_'+str(i)+'.csv')
        os.remove('/home/Username/Desktop/TableExtraction/result_'+str(i)+'.xml')

        pass




