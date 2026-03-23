
import json
from http import HTTPStatus
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
            "body": json.dumps(data)
        }

    @staticmethod
    def data_response(data, code=HTTPStatus.OK):
        return {
            "statusCode": code,
            "headers": ResponseTemplate.HEADERS,
            "body": json.dumps(data)
        }

    @staticmethod
    def created(message, code=HTTPStatus.CREATED):
        return {
            "statusCode": code,
            "headers": ResponseTemplate.HEADERS,
            "body": None,
            "message": message
        }

    @staticmethod
    def data_paginated(data, page, limit, total, code=HTTPStatus.OK):
        return {
            "statusCode": code,
            "headers": ResponseTemplate.HEADERS,
            "body": {
                "data": json.dumps(data),
                "pagination": {
                    "page": page,
                    "limit": limit,
                    "total": total
                }
            }
        }

    @staticmethod
    def not_found(message, code=HTTPStatus.NOT_FOUND):
        return {
            "statusCode": code,
            "headers": ResponseTemplate.HEADERS,
            "body": {
                "message": message
            }
        }

    @staticmethod
    def error_response(message, code=HTTPStatus.INTERNAL_SERVER_ERROR):
        return {
            "statusCode": code,
            "headers": ResponseTemplate.HEADERS,
            "body": {
                "message": message
            }
        }
