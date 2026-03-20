import json
from app_gastos_hormigas.src.shared.response_template import ResponseTemplate


def create_user(event):
    try:
        body = json.loads(event["body"])
        user = {
            "name": body["name"],
            "lastName": body["lastName"],
            "age": body["age"],
            "phoneNumber": body["phoneNumber"],
            "identification": body["identification"]
        }
        print('Se agrego un nuevo usuario')
        return ResponseTemplate.data_response(user)

    except Exception as e:
        print(e)
        return ResponseTemplate.error_response(str(e))
    finally:
        print('Finalizo el proceso')

