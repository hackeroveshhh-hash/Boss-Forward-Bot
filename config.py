from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "23903140"))
    API_HASH = environ.get("API_HASH", "579f1bcf3eac1660d81ef34b09906012")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "vjbot") 
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://bosstgbots_db_user:DiRFdWd2U9kHoP4j@cluster0.g6p3m4j.mongodb.net/?appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "vj-forward-bot")
    BOT_OWNER = int(environ.get("BOT_OWNER", "1416433622"))
    # New Configs
    LOG_ID = int(environ.get("LOG_ID", "-1003166629808"))
    WELCOME_IMG = "https://graph.org/file/f340b55f492b0ad0276a9-24b7dabf4b19a8d723.jpg"

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
