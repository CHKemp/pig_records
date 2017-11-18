#!interpreter/bin/python
from app import app
from api import api
api.run(debug=True)
app.run(debug=True)
