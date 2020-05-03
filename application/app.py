from flask_environ import get, collect, word_for_true
from flask import Flask,jsonify
from flask_restful import Api
from sommelier.databases.db import initialize_db
from sommelier.resources.routers import initialize_routes

from middleware.mid import FilterMiddleware


app = Flask(__name__)
api = Api(app)

app.wsgi_app = FilterMiddleware(app.wsgi_app)

app.config.update(collect(
    get('DEBUG', default=False, convert=word_for_true),
))

app.config['MONGODB_SETTINGS'] = collect(
    get('HOST', convert=str),
    get('USERNAME', convert=str),
    get('PASSWORD', convert=str),
)
print(app.config)

initialize_db(app)
initialize_routes(api)
