

from app_gastos_hormigas.src.shared.response_template import ResponseTemplate
def search_user_by_general_data(event):
    # TODO: POR EL MOMENTO VOY A RETORNAR DATOS DE PRUEBA.
    data = [
        {
            "userId": 1, "name": "Gerson", "lastName": "Santos Mateo", "age": 28,
            "phoneNumber": "8095551234", "cedula": "40223456781"
        },
        {
            "userId": 2, "name": "Ana", "lastName": "García Pérez", "age": 32,
            "phoneNumber": "8294445678", "cedula": "00198765432"
        },
        {
            "userId": 3, "name": "Carlos", "lastName": "López Rodríguez", "age": 45,
            "phoneNumber": "8493339012", "cedula": "03111223345"
        },
        {
            "userId": 4, "name": "María", "lastName": "Martínez Gómez", "age": 25,
            "phoneNumber": "8092223456", "cedula": "40255667789"
        },
        {
            "userId": 5, "name": "Juan", "lastName": "Fernández Ruiz", "age": 38,
            "phoneNumber": "8291117890", "cedula": "04799887764"
        },
        {
            "userId": 6, "name": "Laura", "lastName": "Díaz Sánchez", "age": 29,
            "phoneNumber": "8499991234", "cedula": "22344556670"
        },
        {
            "userId": 7, "name": "Pedro", "lastName": "Moreno Álvarez", "age": 51,
            "phoneNumber": "8098885678", "cedula": "00133445567"
        },
        {
            "userId": 8, "name": "Sofía", "lastName": "Romero Alonso", "age": 22,
            "phoneNumber": "8297779012", "cedula": "40288990012"
        },
        {
            "userId": 9, "name": "Luis", "lastName": "Gutiérrez Navarro", "age": 41,
            "phoneNumber": "8496663456", "cedula": "01255661123"
        },
        {
            "userId": 10, "name": "Carmen", "lastName": "Torres Domínguez", "age": 36,
            "phoneNumber": "8095557890", "cedula": "00122334456"
        },
        {
            "userId": 11, "name": "Jorge", "lastName": "Vázquez Ramos", "age": 48,
            "phoneNumber": "8294441234", "cedula": "05466778890"
        },
        {
            "userId": 12, "name": "Elena", "lastName": "Gil Blanco", "age": 27,
            "phoneNumber": "8493335678", "cedula": "40211229984"
        },
        {
            "userId": 13, "name": "Diego", "lastName": "Ramírez Castro", "age": 33,
            "phoneNumber": "8092229012", "cedula": "00177889901"
        },
        {
            "userId": 14, "name": "Lucía", "lastName": "Molina Ortiz", "age": 24,
            "phoneNumber": "8291113456", "cedula": "40233445568"
        },
        {
            "userId": 15, "name": "Miguel", "lastName": "Delgado Silva", "age": 55,
            "phoneNumber": "8499997890", "cedula": "06599001125"
        },
        {
            "userId": 16, "name": "Paula", "lastName": "Castro Núñez", "age": 30,
            "phoneNumber": "8098881234", "cedula": "00155443326"
        },
        {
            "userId": 17, "name": "Javier", "lastName": "Iglesias Medina", "age": 42,
            "phoneNumber": "8297775678", "cedula": "03188776659"
        },
        {
            "userId": 18, "name": "Marta", "lastName": "Garrido Rojas", "age": 26,
            "phoneNumber": "8496669012", "cedula": "40211998873"
        },
        {
            "userId": 19, "name": "Alejandro", "lastName": "Cortés Peña", "age": 39,
            "phoneNumber": "8095553456", "cedula": "00122883340"
        },
        {
            "userId": 20, "name": "Sara", "lastName": "Flores Cabrera", "age": 31,
            "phoneNumber": "8294447890", "cedula": "40255446672"
        },
        {
            "userId": 21, "name": "David", "lastName": "Arias Montes", "age": 47,
            "phoneNumber": "8493331234", "cedula": "04799112235"
        },
        {
            "userId": 22, "name": "Raquel", "lastName": "Herrera Vega", "age": 23,
            "phoneNumber": "8092225678", "cedula": "40233221108"
        },
        {
            "userId": 23, "name": "Antonio", "lastName": "Luna Ríos", "age": 50,
            "phoneNumber": "8291119012", "cedula": "00166554431"
        },
        {
            "userId": 24, "name": "Beatriz", "lastName": "Carmona Mora", "age": 34,
            "phoneNumber": "8499993456", "cedula": "01288779904"
        },
        {
            "userId": 25, "name": "Fernando", "lastName": "Vicente Cruz", "age": 44,
            "phoneNumber": "8098887890", "cedula": "00122446687"
        }
    ]

    try:
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

