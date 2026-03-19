import requests
import threading
import argparse

from flask import Flask


class Server:
    
    def __init__(self, port, host):
        self.port = port
        self.host = host
        
        self.app = Flask(__name__)

        self.app.add_url_rule('')

    def shutdown(self):
        pass

    def server_shutdown(self):
        pass


