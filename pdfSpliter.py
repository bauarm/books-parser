import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def log_writer(book,text):
		with open(curDir+"/log/"+'LOG_'+book+'.txt', 'a', newline='', encoding='utf-8-sig') as f:
			f.write(text)

curDir=os.getcwd()
book_patch = curDir+"/book/" 
pdf_document = os.listdir(book_patch)
pdf = PdfFileReader(open(book_patch+pdf_document[0],'rb'))
pageCount=pdf.getNumPages()
print(pdf_document,'page - ',pageCount)
log_writer(str(pdf_document[0])[0:-4],str(pdf_document[0])[0:-4]+'\n')
log_writer(str(pdf_document[0])[0:-4],'Page in this book - '+str(pageCount)+'\n')

def readyPage():
	if(len(pdf_document)>0):
		for page in range(pageCount):
			getThisPage(page)

def getThisPage(num):
	pdf_writer = PdfFileWriter()
	current_page = pdf.getPage(num)
	pdf_writer.addPage(current_page)
	outputFilename = curDir+"/pdf_source/{}.pdf".format(num + 1)
	with open(outputFilename, "wb") as out:
		pdf_writer.write(out)
		print(num + 1,'/',pageCount,"created", outputFilename)
		log_writer(str(pdf_document[0])[0:-4],str(num + 1)+'/'+str(pageCount)+" created "+outputFilename+'\n')
		
if __name__ == "__main__":
	readyPage()