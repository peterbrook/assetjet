import ConfigParser, os
from assetjet.util import util
import sys
from os.path import pardir

# appName will be AssetJet or AssetJetDev
appName = os.path.splitext(os.path.split(sys.executable)[1])[0]

# set name and location of config file
# Esky Hack: to make patch work, no new files may be in the appdata folder,
# therefore store it in the parent of main.py
fileName = 'app.cfg'
location = os.path.join(util.getBaseDir(), pardir, pardir)
filePath = os.path.join(location, fileName)
#print location
#print filePath

# If config file doesn't exist, create with defaults
# TODO: get db location from user input upon first startup
if not os.path.exists(os.path.join(location, fileName)):
    config = ConfigParser.RawConfigParser()
    config.add_section('Database')
    config.set('Database', 'filePath', r'C:\assetjet.db')
    config.add_section('Updates')
    if appName == 'AssetJet':
        config.set('Updates', 'url', r'http://www.assetjet.com/prod/downloads')
    elif appName == 'AssetJetDev':
        config.set('Updates', 'url', r'http://www.assetjet.com/dev/downloads')
    elif appName =='python': # when running from source
        config.set('Updates', 'url', r'http://localhost:8000')
    
    with open(os.path.join(location, fileName), 'w') as configfile:
        config.write(configfile)


class Cfg(ConfigParser.ConfigParser):
    DbFileName = ""
    UpdateUrl = ""
    def __init__(self, cfgFile=None):
        ConfigParser.ConfigParser.__init__(self)
        if cfgFile is None:
            return
        self.DbFileName = str(cfgFile.get('Database', 'filePath'))
        self.UpdateUrl = str(cfgFile.get('Updates', 'url'))    
        

config = ConfigParser.ConfigParser()
config.readfp(open(os.path.join(location, fileName)))
root = Cfg(config)
