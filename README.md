# domain-finder
Uses Python to scrape PDFs for domain names, check availability using the GoDaddy Domain API, and get appraisal value using the GoDaddy Appraisal API.

## How to Run
These instructions will allow you to run the project on your machine.

### Requirements
* Requires Python 3.7

### Download
* Download the repository files

### Usage
1. List paths to pdfs in filepaths.txt
2. Run pdfscrape.py:
```
python pdfscrape.py
```
3. Modify the soup.py file to read the html file produced from the pdf (found in outputs folder by default) and specify the style of the elements to scrape from the html file.

Run 
```
python soup.py
```
This is not automated currently due to different styles in each html file, but it will be considered for a future update.

4. Check wordlist.txt and optimize words. 
Run 
```
python cleanupwords.py
```
5. Run 
```
python available.py input.txt output.txt
```
where input.txt is the word list file and output.txt is the file to output available domain names to. In the example, the input file is wordlist.txt and the output file is available.txt.

6. Run 
```
python appraise.py input.txt output.txt
```
where input.txt is the available domain names file and output.txt is the file to output the appraised domain names to. In the example, the input file is available.txt and the output file is appraisal.txt.

### Acknowledgements 
The code for pdf2txt.py is a tool of pdfminer.six. To install pdfminer.six, use 
```
pip install pdfminer.six
```

The pdf used as a sample is an encyclopedia titled The Handy Cyclopedia of Things Worth Knowing by Joseph Triemens. It can be acquired from https://www.gutenberg.org/ebooks/20190.
