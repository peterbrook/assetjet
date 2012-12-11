import os

rootDir = os.getcwd()
print ("Current path is: ", rootDir)

fileList = []
for root, subFolders, files in os.walk(rootDir):
    for file in files:
        if file.endswith(".ui"):
            fileList.append(os.path.join(root,file))
print fileList
for uiFile in fileList:
    cmd = "pyuic4 -o {0} {1}".format(uiFile.replace("ui", 'py'), uiFile)
    #print cmd    
    os.system(cmd)


print "Done"