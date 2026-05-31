from pymongo import MongoClient
from config import Config
import datetime


class Mongo:

    def __init__(self):
        '''
        Establish connection to the MongoDB database.
        '''
        try:
            config = Config()
            self.client = MongoClient(host=config.dbhost,
                                      port=config.dbport,
                                      username=config.dbuser,
                                      password=config.dbpass,
                                      authSource=config.dbauth)
            self.db = self.client[config.dbname]
        except Exception:
            raise RuntimeError("Could not connect to database.")
        return None

    def find_result(self, latitude, longitude):
        try:
            result = self.db.results.findOne({
                    "location": {"$nearSphere": {"$geometry": {
                        "type": "Point", "coordinates": [longitude, latitude]},
                        "$maxDistance": Config.max_distance_meters}}})
            return result.get('result')
        except Exception:
            return None

    def store_result(self, latitude, longitude, result):
        try:
            self.db.results.insert_one({"location": {
                        "type": "Point", "coordinates": [longitude, latitude]},
                        "result": result, "timestamp": datetime.utcnow()})
            return True
        except Exception:
            return False
