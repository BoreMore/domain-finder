import os
from bs4 import BeautifulSoup

wordlist = open('wordlist.txt', 'a')

# pdf to read
with open('outputs/pdf1.html', 'rb') as html:
    # scrapes using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    # finds words with specific styles in html
    for tag in soup.findAll('span', attrs={"style": "font-family: b'TimesNewRomanPS-BoldMT'; font-size:9px"}): 
        try:
            # writes words to file
            wordlist.write(tag.text)
        except:
            pass

wordlist.close()