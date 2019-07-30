#! python3
import os
totalSize = 0
for filename in os.listdir(r'C:\Users\patri\OneDrive\Desktop\MyPythonScripts'):
	if not os.path.isfile(os.path.join(r'C:\Users\patri\OneDrive\Desktop\MyPythonScripts', filename)):
	    continue
	totalSize = totalSize + os.path.getsize(os.path.join(r'C:\Users\patri\OneDrive\Desktop\MyPythonScripts', filename))
print(totalSize)
