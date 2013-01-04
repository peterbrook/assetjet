import os
from subprocess import call
import shutil
from zipfile import ZipFile
from deploy import package

name = 'AssetJet-{0}.win-amd64'.format(package.GetVersionString())

# Clean
if os.path.isdir(os.path.join('dist', 'AssetJet')):
    shutil.rmtree(os.path.join('dist', 'AssetJet'))
    
if os.path.isfile(os.path.join('dist', 'AssetJet.exe')):
    os.remove(os.path.join('dist', 'AssetJet.exe'))

# Unzip file
with ZipFile(os.path.join('dist', name + '.zip'),"r") as zf:
    zf.extractall(os.path.join('dist', 'AssetJet'))

# bring into esky folder structure
shutil.move(os.path.join('dist','AssetJet',name), os.path.join('dist','AssetJet','appdata',name))

# Compile it (Inno Setup has to be installed)
# TODO: pick up version string in iss file
call('"C:\Program Files (x86)\Inno Setup 5\iscc" inno_installer_64bit.iss')
