from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as _apigw,
)

from app_gastos_hormigas.constants.table_config import TableName

###
# Constantes para la configuración de las lambdas
###

RUNTIME = _lambda.Runtime.PYTHON_3_12

class LambdaConfig:
    # TODO: investigar después como agregar los layers.
    configs = [
        #   region lambda users
        {
            "id": "search-user-by-general-data",
            "runtime": RUNTIME,
            "handler": "app_gastos_hormigas.src.code.users.app.lambda_handler",
            "code": "../../",
            "route": "/user/search-user",
            "method": "GET",
            "tagTable": TableName.USERS,
            "requestParameters": {
                "method.request.querystring.userId": False,
                "method.request.querystring.identification": False,
                "method.request.querystring.phoneNumber": False,
                "method.request.querystring.state": False
            }
        },
        {
            "id": "search-user-by-id",
            "runtime": RUNTIME,
            "handler": "app_gastos_hormigas.src.code.users.app.lambda_handler",
            "code": "../../",
            "route": "/user/{userId}",
            "method": "GET",
            "tagTable": TableName.USERS,
            "requestParameters": {
                "method.request.path.userId": True
            }
        },
        {
            "id": "add-user",
            "runtime": RUNTIME,
            "handler": "app_gastos_hormigas.src.code.users.app.lambda_handler",
            "code": "../../",
            "route": "/user/add",
            "method": "POST",
            "tagTable": TableName.USERS,
            "schema": _apigw.JsonSchema(
                type=_apigw.JsonSchemaType.OBJECT,
                required=["name", "lastName", "age", "identification", "phoneNumber"],
                properties={
                    "name": _apigw.JsonSchema(type=_apigw.JsonSchemaType.STRING, max_length=50),
                    "lastName": _apigw.JsonSchema(type=_apigw.JsonSchemaType.STRING, max_length=50),
                    "age": _apigw.JsonSchema(type=_apigw.JsonSchemaType.INTEGER, minimum=1, maximum=150),
                    "identification": _apigw.JsonSchema(type=_apigw.JsonSchemaType.STRING, min_length=11, max_length=11),
                    "phoneNumber": _apigw.JsonSchema(type=_apigw.JsonSchemaType.STRING, min_length=10, max_length=15),
                    "state": _apigw.JsonSchema(type=_apigw.JsonSchemaType.STRING, min_length=2, max_length=2)
                }
            )
        },
        {
            "id": "update-user",
            "runtime": RUNTIME,
            "handler": "app_gastos_hormigas.src.code.users.app.lambda_handler",
            "code": "../../",
            "route": "/user/update",
            "method": "PATCH",
            "tagTable": TableName.USERS,
            "schema": _apigw.JsonSchema(
                type=_apigw.JsonSchemaType.OBJECT,
                required=["userId"],
                properties={
                    "userId": _apigw.JsonSchema(type=_apigw.JsonSchemaType.STRING),
                    "name": _apigw.JsonSchema(type=_apigw.JsonSchemaType.STRING, max_length=50),
                    "lastName": _apigw.JsonSchema(type=_apigw.JsonSchemaType.STRING, max_length=50),
                    "age": _apigw.JsonSchema(type=_apigw.JsonSchemaType.INTEGER, minimum=1, maximum=150),
                    "identification": _apigw.JsonSchema(type=_apigw.JsonSchemaType.STRING, min_length=11, max_length=11),
                    "phoneNumber": _apigw.JsonSchema(type=_apigw.JsonSchemaType.STRING, min_length=10, max_length=15),
                    "state": _apigw.JsonSchema(type=_apigw.JsonSchemaType.STRING, min_length=2, max_length=2),
                }
            )
        },
        {
            "id": "delete-user",
            "runtime": RUNTIME,
            "handler": "app_gastos_hormigas.src.code.users.app.lambda_handler",
            "code": "../../",
            "route": "/user/delete/{userId}",
            "method": "DELETE",
            "tagTable": TableName.USERS,
            "requestParameters": {
                "method.request.path.userId": True
            }
        },
        #   endregion
    ]
