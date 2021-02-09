from wsgiref import simple_server
from routes.route import Router
from models.db import createConnection

createConnection()

app = Router.route()

if __name__ == '__main__':
    
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()