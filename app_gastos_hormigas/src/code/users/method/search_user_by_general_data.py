
from app_gastos_hormigas.src.shared.response_template import ResponseTemplate

def search_user_by_general_data(event):
    try:
        # TODO: DEBO CREAR UNA RAMA PARA GUARDAR LAS BITACORAS.
        query_params = event.get("queryStringParameters") or None

        user_id: str | None = query_params.get("userId", None)
        identification: str | None = query_params.get("identification", None)
        phone_number: str | None = query_params.get("phoneNumber", None)

        # TODO: ELIMINAR ESTE BLOQUE DE CODIGO.

        leaked_data = []

        if user_id is not None:
            leaked_data = [item for item in data if item["userId"] == int(user_id)]
            if len(leaked_data) == 0:
                return ResponseTemplate.not_found("Usuario no encontrado")
            return ResponseTemplate.data_response(leaked_data)

        elif identification is not None:
            leaked_data = [item for item in data if identification in item["cedula"]]
            if len(leaked_data) == 0:
                return ResponseTemplate.not_found("Usuario no encontrado")
            return ResponseTemplate.data_response(leaked_data)

        elif phone_number is not None:
            leaked_data = [item for item in data if phone_number in item["phoneNumber"]]
            if len(leaked_data) == 0:
                return ResponseTemplate.not_found("Usuario no encontrado")
            return ResponseTemplate.data_response(leaked_data)

        return ResponseTemplate.data_response(data)

    except Exception as e:
        print(e)
        return ResponseTemplate.error_response(str(e))
    finally:
        print('Finalizo el proceso')

