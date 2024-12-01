import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29790818"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1fa40d153769016ea15c007879668e9d")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://vishwajit87:k0ioXpsJu2DOVfGI@cluster0.e66qt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
