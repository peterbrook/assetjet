from ftplib import FTP
from subprocess import call
from deploy import package

FTPServer = ""
Benutzername = ""
Passwort = ""
Verzeichnis = ""

from ConfigParser import ConfigParser
cfg = ConfigParser()
cfg.read(filenames='dev.cfg')

FTPServer = cfg.get('Deploy', 'FTPServer')
Benutzername = cfg.get('Deploy', 'Benutzername')
Passwort = cfg.get('Deploy', 'Passwort')
Verzeichnis = cfg.get('Deploy', 'Verzeichnis')

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

