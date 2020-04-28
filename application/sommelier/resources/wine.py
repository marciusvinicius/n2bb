from flask import Response, request
from flask_restful import Resource
from sommelier.databases.models import Wine


class WinesApi(Resource):
    def get(self):
        wines = Wine.objects().to_json()
        return Response(wines, mimetype="application/json", status=200)