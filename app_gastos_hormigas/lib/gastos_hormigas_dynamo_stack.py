from app_gastos_hormigas.constants.table_config import TableConfig
import os

from aws_cdk import (
    Stack,
    aws_dynamodb as _dynamodb
)

from constructs import Construct

DIRNAME = os.path.dirname(__file__)

class GastosHormigasDynamoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, env: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.tables = {}

        for table in TableConfig.TABLES:
            table_name = f"{table['name']}_{env}"
            dynamodb_table = _dynamodb.Table(
                self,
                id=table_name,
                table_name=table_name,
                partition_key=_dynamodb.Attribute(
                    name=table["partition_key"],
                    type=_dynamodb.AttributeType.STRING
                ),
                billing_mode=_dynamodb.BillingMode.PAY_PER_REQUEST
            )

            self.tables[table_name] = dynamodb_table
