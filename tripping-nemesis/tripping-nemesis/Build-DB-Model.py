<<<<<<< HEAD
# -*- coding: utf-8 -*-

import os, sys
import migrate.versioning.api as dbm

sys.path.append(os.curdir + "\\src\\UI")
sys.path.append(os.curdir + "\\src\\DB")
sys.path.append(os.curdir + "\\src\\models")

repoName= "DB_REPO"

dbm.create(repoName, "tn")
dbm.version_control("sqlite:///src/DB/Data/stocks.db", repoName)
dbm.create_model("sqlite:///src/DB/Data/stocks.db", repoName)
=======
# -*- coding: utf-8 -*-

import os, sys
import migrate.versioning.api as dbm

sys.path.append(os.curdir + "\\src\\UI")
sys.path.append(os.curdir + "\\src\\DB")
sys.path.append(os.curdir + "\\src\\models")

repoName= "DB_REPO"

dbm.create(repoName, "tn")
dbm.version_control("sqlite:///src/DB/Data/stocks.db", repoName)
dbm.create_model("sqlite:///src/DB/Data/stocks.db", repoName)
>>>>>>> f603b51d879d749ada65ed0bbb576e7658990349
#dbm.make_update_script_for_model()