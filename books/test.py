import os
import enchant

from PyPDF2 import pdf
from PyPDF2.pdf import PdfFileReader, PdfFileWriter, ContentStream, TextStringObject, b_, u_, re


def getDataUsingPyPdf2(filename):
    pdf = PdfFileReader(open(filename, "rb"))
    content = ""
    num = pdf.getNumPages()
    for i in range(0, num):
        extractedText = pdf.getPage(i).extractText()
        content += extractedText + "\n"
        return content


def dopage(page):
    content = page["/Contents"].getObject()
    if not isinstance(content, ContentStream):
        content = ContentStream(content, pdf)
    results = ""

    for a, b in content.operations:
        results += str(a)
    return results


def extract_words(input):
    results = ""
    for x in input:
        if x.isalpha() or x == ',' or x == '\'' or x == '\"' or x == '-':
            results += x
    results = results.replace(',u\'', '')

    tmp, results = results, ""
    for x in tmp:
        if x.isalpha() or x == '-':
            results += x
    #
    results = results.split('-')
    results = list(set(results))

    edict = enchant.Dict("en_US")
    for word in results:
        if len(word) > 1 and edict.check(word):
            words.append(word)


def getData(filename):
    pdf = PdfFileReader(open(filename, "rb"))
    content = ""
    num = pdf.getNumPages()
    for i in range(0, num):
        extractedText = dopage(pdf.getPage(i))
        content += extractedText + "\n"
    return content


files = os.listdir('.')

content = ''
for filename in files:
    items = filename.split('.')
    if items[-1] == 'pdf':
        content += getData(filename)

words = []
extract_words(content)
print(len(words), words)

