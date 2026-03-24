from app_gastos_hormigas.src.shared.repositories.user import search_user_by_general_data_ddb
from app_gastos_hormigas.src.shared.response_template import ResponseTemplate


def search_user_by_general_data(event):
    try:
        # TODO: DEBO CREAR UNA RAMA PARA GUARDAR LAS BITACORAS.
        query_params = event.get("queryStringParameters") or None

        user_id: str | None = query_params.get("userId", None)
        identification: str | None = query_params.get("identification", None)
        phone_number: str | None = query_params.get("phoneNumber", None)

        if user_id is not None:
            data = search_user_by_general_data_ddb(user_id=int(user_id))
            if len(data) == 0:
                return ResponseTemplate.not_found("Usuario no encontrado")
            return ResponseTemplate.data_response(data)

        elif identification is not None:
            data = search_user_by_general_data_ddb(identification=identification)
            if len(data) == 0:
                return ResponseTemplate.not_found("Usuario no encontrado")
            return ResponseTemplate.data_response(data)

        elif phone_number is not None:
            data = search_user_by_general_data_ddb(phone_number=phone_number)
            if len(data) == 0:
                return ResponseTemplate.not_found("Usuario no encontrado")
            return ResponseTemplate.data_response(data)

        data = search_user_by_general_data_ddb()

        return ResponseTemplate.data_response(data)

    except Exception as e:
        print(e)
        return ResponseTemplate.error_response(str(e))
    finally:
        print('Finalizo el proceso')
