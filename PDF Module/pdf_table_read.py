##from tabula import *
##
##convert_into("010_n.pdf", "test_n.csv", output = "csv")
###tabula.convert_into("table.pdf", "output.csv", output_format="csv")
###print df
##

from tabula import *
import pyPdf,os, time
import pandas as pd

filename = "008.pdf"
pdf = pyPdf.PdfFileReader(open(filename, "rb"))
pag_no = pdf.getNumPages()

#-------------------------------- Page Segmentation ---------------------------------#
for i in range(0,pag_no):
    pg = pdf.getPage(i)
    
    writer = pyPdf.PdfFileWriter()

    writer.addPage(pg)
    NewPDFfilename = "allTables"+str(i)+".pdf"
    with open(NewPDFfilename, "wb") as outputStream: 
        writer.write(outputStream)

time.sleep(0.2)


for i in range(0,pag_no):
    convert_into('allTables'+str(i)+'.pdf', 'test_'+str(i)+'.csv', output_format = 'CSV')

for i in range(0,pag_no):
    try:
        df = pd.read_csv("test_"+str(i)+".csv")
        if(df.empty):
            print "yes"
        else:
            print "Table found in -----> PAGE"+str(i+1)+" and stored in -----> test_"+str(i)+".csv"
    except:
        os.remove(r'C:\Users\Anudeep\Desktop\table_proj\allTables'+str(i)+'.pdf')
        os.remove(r'C:\Users\Anudeep\Desktop\table_proj\test_'+str(i)+'.csv')
        pass











##------Programme for extracting the data and writing it into another pdf----#
##pg3 = pdf.getPage(2)
##
##writer = pyPdf.PdfFileWriter()
##
##writer.addPage(pg6)
##
##NewPDFfilename = "allTables.pdf"
##with open(NewPDFfilename, "wb") as outputStream: 
##    writer.write(outputStream) 


