#!interpreter/bin/python
from api import api
# from app import app
api.run(debug=True)
# app.run(debug=True)


# Custom converter for dates in urls, see util.py
from .util import DateConverter
app.url_map.converters['date'] = DateConverter