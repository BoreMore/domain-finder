import os
import re
# writes words to temporary file
tmp = open('tmp.txt', 'a')
with open('wordlist.txt', 'r') as file:
    for line in file:
        tmp.write(line)
tmp.close()

# removes spaces and duplicate words from word list
lines_seen = set()
outfile = open('wordlist.txt', "w")
for line in open('tmp.txt', "r"):
    if line.replace(" ", "").lower() not in lines_seen:
        outfile.write(line.replace(" ", "").lower())
        lines_seen.add(line.replace(" ", "").lower())
outfile.close()
os.remove('tmp.txt')