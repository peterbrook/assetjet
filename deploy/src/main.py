"""
This script freezes the app using Esky with cx_Freeze, produces a Windows 
Installer with Inno Setup and pushes everything onto the web server. Esky also
produces patch files to enable updates without the need to download everything.

Prerequisites:
- Update the version string in the __init__file of the assetjet package
- Inno Setup >5.5 must be installed
- The following file ("ftserver.cfg") must be present in the same directory:
[Deploy]
ftpserver = <...>
username = <...>
password = <...>
innoSetupLoc = C:\Program Files (x86)\Inno Setup 5\iscc

Once the app has been frozen, a Windows installer is created with Inno Setup.
The Windows installer follows the Esky folder structure to enable updates.
Then, the Esky zip file, the patch files and the installer are uploaded onto
the web server. The last two steps are optional (-> Settings)

TODO: extend for Mac and Linux
"""
import sys, os
from subprocess import call
import distutils.util
from glob import glob
from assetjet import __version__
import publish
import build_inno_setup

################################ SETTINGS #####################################
environment = 'DEV' # Set to 'DEV' or 'PROD'
createInstaller = False
pushToServer = False # push esky zip file, patch files and installer onto server
###############################################################################

# Name of Application
if environment.lower() == 'dev':
    appName = 'AssetJetDev'
elif environment.lower() == 'prod':
    appName = 'AssetJet'

# Name of Executable
if sys.platform in ['win32','cygwin','win64']:
    exeName = '{0}.exe'.format(appName)
    
# Name of Esky zip file (without zip extension)
filename = '{0}-{1}.{2}'.format(appName, __version__,
                                distutils.util.get_platform())

# Name of Windows installer
if distutils.util.get_platform() in ['win-amd64']:
    installerName = '{0} {1} (64bit)'.format(appName, __version__)
else:
    installerName = '{0} {1} (32bit)'.format(appName, __version__)

def main():
    # Freeze the files and create patches if older version are in dist folder
    call('python setup_esky.py bdist_esky_patch')
    print('done with esky')
    # Create installer
    if createInstaller:
        build_inno_setup.build_installer(appName, filename, installerName)
    # Push files onto web server
    if pushToServer:    
        try:
            ftp = publish.connect(environment)
            publish.push(os.path.abspath(os.path.join('dist', installerName + '.exe')), ftp)
            for fullpath in glob('dist/{0}*'.format(filename)):
                publish.push(fullpath, ftp)
        except Exception, ex:
            print(ex)
        finally:
            logout = ftp.quit()
            print(logout)

if __name__ == '__main__':
    main()
    
    