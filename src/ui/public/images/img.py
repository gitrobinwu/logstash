#-*- coding: utf-8 -*-
from PIL import Image 

def image_info(filepath):
	im = Image.open(filepath)
	print '-'*60
	print im
	print  im.size
	print im.format 
	print im.mode
	print '-'*60
image_info('./elk.ico')
image_info('./rd_logo.png')


import os
f,e = os.path.splitext('./rd_logo')
outfile = "{0}.ico".format(f)
print outfile
im = Image.open('./rd_logo.png')
im.thumbnail((16,16))
im.save(outfile,'ICO')

image_info('./rd_logo.ico')

outfile1 = "{0}_new.png".format(f)
print outfile1
im1 = Image.open('./rd_logo.png')
#im1.thumbnail((252,45))

#im1.save(outfile1,"PNG")
im1.resize((150, 65), Image.ANTIALIAS).save(outfile1)
image_info('./rd_logo_new.png')
os.system('rm -rf ./kibana.svg')
os.system('cp ./rd_logo_new.png kibana.svg')
