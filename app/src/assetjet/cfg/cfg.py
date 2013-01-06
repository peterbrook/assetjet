
import ConfigParser, os
from assetjet.util import util

fileName = 'app.cfg'
location = os.path.dirname(util.getBaseDir())

# If config file doesn't exist, create with defaults
# TODO: get db location from user input upon first startup
if not os.path.exists(os.path.join(location, fileName)):
    config = ConfigParser.RawConfigParser()
    config.add_section('Database')
    config.set('Database', 'filePath', r'C:\assetjet.db')
    config.add_section('Updates')
    config.set('Updates', 'url', r'www.assetjet.com/downloads')
    
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
