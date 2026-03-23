import json

from app_gastos_hormigas.constants.constants import UserState
from app_gastos_hormigas.constants.table_config import TableName
from app_gastos_hormigas.src.shared.repositories.register_information import register_and_update_data
from app_gastos_hormigas.src.shared.response_template import ResponseTemplate


def create_user(event):
    try:
        # TODO: DEBO CREAR UNA RAMA PARA GUARDAR LAS BITACORAS.
        body = json.loads(event["body"])
        user = {
            "name": body["name"],
            "lastName": body["lastName"],
            "age": body["age"],
            "phoneNumber": body["phoneNumber"],
            "identification": body["identification"],
            "state": UserState.ACTIVE
        }

        response = register_and_update_data(
            data=user,
            table_name=TableName.USERS
        )
        print('Se agrego un nuevo usuario')
        return response

    except Exception as e:
        print(e)
        return ResponseTemplate.error_response(str(e))
    finally:
        print('Finalizo el proceso')

