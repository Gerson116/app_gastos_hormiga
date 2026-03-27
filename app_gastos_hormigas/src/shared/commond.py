import boto3

from app_gastos_hormigas.constants.constants import REGION_NAME


def dynamodb_config(table_name: str):
    dynamodb = boto3.resource('dynamodb', region_name=REGION_NAME)
    table = dynamodb.Table(table_name)
    return table