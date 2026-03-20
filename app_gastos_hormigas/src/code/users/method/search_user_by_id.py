from app_gastos_hormigas.src.shared.response_template import ResponseTemplate
import json


def search_user_by_id(event):
    # TODO: POR EL MOMENTO VOY A RETORNAR DATOS DE PRUEBA.
    data = [
        {
            "userId": 1, "name": "Gerson", "lastName": "Santos Mateo", "age": 28,
            "phoneNumber": "8095551234", "identification": "40223456781"
        },
        {
            "userId": 2, "name": "Ana", "lastName": "García Pérez", "age": 32,
            "phoneNumber": "8294445678", "identification": "00198765432"
        },
        {
            "userId": 3, "name": "Carlos", "lastName": "López Rodríguez", "age": 45,
            "phoneNumber": "8493339012", "identification": "03111223345"
        },
        {
            "userId": 4, "name": "María", "lastName": "Martínez Gómez", "age": 25,
            "phoneNumber": "8092223456", "identification": "40255667789"
        },
        {
            "userId": 5, "name": "Juan", "lastName": "Fernández Ruiz", "age": 38,
            "phoneNumber": "8291117890", "identification": "04799887764"
        },
        {
            "userId": 6, "name": "Laura", "lastName": "Díaz Sánchez", "age": 29,
            "phoneNumber": "8499991234", "identification": "22344556670"
        },
        {
            "userId": 7, "name": "Pedro", "lastName": "Moreno Álvarez", "age": 51,
            "phoneNumber": "8098885678", "identification": "00133445567"
        },
        {
            "userId": 8, "name": "Sofía", "lastName": "Romero Alonso", "age": 22,
            "phoneNumber": "8297779012", "identification": "40288990012"
        },
        {
            "userId": 9, "name": "Luis", "lastName": "Gutiérrez Navarro", "age": 41,
            "phoneNumber": "8496663456", "identification": "01255661123"
        },
        {
            "userId": 10, "name": "Carmen", "lastName": "Torres Domínguez", "age": 36,
            "phoneNumber": "8095557890", "identification": "00122334456"
        },
        {
            "userId": 11, "name": "Jorge", "lastName": "Vázquez Ramos", "age": 48,
            "phoneNumber": "8294441234", "identification": "05466778890"
        },
        {
            "userId": 12, "name": "Elena", "lastName": "Gil Blanco", "age": 27,
            "phoneNumber": "8493335678", "identification": "40211229984"
        },
        {
            "userId": 13, "name": "Diego", "lastName": "Ramírez Castro", "age": 33,
            "phoneNumber": "8092229012", "identification": "00177889901"
        },
        {
            "userId": 14, "name": "Lucía", "lastName": "Molina Ortiz", "age": 24,
            "phoneNumber": "8291113456", "identification": "40233445568"
        },
        {
            "userId": 15, "name": "Miguel", "lastName": "Delgado Silva", "age": 55,
            "phoneNumber": "8499997890", "identification": "06599001125"
        },
        {
            "userId": 16, "name": "Paula", "lastName": "Castro Núñez", "age": 30,
            "phoneNumber": "8098881234", "identification": "00155443326"
        },
        {
            "userId": 17, "name": "Javier", "lastName": "Iglesias Medina", "age": 42,
            "phoneNumber": "8297775678", "identification": "03188776659"
        },
        {
            "userId": 18, "name": "Marta", "lastName": "Garrido Rojas", "age": 26,
            "phoneNumber": "8496669012", "identification": "40211998873"
        },
        {
            "userId": 19, "name": "Alejandro", "lastName": "Cortés Peña", "age": 39,
            "phoneNumber": "8095553456", "identification": "00122883340"
        },
        {
            "userId": 20, "name": "Sara", "lastName": "Flores Cabrera", "age": 31,
            "phoneNumber": "8294447890", "identification": "40255446672"
        },
        {
            "userId": 21, "name": "David", "lastName": "Arias Montes", "age": 47,
            "phoneNumber": "8493331234", "identification": "04799112235"
        },
        {
            "userId": 22, "name": "Raquel", "lastName": "Herrera Vega", "age": 23,
            "phoneNumber": "8092225678", "identification": "40233221108"
        },
        {
            "userId": 23, "name": "Antonio", "lastName": "Luna Ríos", "age": 50,
            "phoneNumber": "8291119012", "identification": "00166554431"
        },
        {
            "userId": 24, "name": "Beatriz", "lastName": "Carmona Mora", "age": 34,
            "phoneNumber": "8499993456", "identification": "01288779904"
        },
        {
            "userId": 25, "name": "Fernando", "lastName": "Vicente Cruz", "age": 44,
            "phoneNumber": "8098887890", "identification": "00122446687"
        }
    ]

    try:
        path_params = event.get("pathParameters")

        user_id: str = path_params.get("userId")

        # TODO: ELIMINAR ESTE BLOQUE DE CODIGO.

        obj_user = next((item for item in data if item["userId"] == int(user_id)), None)

        if obj_user is None:
            return ResponseTemplate.not_found("Usuario no encontrado")

        return ResponseTemplate.data_response(obj_user)

    except Exception as e:
        print(e)
        return ResponseTemplate.error_response(str(e))
    finally:
        print('Finalizo el proceso')

