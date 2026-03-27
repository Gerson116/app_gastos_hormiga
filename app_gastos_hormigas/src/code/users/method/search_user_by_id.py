from app_gastos_hormigas.constants.table_config import TableName
from app_gastos_hormigas.src.shared.commond import dynamodb_config
from app_gastos_hormigas.src.shared.repositories.user import search_user_by_id_ddb
from app_gastos_hormigas.src.shared.response_template import ResponseTemplate


def search_user_by_id(event, env):
    try:
        # TODO: DEBO CREAR UNA RAMA PARA GUARDAR LAS BITACORAS.
        path_params = event.get("pathParameters")

        user_id: str = path_params.get("userId")

        temp_table_name = f"{TableName.USERS}_{env}"

        data = search_user_by_id_ddb(user_id=user_id, table_name=temp_table_name)

        return data

    except Exception as e:
        print(e)
        return ResponseTemplate.error_response(str(e))
    finally:
        print('Finalizo el proceso')
