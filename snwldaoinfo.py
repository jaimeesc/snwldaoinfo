import os
import shutil

# Run the program from the same directory where the .wri files are stored.
# Either copy the script to the directory where the .wri files are
#  or run the program from that directory via command line.

file_dir = os.path.normpath(os.getcwd()) + '\\'
file_dir_no_slash = os.path.normpath(os.getcwd())


def processFile(fileName):
	openFileListObject = []
	print("----", fileName, "----")
	with open(fileName, 'r') as openFile:
		for line in openFile:
			openFileListObject.append(line)
	for i in openFileListObject:
		index = openFileListObject.index(i)
		if i.startswith("-------") and i.endswith("-------\n"):
			if "RETRY COUNT: " in openFileListObject[index+5]:
				objName = str(i).lstrip("-------")
				objName = objName.rstrip("-------\n")
				objFQDN = str(openFileListObject[index+4]).rstrip("\n")
				objRetry = str(openFileListObject[index+5]).rstrip("\n")
				objManTTL = str(openFileListObject[index+6]).rstrip("\n")
				objHosts1 = str(openFileListObject[index+7]).rstrip("\n") # HOSTS
				objHosts2 = str(openFileListObject[index+8]).rstrip("\n") # CREATED
				objHosts3 = str(openFileListObject[index+9]).rstrip("\n") # REFERENCES
				print(objName + "," + objFQDN + "," + objHosts1) # Prints on one line per object, comma-separated.
# The following print statements print line-by-line.
#				print(index, str(i).replace("  ", ""), end='')
#				print(index+1, openFileListObject[index+1], end='') # UUID
#				print(index+2, openFileListObject[index+2], end='') # Class
#				print(index+4, openFileListObject[index+4], end='') # FQDN
#				print(index+5, openFileListObject[index+5], end='') # RETRY COUNT
#				print(index+6, openFileListObject[index+6], end='') # Manually set TTL
#				print(index+7, openFileListObject[index+7], end='') # HOSTS
#				print(index+8, openFileListObject[index+8], end='') # HOSTS 2 if TTL is manually set, or Time Created if not
#				print(index+9, openFileListObject[index+9], end='') # References or Time Created, depends if Manual TTL set.
#				print(index+10, openFileListObject[index+10], end='')
	openFileListObject.clear()


# For each file in the directory, create the folder + file path. If there are .WRI files, process them.
for file in os.listdir(file_dir):
	fileName = file_dir + file
	if '.wri' in fileName:
		processFile(fileName)
