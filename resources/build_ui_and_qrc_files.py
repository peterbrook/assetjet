import os
from subprocess import call

# UIs

rootDir = '..'
targetDir = r'app/src/assetjet/view'

outDir = os.path.join(rootDir, targetDir)
fileList = []

for root, subFolders, files in os.walk(rootDir):
    for file_ in files:
        if file_.endswith(".ui"):
            outFile = os.path.join(outDir, file_.replace(".ui", '.py'))
            fileList.append((os.path.join(root,file_), outFile))

for uiFile, outFile in fileList:
    print "Building: {0} to: {1}".format(uiFile, outFile)
    cmd = "pyside-uic -o {0} {1}".format(outFile, uiFile)
    call(cmd)

print "UI files done"

# Resources

fileList = []

for root, subFolders, files in os.walk(rootDir):
    for file_ in files:
        if file_.endswith(".qrc"):
            outFile = os.path.join(outDir, file_.replace(".qrc", '_rc.py'))
            fileList.append((os.path.join(root,file_), outFile))

for rcFile, outFile in fileList:
    print "Building: {0} to: {1}".format(rcFile, outFile)
    cmd = "pyside-rcc -o {0} {1}".format(outFile, rcFile)
    call(cmd)

print "Rersource files done"