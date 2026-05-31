import os


class Config:

    def __init__(self):

        # Range
        self.max_distance_meters = os.environ.get('MAXDISTANCE', 100)

        # MongoDB Database
        self.dbhost = os.environ.get('DBHOST', 'localhost')
        self.dbport = os.environ.get('DBPORT', 27017)
        self.dbuser = os.environ.get('DBUSER', '')
        self.dbpass = os.environ.get('DBPASS', '')
        self.dbauth = os.environ.get('DBAUTH', '')
        self.dbname = os.environ.get('DBNAME', 'cache')

        # CORS - Cross-Origin Resource Access
        self.cors = os.environ.get('CORS', '*')

        # Google API
        self.apikey = os.environ.get('APIKEY', None)  # TODO: transfer to API
        self.apiurl = os.environ.get(
            'APIURL',
            "https://maps.googleapis.com/maps/api/geocode/json?" +
            "latlng={},{}&key={}")

        return None
