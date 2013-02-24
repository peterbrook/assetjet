import os
from subprocess import call
import shutil
import distutils.util
from zipfile import ZipFile
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
    
    # Clean
    if os.path.isdir(os.path.join('dist', 'AssetJet')):
        print('Deleting existing folder...')
        shutil.rmtree(os.path.join('dist', 'AssetJet'))
       
    if os.path.isfile(os.path.join('dist', installerName, '.exe')):
        print('Deleting existing installer...')
        os.remove(os.path.join('dist', installerName, '.exe'))
    
    # Unzip file
    print('unzipping')
    with ZipFile(os.path.join('dist', filename + '.zip'),"r") as zf:
        zf.extractall(os.path.join('dist', 'AssetJet'))
    
    # Bring into esky folder structure
    print('bring into esky folder structure')
    shutil.move(os.path.join('dist','AssetJet', filename),
                os.path.join('dist','AssetJet','appdata',filename))
    
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