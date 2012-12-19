import os, sys
import migrate.versioning.api as dbm

sys.path.append(os.curdir + "\\src\\UI")
sys.path.append(os.curdir + "\\src\\DB")
sys.path.append(os.curdir + "\\src\\models")

repoName= "DB_REPO"

dbm.create(repoName, "tn")
dbm.version_control("sqlite:///src/DB/Data/stocks.db", repoName)
dbm.create_model("sqlite:///src/DB/Data/stocks.db", repoName)
