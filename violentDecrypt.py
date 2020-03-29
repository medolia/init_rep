#! python3 violentDecrypt.py uses words in dictionary to violently decrypt pdf file.

import PyPDF2
import os

os.chdir(r'C:\Users\Medolia\Documents\python_prc\automate_online-materials')
pdfObj = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))

pwDic = open('dictionary.txt', 'r')

for each_word in pwDic:
    if pdfObj.decrypt(each_word):
        print("Password found: %s" % (each_word))
        break
    elif pdfObj.decrypt(each_word.lower()):
        print("Password found: %s" % (each_word.lower()))
        break
    else:
        print("Wrong password: %s" % (each_word))
