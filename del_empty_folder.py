# Deletes all empty folders in target_dir.
import os
 
__author__ = "helly"
target_dir = "C:\\Users\\hachen\\Desktop\\1"
toDelete = []

for root,dirs,files in os.walk(target_dir):   
	#print root
	#print dirs
	#print files
	if ((not dirs) and (not files)):
		toDelete.append(root)

# Optimization needed. We can ilimenate empty folders in subfolder first,
# so that we needn't to check whecher the dir exists.
for dir in toDelete:
	if os.path.exists(dir):
		print dir
		os.removedirs(dir)
