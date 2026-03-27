import json
import uuid

from app_gastos_hormigas.constants.constants import UserState
from app_gastos_hormigas.constants.table_config import TableName
from app_gastos_hormigas.src.shared.repositories.register_information import register_and_update_data
from app_gastos_hormigas.src.shared.response_template import ResponseTemplate

import json
import uuid


def create_user(event, env):
    try:
        # 1. IMPORTANTE: Convertir el string del body a un diccionario
        # Si event["body"] ya es un dict (por pruebas locales), usamos get
        body_raw = event.get("body", "{}")

        # Si el body es un string (como viene de API Gateway), lo cargamos
        if isinstance(body_raw, str):
            body = json.loads(body_raw)
        else:
            body = body_raw

        user_id = uuid.uuid4()

        # 2. Ahora sí puedes acceder a los campos como diccionario
        user = {
            "UserId": str(user_id),
            "name": body.get("name"),
            "lastName": body.get("lastName"),
            "age": int(body.get("age")),  # Aquí 'age' será el entero 28
            "phoneNumber": body.get("phoneNumber"),
            "identification": body.get("identification"),
            "state": UserState.ACTIVE
        }

        temp_table_name = f"{TableName.USERS}_{env}"

        response = register_and_update_data(
            data=user,
            table_name=temp_table_name
        )
        print('Se agrego un nuevo usuario')
        return response

    except Exception as e:
        print(f"Error detectado: {e}")
        return ResponseTemplate.error_response(str(e))
    finally:
        print('Finalizo el proceso')

