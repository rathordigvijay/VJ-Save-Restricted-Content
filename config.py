import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29790818"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1fa40d153769016ea15c007879668e9d")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://rathordigvijay:iRLHal8C7RdJoOnm@cluster0.qp239.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
