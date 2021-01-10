import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

curDir=os.getcwd()

def file_writer(text,page):
    with open(curDir+"/dirty_text/"+page+'.txt', 'w', newline='', encoding='utf-8-sig') as f:
        f.write(text)
        print('to__'+curDir+"/dirty_text/"+page+'.txt')

def imgRead(img_patch,page):
    image = Image.open(img_patch)
    text = pytesseract.image_to_string(image, lang='rus+deu+fra')
    file_writer(text,page)

def main():
	files = os.listdir(curDir+"/img_source/")	
	print(curDir)	
	print(files)
	for file in files:
            this_file=(curDir+"/img_source/"+file)
            print('===============================')
            print('from__'+this_file)
            imgRead(this_file,file[0:-4])

        
if __name__ == "__main__":
    main()
