from __future__ import print_function
from wand.image import Image
from wand.color import Color
import os


def main():
	curDir=os.getcwd()
	files = os.listdir(curDir+"/pdf_source")	
	files = sorted(files) 
	print(len(files))
	print(files)
	for file in files:
		this_file=(curDir+"/pdf_source"+"/"+file)
		with Image(filename=this_file, resolution=300) as img:
			img.background_color = Color("white")
			img.alpha_channel = False
			img.save(filename=curDir+"/img_source/"+file[0:-4]+'.png')
			print('=============================')
			print('from__'+this_file)
			print('to__'+file[0:-4]+'.png')
        
if __name__ == "__main__":
    main()
