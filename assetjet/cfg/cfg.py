from sqlalchemy import create_engine
import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open('app.cfg'))
defaultDbFileName = str(config.get('Database', 'filePath'))

FilePath = defaultDbFileName
DbFileName = FilePath



