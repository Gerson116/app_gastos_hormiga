from app_gastos_hormigas.constants.table_config import TableName
from app_gastos_hormigas.src.shared.repositories.user import search_user_by_general_data_ddb
from app_gastos_hormigas.src.shared.response_template import ResponseTemplate


def search_user_by_general_data(event, env):
    try:
        # TODO: DEBO CREAR UNA RAMA PARA GUARDAR LAS BITACORAS.
        query_params = event.get("queryStringParameters") if event.get("queryStringParameters") is not None else None

        user_id = query_params.get("userId") if query_params is not None else None
        identification = query_params.get("identification") if query_params is not None else None
        phone_number = query_params.get("phoneNumber") if query_params is not None else None

        temp_table_name = f"{TableName.USERS}_{env}"

        if user_id is not None:
            data = search_user_by_general_data_ddb(user_id=user_id, table_name=temp_table_name)
            if not data:
                return ResponseTemplate.not_found("Usuario no encontrado")
            return ResponseTemplate.data_response(data)

        elif identification is not None:
            data = search_user_by_general_data_ddb(identification=identification, table_name=temp_table_name)
            if not data:
                return ResponseTemplate.not_found("Usuario no encontrado")
            return ResponseTemplate.data_response(data)

        elif phone_number is not None:
            data = search_user_by_general_data_ddb(phone_number=phone_number, table_name=temp_table_name)
            if not data:
                return ResponseTemplate.not_found("Usuario no encontrado")
            return ResponseTemplate.data_response(data)

        data = search_user_by_general_data_ddb(table_name=temp_table_name)
        return ResponseTemplate.data_response(data)

    except Exception as e:
        print(e)
        return ResponseTemplate.error_response(str(e))
    finally:
        print('Finalizo el proceso')
