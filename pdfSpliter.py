import os
from PyPDF2 import PdfFileReader, PdfFileWriter



def getThisPage():
	arr=[] #сюда надо добавить страницы для обработки
	
	curDir=os.getcwd()
	book_patch = curDir+"/book/" 
	pdf_document = os.listdir(book_patch)
	pdf = PdfFileReader(open(book_patch+pdf_document[0],'rb'))
	pageCount=pdf.getNumPages()
	print(pdf_document,'page - ',pageCount)
	
	if len(arr)>0:
		for page in arr:  
			pdf_writer = PdfFileWriter()
			current_page = pdf.getPage(page)
			pdf_writer.addPage(current_page)
			outputFilename = curDir+"/pdf_source/{}.pdf".format(page)
			with open(outputFilename, "wb") as out:
				pdf_writer.write(out)
				print("created", outputFilename)
				

	else:
		for page in range(pageCount):  
			pdf_writer = PdfFileWriter()
			current_page = pdf.getPage(page)
			pdf_writer.addPage(current_page)
			outputFilename = curDir+"/pdf_source/{}.pdf".format(page + 1)
			with open(outputFilename, "wb") as out:
				pdf_writer.write(out)
				print(page + 1,'/',pageCount,"created", outputFilename)





if __name__ == "__main__":
    getThisPage()