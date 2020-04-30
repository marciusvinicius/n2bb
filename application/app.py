from flask import Flask
from flask_restful import Api
from sommelier.databases.db import initialize_db
from sommelier.resources.routers import initialize_routes

app = Flask(__name__)
api = Api(app)

#TODO: Move for config or env
#TODO: Use postgresql or mysql
app.config['MONGODB_SETTINGS'] = {
 'host': 'mongodb://wine-db:27017/sommelier',
 'username': 'root',
 'password': 'rootpassword',
}

initialize_db(app)
initialize_routes(api)
