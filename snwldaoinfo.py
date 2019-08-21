import os
import shutil

# Run the program from the same directory where the .wri files are stored.
# Either copy the script to the directory where the .wri files are
#   or run the program from that directory via command line.

file_dir = os.path.normpath(os.getcwd()) + '\\'
file_dir_no_slash = os.path.normpath(os.getcwd())

# Filters out 
filter_list = ['Created','Updated']

# List of object names. Becomes populated as objects are parsed
# Used to identify the first item in the second set of object info in TSR.
object_names = []

# Parse through the file and do some stuff
def processFile(fileName):
	openFileListObject = []
	print("----", fileName, "----")
	print("Object Name,FQDN,Manually Set TTL,Resolved Hosts,Resolved Hosts,Resolved Hosts,Resolved Hosts,Resolved Hosts,Resolved Hosts,Resolved Hosts,Resolved Hosts,Resolved Hosts,Resolved Hosts,Resolved Hosts,Resolved Hosts,Resolved Hosts,Resolved Hosts,Resolved Hosts,Resolved Hosts,Resolved Hosts,Resolved Hosts")
	with open(fileName, 'r') as openFile:
		for line in openFile:
			openFileListObject.append(line)
	for i in openFileListObject:
		index = openFileListObject.index(i)
		if i.startswith("-------") and i.endswith("-------\n"):
			if "Class: Custom" in openFileListObject[index+2]:
	#			if "RETRY COUNT: " in openFileListObject[index+5]:
				if "Manually Set TTL:" in openFileListObject[index+6]:
					objName = str(i).lstrip("-------") # Name with ----- stripped off left side
					objName = objName.rstrip("-------\n") # Name with ----- stripped off right side
					objFQDN = str(openFileListObject[index+4]).rstrip("\n") # Configured FQDN
					objRetry = str(openFileListObject[index+5]).rstrip("\n") # Object Retries
					objManTTL = str(openFileListObject[index+6]).rstrip("\n") # Manually Set TTL:
					objHosts1 = str(openFileListObject[index+7]).rstrip("\n") # HOSTS
					objHosts2 = str(openFileListObject[index+8]).rstrip("\n") # CREATED
					objHosts3 = str(openFileListObject[index+9]).rstrip("\n") # REFERENCES
					for t in input_list: # Filters out Created and Updated timestamps
						if t in objHosts2:
							objHosts2 = ""
					for x in object_names: # Looks for duplicate object names
						if str(x) == objName:
#							print(x, "=", objName) # Prints first duplicate object name
							exit() # Exits when it hits the first duplicate object name
					print(objName + "," + objFQDN + "," + objManTTL + "," + objHosts1 + "," + objHosts2)
					object_names.append(objName)
#				print(index, str(i).replace("  ", ""), end='')
#				print(index+1, openFileListObject[index+1], end='') # UUID
#				print(index+2, openFileListObject[index+2], end='') # Class
#				print(index+4, openFileListObject[index+4], end='') # FQDN
#				print(index+5, openFileListObject[index+5], end='') # RETRY COUNT
#				print(index+6, openFileListObject[index+6], end='') # Manually set TTL
#				print(index+7, openFileListObject[index+7], end='') # HOSTS
#				print(index+8, openFileListObject[index+8], end='') # HOSTS 2 or Time Created
#				print(index+9, openFileListObject[index+9], end='')
#				print(index+10, openFileListObject[index+10], end='')
	openFileListObject.clear()
	object_names.clear()


# For each file in the directory, create the folder + file path. If there are .WRI files, process them.
for file in os.listdir(file_dir):
	fileName = file_dir + file
	if '.wri' in fileName:
		processFile(fileName)
