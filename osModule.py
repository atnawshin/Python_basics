#file management
import os
#print(os.getcwd()) #givs us pythons current directory(dir)
#os.mkdir("New_Folder")
#os.rename("New_Folder","RenamedFolder") #if the file is in another location then the wholw location have to be specified in the first palce along with file name
#os.rmdir("RenamedFolder") #for deleting a dir
#print(dir(os)) #to see all the methods
#print(os.path.isfile("osModule.py"))

#to check a files existence
'''
fileloc = 'osModule.py'

if os.path.isfile(fileloc):
    print("File",fileloc,"exists.")
else:
    print("File",fileloc,"don\'t exist.")
'''

#to check a dir's existence
#print(os.path.isdir('Folder'))

# we can import the modules and rename them
import os as operatoringS

print(operatoringS.getcwd())


