from pymongo import MongoClient
from src.utils.settings import Settings

config = Settings.get_config()

client = MongoClient(config.MONGO_URI)