import os
import sys
PATH = "c:\cms"
def Test1(rootDir): 
	file = open("c:\\test.txt","w")
	list_dirs = os.walk(rootDir) 
	for root, dirs, files in list_dirs: 
		#for d in dirs: 
			#print os.path.join(root, d) 
			#file.write(os.path.join(root,d)+"\n")
		for f in files: 
			file.write( os.path.join(root, f) + "\n")
Test1(PATH)