from urllib.request import urlopen
from well.params import *

class Utils:

    def __init__(self):
        self.API_URL = API_URL
        self.PORT = API_PORT
        self.connection = None

    def check_connection(self):
        try:
            url = f"{self.API_URL}:{self.PORT}"
            self.connection = True if urlopen(url, timeout=3) else False
        except:
            self.connection = False
        return self.connection
