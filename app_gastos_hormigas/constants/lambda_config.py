from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
)
###
# Constantes para la configuración de las lambdas
###

class LambdaConfig:
    # TODO: investigar después como agregar los layers.
    configs = [
        {
            "id": "lambda-users-stack",
            "runtime": _lambda.Runtime.PYTHON_3_12,
            "handler": "app.lambda_handler",
            "code": "../src/code/users"
        }
        # {
        #     "id": "lambda-expenses-stack",
        #     "runtime": _lambda.Runtime.PYTHON_3_12,
        #     "handler": "app.lambda_handler",
        #     "code": "../src/code/expenses"
        # },
        # {
        #     "id": "lambda-categories-stack",
        #     "runtime": _lambda.Runtime.PYTHON_3_12,
        #     "handler": "app.lambda_handler",
        #     "code": "../src/code/categories"
        # }
    ]
