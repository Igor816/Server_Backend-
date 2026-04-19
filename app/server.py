import requests
import threading
import argparse
from utils import config_parser

from flask import Flask, request


class Server:
    
    def __init__(self, port, host):
        self.port = port
        self.host = host
        
        self.app = Flask(__name__)#Создание приложения

        self.app.add_url_rule('/shutdown', view_func=self.shutdown)#Выключает сервер для удобства.Тест
        self.app.add_url_rule('/home', view_func=self.get_home) 
        self.app.add_url_rule('/', view_func=self.get_home)
        self.app.add_url_rule('/', view_func=self.run_server)

    def run_server(self):#start servers
        self.server = threading.Thread(target=self.app.run, kwargs={'host': self.host, 'port': self.port})
        self.server.start()
        return self.server

    def server_shutdown(self):#Соеденение с серверром
        requests.get(f'https://{self.host}:{self.port}/shutdown')


    def shutdown(self):#Выключает наш сервер 
        terminate_func = request.environ.get('werkzeug.server.shutdown')#Получение фукции 
        if terminate_func:
            terminate_func()



    def get_home(self):
        return "Hello, api server"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, dest='config')#добавление файла аргумента

    args = parser.parse_args()#Сохраняем аргументы

    config = config_parser(args.config)#Считываем конфиг файл
    server_host = config['SERVER_HOST']
    server_port = config['SERVER_PORT']

    server = Server(
        port = server_port,
        host = server_host
    )
    
    server.run_server()

    