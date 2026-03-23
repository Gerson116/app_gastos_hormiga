from typing import Any

from app_gastos_hormigas.constants.table_config import TableName
from app_gastos_hormigas.src.shared.commond import dynamodb_config
from app_gastos_hormigas.src.shared.response_template import ResponseTemplate


def search_user_by_general_data(
    user_id: int | None = None,
    identification: str | None = None,
    phone_number: str | None = None
):
    try:
        table = dynamodb_config(table_name=TableName.USERS)

        response: Any | None = None

        if user_id is not None:
            response = table.get_item(
                Key={
                    'userId': user_id,
                }
            )
        elif identification is not None:
            response = table.get_item(
                Key={
                    'identification': identification,
                }
            )
        elif phone_number is not None:
            response = table.get_item(
                Key={
                    'phoneNumber': phone_number,
                }
            )
        else:
            response = table.get_item()

        result = response.get('Item')

        if result is not None:
            return ResponseTemplate.data_response(result)

        return ResponseTemplate.not_found("No se encontraron datos.")

    except Exception as e:
        print(e)

def search_user_by_id(user_id: int | None = None):
    try:
        table = dynamodb_config(table_name=TableName.USERS)
        response: Any | None = None

        if user_id is not None:
            response = table.get_item(
                Key={
                    'userId': user_id,
                }
            )

        result = response.get('Item')

        if result is not None:
            return ResponseTemplate.data_response(result)

        return ResponseTemplate.not_found("No se encontraron datos.")

    except Exception as e:
        print(e)