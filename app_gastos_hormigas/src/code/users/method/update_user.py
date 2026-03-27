import json

from app_gastos_hormigas.constants.table_config import TableName
from app_gastos_hormigas.src.shared.repositories.register_information import register_and_update_data
from app_gastos_hormigas.src.shared.response_template import ResponseTemplate


def update_user(event, env):
    try:
        # TODO: DEBO CREAR UNA RAMA PARA GUARDAR LAS BITACORAS.
        body_str = event.get("body", "{}")
        
        if isinstance(body_str, str):
            body = json.loads(body_str)
        else:
            body = body_str

        user_id = body.get("userId", None)

        if user_id is None:
            return ResponseTemplate.error_response("El campo usuario es requerido")

        user = {
            "UserId": user_id,
            "name": body.get("name", None),
            "lastName": body.get("lastName", None),
            "age": int(body.get("age")) if body.get("age") is not None else None,
            "phoneNumber": body.get("phoneNumber", None),
            "identification": body.get("identification", None),
            "state": body.get("state", None)
        }

        temp_table_name = f"{TableName.USERS}_{env}"

        response = register_and_update_data(
            data=user,
            table_name=temp_table_name
        )
        print('Se actualizo un nuevo usuario')
        return response

    except Exception as e:
        print(e)
        return ResponseTemplate.error_response(str(e))
    finally:
        print('Finalizo el proceso')

