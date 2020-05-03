import json

from flask import Response, request, jsonify
from flask_restful import Resource
from sommelier.databases.models import Wine, possible_filters


class WinesApi(Resource):
    def get(self):
        query = Wine.objects.filter(**request.environ['filters'])
        query = query.order_by(*request.environ['sort'])
        wine_pagination = query.paginate(
            **request.environ['page']
        )
        previous_page = wine_pagination.prev_num if wine_pagination.has_prev else None
        current_page = wine_pagination.page
        total_pages = wine_pagination.pages
        next_page =  wine_pagination.next_num if wine_pagination.has_next else None
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