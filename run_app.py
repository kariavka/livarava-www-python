from app import app
from settings import PORT

app.debug = True

app.run(port=PORT)
