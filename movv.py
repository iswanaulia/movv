import sys, os, shutil, fnmatch

source = str(sys.argv[1])
dest = str(sys.argv[2])

files = os.listdir(source)

for f in files:
	if fnmatch.fnmatch(f, str(sys.argv[3])+'*'):
		print(f)
		# If the file exists on destination folder, delete it
		if os.path.isfile(dest+'\\'+f) :
			os.remove(dest+'\\'+f)
		#then move it
		shutil.move(os.path.join(source, f), dest)
	else :
		print ("no match file")

