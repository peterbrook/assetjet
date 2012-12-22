import os

rootDir = os.getcwd()
print ("Current path is: ", rootDir)
outDir = os.path.join(rootDir, "src\\view")

fileList = []
for root, subFolders, files in os.walk(rootDir):
    for file in files:
        if file.endswith(".ui"):
            outFile = os.path.join(outDir, file.replace("ui", 'py'))
            fileList.append((os.path.join(root,file), outFile))

for uiFile, outFile in fileList:
    print "Building: {0} to: {1}".format(uiFile, outFile)
    cmd = "pyuic4 -o {0} {1}".format(outFile, uiFile)    
    os.system(cmd)

print "Done"