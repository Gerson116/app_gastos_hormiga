import json
from app_gastos_hormigas.src.shared.response_template import ResponseTemplate


def update_user(event):
    try:
        body = json.loads(event["body"])
        user = {
            "name": body.get("name", None),
            "lastName": body.get("lastName", None),
            "age": body.get("age", None),
            "phoneNumber": body.get("phoneNumber", None),
            "identification": body.get("identification", None)
        }
        print('Se actualizo un nuevo usuario')
        return ResponseTemplate.data_response(user)

    except Exception as e:
        print(e)
        return ResponseTemplate.error_response(str(e))
    finally:
        print('Finalizo el proceso')

