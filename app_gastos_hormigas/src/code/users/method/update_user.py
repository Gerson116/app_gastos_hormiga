import json

from app_gastos_hormigas.constants.table_config import TableName
from app_gastos_hormigas.src.shared.repositories.register_information import register_and_update_data
from app_gastos_hormigas.src.shared.response_template import ResponseTemplate


def update_user(event):
    try:
        # TODO: DEBO CREAR UNA RAMA PARA GUARDAR LAS BITACORAS.
        body = json.loads(event["body"])
        user = {
            "userId": body["userId"],
            "name": body.get("name", None),
            "lastName": body.get("lastName", None),
            "age": body.get("age", None),
            "phoneNumber": body.get("phoneNumber", None),
            "identification": body.get("identification", None)
        }
        response = register_and_update_data(
            data=user,
            table_name=TableName.USERS
        )
        print('Se actualizo un nuevo usuario')
        return response

    except Exception as e:
        print(e)
        return ResponseTemplate.error_response(str(e))
    finally:
        print('Finalizo el proceso')

