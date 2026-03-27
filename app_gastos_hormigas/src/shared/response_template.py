import json
from decimal import Decimal
from http import HTTPStatus

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return int(obj) if obj % 1 == 0 else float(obj)
        return super(DecimalEncoder, self).default(obj)

class ResponseTemplate:
    HEADERS = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PUT, PATCH, DELETE",
        "Access-Control-Allow-Headers": "Content-Type, Authorization, x-amz-date, x-api-key, x-amz-security-token"
    }

    @staticmethod
    def success(data, code=HTTPStatus.OK):
        return {
            "statusCode": code,
            "headers": ResponseTemplate.HEADERS,
            "body": json.dumps(data, cls=DecimalEncoder)
        }

    @staticmethod
    def data_response(data, code=HTTPStatus.OK):
        return {
            "statusCode": code,
            "headers": ResponseTemplate.HEADERS,
            "body": json.dumps(data, cls=DecimalEncoder)
        }

    @staticmethod
    def created(message, code=HTTPStatus.CREATED):
        return {
            "statusCode": code,
            "headers": ResponseTemplate.HEADERS,
            "body": json.dumps({"message": message})
        }

    @staticmethod
    def data_paginated(data, page, limit, total, code=HTTPStatus.OK):
        return {
            "statusCode": code,
            "headers": ResponseTemplate.HEADERS,
            "body": json.dumps({
                "data": data,
                "pagination": {
                    "page": page,
                    "limit": limit,
                    "total": total
                }
            }, cls=DecimalEncoder)
        }

    @staticmethod
    def not_found(message, code=HTTPStatus.NOT_FOUND):
        return {
            "statusCode": code,
            "headers": ResponseTemplate.HEADERS,
            "body": json.dumps({
                "message": message
            })
        }

    @staticmethod
    def error_response(message, code=HTTPStatus.INTERNAL_SERVER_ERROR):
        return {
            "statusCode": code,
            "headers": ResponseTemplate.HEADERS,
            "body": json.dumps({
                "message": message
            })
        }
