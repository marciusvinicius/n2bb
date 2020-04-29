import json
from flask import Response, request, jsonify
from flask_restful import Resource
from sommelier.databases.models import Wine


possible_filters = ["price", "title"]

class WinesApi(Resource):
    def get(self):
        query_params = request.args
        filters = {k:v for k, v in query_params.items() if k in possible_filters}
        query = Wine.objects.filter(**filters)
        page = query_params.get('page') or 1
        per_page = query_params.get('per_page') or 10
        wine_pagination = query.paginate(
            page=int(page),
            per_page=int(per_page)
        )
        previous_page = (wine_pagination.page - 1) or None
        current_page = wine_pagination.page
        total_pages = wine_pagination.pages
        next_page =  (current_page + 1) if (current_page + 1 <= total_pages) else None
        count = wine_pagination.total
        list_of_items = wine_pagination.items

        return jsonify({
            "previous_page": previous_page,
            "current_page": current_page,
            "next_page": next_page,
            "total_pages": total_pages,
            "data": list_of_items,
            "count": count
        })