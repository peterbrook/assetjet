import ConfigParser, os
from assetjet.util import util
import sys
from os.path import pardir

# appName will be AssetJet or AssetJetDev
appName = os.path.splitext(os.path.split(sys.executable)[1])[0]

# set name and location of config file
fileName = 'app.cfg'
location = os.path.abspath(os.path.join(util.getBaseDir(), pardir, pardir))
filePath = os.path.abspath(os.path.join(location, fileName))
print location
print filePath

# If config file doesn't exist, create with defaults
if not os.path.exists(os.path.join(location, fileName)):
    config = ConfigParser.RawConfigParser()
    config.add_section('Updates')
    if appName == 'AssetJet':
        config.set('Updates', 'url', r'http://www.assetjet.com/prod/downloads')
    elif appName == 'AssetJetDev':
        config.set('Updates', 'url', r'http://www.assetjet.com/dev/downloads')
    else: # when running from source
        config.set('Updates', 'url', r'http://localhost:8000')
    
    with open(os.path.join(location, fileName), 'w') as configfile:
        config.write(configfile)

class Cfg(ConfigParser.ConfigParser):
    def __init__(self, cfgFile=None):
        ConfigParser.ConfigParser.__init__(self)
        if cfgFile.has_section('Database'):
            self.DbFileName = cfgFile.get('Database', 'dbfilename')
        self.UpdateUrl = cfgFile.get('Updates', 'url')   
    
def add_entry(section, option, value=None):
    config.read(filePath)

    if not config.has_section(section):
        config.add_section(section)    
    
    config.set(section, option, value)
    
    with open(filePath, 'w') as f:
        config.write(f)
    
    setattr(root, option, config.get(section, option))

config = ConfigParser.ConfigParser()
config.readfp(open(filePath))
root = Cfg(config)