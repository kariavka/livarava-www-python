from livereload import Server, shell
from app import app
from settings import PORT

app.debug = True

server = Server(app.wsgi_app)
server.watch('assets/scss/*.scss', shell('make styles'))
server.serve(port=PORT, debug=True)
