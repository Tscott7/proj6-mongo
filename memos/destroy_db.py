"""
Destroy the database for the specified user
(who must not be siteUserAdmin)
"""

import pymongo
from pymongo import MongoClient
import sys

import config
CONFIG = config.configuration()

MONGO_ADMIN_URL = "mongodb://{}:{}@{}:{}/proj6-mongo".format(
    CONFIG.DB_USER,
    CONFIG.DB_USER_PW,
    CONFIG.DB_HOST, 
    CONFIG.DB_PORT)

try: 
    dbclient = MongoClient(MONGO_ADMIN_URL)
    db = getattr(dbclient, CONFIG.DB)
    print("Got database")
    print("Attempting drop users")
    # db.command( {"dropAllUsersFromDatabase": 1 } )
    db.remove_user(CONFIG.DB_USER)
    print("Dropped database users for {}".format(CONFIG.DB_USER))
    db.command( {"dropDatabase": 1 } )
    print("Dropped database {}".format(CONFIG.DB))
except Exception as err:
    print("Failed")
    print(err)



        
