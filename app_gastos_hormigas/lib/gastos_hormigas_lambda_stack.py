import os

from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
)
from constructs import Construct

from app_gastos_hormigas.constants.lambda_config import LambdaConfig

DIRNAME = os.path.dirname(__file__)

class GastosHormigasLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, env: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # TODO: INVESTIGAR COMO CREAR MULTIPLES LAMBDAS DESDE UN MISMO ARCHIVO

        for lambda_config in LambdaConfig.configs:
            
            lambda_id = lambda_config["id"] + "-" + env

            lambda_function = _lambda.Function(
                self,
                id=lambda_id,
                runtime=lambda_config["runtime"],
                handler=lambda_config["handler"],
                code=_lambda.Code.from_asset(os.path.join(DIRNAME, lambda_config["code"]))
            )
