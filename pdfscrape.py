import os
from bs4 import BeautifulSoup

i = 0
# reads pdf file paths
with open('filepaths.txt', 'r') as file:
    for line in file:
        i += 1
        # uses pdf2txt tool from PDFMiner to convert pdf to html
        command = 'python pdf2txt.py -o "outputs/pdf' + str(i) + '.html" -t html "' + line + '"'
        print(command)
        os.system(command)