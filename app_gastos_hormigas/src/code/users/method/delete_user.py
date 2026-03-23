from http import HTTPStatus

from app_gastos_hormigas.constants.constants import UserState
from app_gastos_hormigas.constants.table_config import TableName
from app_gastos_hormigas.src.shared.commond import dynamodb_config
from app_gastos_hormigas.src.shared.repositories.register_information import register_and_update_data
from app_gastos_hormigas.src.shared.response_template import ResponseTemplate

def delete_user(event):
    try:
        # TODO: DEBO CREAR UNA RAMA PARA GUARDAR LAS BITACORAS.
        path_params = event.get("pathParameters")

        user_id: str = path_params.get("userId")

        table = dynamodb_config(table_name=TableName.USERS)

        response = table.get_item(
            Key={
                'userId': user_id,
            }
        )

        obj_user = response.get('Item')

        if obj_user is  None:
            return ResponseTemplate.not_found("No se encontro el usuario")

        obj_user['state'] = UserState.INACTIVE

        response = register_and_update_data(
            table_name=TableName.USERS,
            data=obj_user
        )

        print("se elimino el usuario.")
        return response

    except Exception as e:
        print(e)
        return ResponseTemplate.error_response(str(e))
    finally:
        print('Finalizo el proceso')

