from livereload import Server
from app import app

app.debug = True

server = Server(app.wsgi_app)
server.serve()
server.watch('/static/css/app.css')
