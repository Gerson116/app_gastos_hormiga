from typing import Any
from boto3.dynamodb.conditions import Attr

from app_gastos_hormigas.constants.table_config import TableName
from app_gastos_hormigas.src.shared.commond import dynamodb_config
from app_gastos_hormigas.src.shared.response_template import ResponseTemplate


def search_user_by_general_data_ddb(
    user_id: str | None = None,
    identification: str | None = None,
    phone_number: str | None = None,
    table_name: str | None = None
):
    try:
        table = dynamodb_config(table_name=table_name)
        result = []

        if user_id is not None:
            response = table.get_item(Key={'UserId': user_id})
            item = response.get('Item')
            if item:
                result = [item]
        elif identification is not None:
            response = table.scan(FilterExpression=Attr('identification').eq(identification))
            result = response.get('Items', [])
        elif phone_number is not None:
            response = table.scan(FilterExpression=Attr('phoneNumber').eq(phone_number))
            result = response.get('Items', [])
        else:
            response = table.scan()
            result = response.get('Items', [])

        return result

    except Exception as e:
        print(e)
        return []

def search_user_by_id_ddb(
        user_id: str | None = None,
        table_name: str | None = None
):
    try:
        table = dynamodb_config(table_name=table_name)
        response: Any | None = None

        if user_id is not None:
            response = table.get_item(
                Key={
                    'UserId': user_id,
                }
            )

        result = response.get('Item')

        if result is not None:
            return ResponseTemplate.data_response(result)

        return ResponseTemplate.not_found("No se encontraron datos.")

    except Exception as e:
        print(e)