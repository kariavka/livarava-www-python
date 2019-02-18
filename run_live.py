from livereload import Server
from app import app

app.debug = True

server = Server(app.wsgi_app)
server.watch('/static/css/app.css')
server.watch('/templates/index.html')
server.serve()
