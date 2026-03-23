from aws_cdk.aws_apigatewayv2_integrations import HttpLambdaIntegration
from aws_cdk.aws_apigatewayv2 import HttpApi, HttpMethod
import os

from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as _apigw
)
from constructs import Construct

from app_gastos_hormigas.constants.lambda_config import LambdaConfig

DIRNAME = os.path.dirname(__file__)

class GastosHormigasLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, env: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        rest_api = _apigw.RestApi(
            self,
            f"gastos-hormigas-api-{env}"
        )

        request_validator = _apigw.RequestValidator(
            self,
            f"gastos-hormigas-request-validator-{env}",
            rest_api=rest_api,
            validate_request_body=True,
            validate_request_parameters=True
        )

        for lambda_config in LambdaConfig.configs:
            
            lambda_id = lambda_config["id"] + "-" + env

            lambda_function = _lambda.Function(
                self,
                id=lambda_id,
                function_name=lambda_id,
                runtime=lambda_config["runtime"],
                handler=lambda_config["handler"],
                code=_lambda.Code.from_asset(
                    os.path.join(DIRNAME, lambda_config["code"]),
                    exclude=[".venv", "node_modules", ".git", "cdk.out", "__pycache__"]
                )
            )

            # region Integraciones con API Gateway
            lambda_integration = _apigw.LambdaIntegration(
                lambda_function
            )

            resource = rest_api.root.resource_for_path(lambda_config["route"])

            request_models = None

            if "schema" in lambda_config:
                model_name = f"RequestModel{lambda_config['id']}{env}".replace("-", "").replace("_", "")
                
                model = rest_api.add_model(
                    f"request-model-{lambda_config['id']}-{env}",
                    content_type="application/json",
                    model_name=model_name,
                    schema=lambda_config["schema"]
                )
                request_models = {
                    "application/json": model
                }
            
            resource.add_method(
                lambda_config["method"],
                lambda_integration,
                request_validator=request_validator,
                request_models=request_models,
                request_parameters=lambda_config.get("requestParameters")
            )
            # endregion

            
