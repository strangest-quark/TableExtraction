# TableExtraction
A solution to extract tabular data from PDF and Image Files
## Extracting tables from PDF

Put instructions to run tabula code here

## Extracting table data from Images

### Step 1: Generate Searchable PDF from image using OCR

Using tesseract for OCR on input image to produce a sandwich pdf with existing image and extracted OCR data

*Follow the commands below to cd into data directory and convert image to searchable pdf.*

```
    cd TableExtraction/Image/data
    tesseract 29.jpg 29 -l eng pdf
```
 **Sample Searchable PDF**
 ![image](https://drive.google.com/uc?export=view&id=1e2PiOngGV4LMGGufCvqQS-ISXb7tWrOv)
 
 ### Step 2: Generate XML from Searchable PDF
```
    pdftohtml -c -hidden -xml 29.pdf 29.xml
```
*Find sample XML in Image/data folder*

 ### Step 3: Cluster lines in Image and generate CSV
```
  python extract.py
```
**Sample Line Clustering**
![image](https://drive.google.com/uc?export=view&id=10lRnS1XB9G_E1yLxORPSK7h1MK9X8KGQ)

### OUTPUT
*Generated output images and CSV files in Image/generated_output folder*
