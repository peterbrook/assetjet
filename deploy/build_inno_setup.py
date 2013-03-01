from subprocess import call
import distutils.util
from ConfigParser import ConfigParser
from assetjet import __version__

def build_installer(appName, filename, installerName):
    
    # read the connection settings from the config file
    cfg = ConfigParser()
    cfg.readfp(open('ftpserver.cfg'))  
    innoSetupLoc = cfg.get('Deploy', 'innoSetupLoc')
    
    # Flag to only allow 64bit versions to be installed on 64bit systems
    if distutils.util.get_platform() in ['win-amd64']:   
        architecturesAllowed = 'x64'
    else:   
        architecturesAllowed = ''
    
    # Compile it
    print('compiling inno setup..')
    call('{0} \
          "/dAppName={1}" \
          "/dVersion={2}" \
          "/dArchitecturesAllowed={3}" \
          "/dOutputBaseFilename={4}" \
          inno_installer.iss'.format(innoSetupLoc,
                                     appName,
                                     __version__,
                                     architecturesAllowed,
                                     installerName)
         )


if __name__ == '__main__':
    from main import appName, filename, installerName
    build_installer(appName, filename, installerName)