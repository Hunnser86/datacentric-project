import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "your_secret_key_here")
os.environ.setdefault("MONGO_URI", "mongodb+srv://root:MongoMogo@myfirstcluster.vjycg.mongodb.net/task_manager?retryWrites=true&w=majority")
os.environ.setdefault("MONGO_DBNAME", "task_manager")