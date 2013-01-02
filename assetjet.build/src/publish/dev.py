from ftplib import FTP
from subprocess import call
from deploy import package


FTPServer = "ariel.kreativmedia.ch"
Benutzername = "ftpass45631"
Passwort = "C6W58Y8b"
Verzeichnis = "httpdocs"

ftp = FTP(host=FTPServer)
loginResult = ftp.login(user=Benutzername, passwd=Passwort, acct=Verzeichnis)

if loginResult:
    print "Successfully logged into FTP server"

ftp.cwd(dirname=Verzeichnis)
ftp.dir()
try:
    ftp.rmd(dirname=package.GetDescriptorString())
    ftp.mkd(dirname=package.GetDescriptorString())
except:
    pass

ftp.cwd(dirname=package.GetDescriptorString())

# ftp.storbinary takes a FILE object not a path, python will automatically close the file
ftp.storbinary('STOR %s' % package.GetDescriptorString(), open('C:\\src\\GitHub\\assetjet\\assetjet.build\\src\\dist\\AssetJet-0.1.6.win-amd64.zip', "rb"))

print("Sent Transfer Command")
ftp.dir()

def publish():

    FTPServer = "ariel.kreativmedia.ch"
    Benutzername = "ftpass45631"
    Passwort = "C6W58Y8b"
    Verzeichnis = "httpdocs"
    ftp = FTP(host=FTPServer)
    loginResult = ftp.login(user=Benutzername, passwd=Passwort, acct=Verzeichnis)
    
    if loginResult:
        print "Successfully logged into FTP server"
    else:
        return

    ftp.cwd(dirname=Verzeichnis)
    ftp.dir()
    ftp.rmd(dirname=package.GetDescriptorString())
    ftp.mkd(dirname=package.GetDescriptorString())
    ftp.ntransfercmd(cmd="STOR *", rest=None)

