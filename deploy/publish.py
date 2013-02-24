import os
from ftplib import FTP
from ConfigParser import ConfigParser

def connect(environment):
    # read the connection settings from the config file
    cfg = ConfigParser()
    cfg.readfp(open('ftpserver.cfg'))  
    ftpserver = cfg.get('Deploy', 'ftpserver')
    username = cfg.get('Deploy', 'username')
    password = cfg.get('Deploy', 'password')
    directory = 'httpdocs/{0}/downloads'.format(environment.lower())
    
    # connect to host, default port
    ftp = FTP(host=ftpserver)  
    loginResult = ftp.login(username, password)
    ftp.cwd(directory)
    if loginResult:
        print('Successfully logged into FTP server')
        
    # return an ftp instance
    return ftp
    
def push(fullpath, ftp):
    # push the file onto the ftp server
    filename = os.path.split(fullpath)[1]
    with open(fullpath,'rb') as f:
        # ftp.storbinary takes a FILE object not a path
        print('Transfer starting: {0}'.format(filename))
        ftp.storbinary('STOR {0}'.format(filename), f)
        print('Transfer complete: {0}'.format(filename))