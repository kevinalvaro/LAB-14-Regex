#by kevin alvaro adianto

import re
file=open("mbox-short.txt","r")
#file=open("test.txt","r")
teks=""
for line in file:
    teks+=line
print(teks)
hasil=re.findall("Author: [\w.-]+@[\w.-]+","teks")
print(hasil)

