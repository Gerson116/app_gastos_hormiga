import json

from app_gastos_hormigas.constants.constants import MethodHttp
from app_gastos_hormigas.src.code.users.method.search_user_by_general_data import search_user_by_general_data
from app_gastos_hormigas.src.code.users.method.create_user import create_user
from app_gastos_hormigas.src.code.users.method.search_user_by_id import search_user_by_id
from app_gastos_hormigas.src.code.users.method.update_user import update_user
from app_gastos_hormigas.src.code.users.method.delete_user import delete_user

SEARCH_USER_BY_GENERAL_DATA = '/user/search-user'
SEARCH_USER_BY_ID = '/user/{userId}'
CREATE_USER = '/user/add'
UPDATE_USER = '/user/update'
DELETE_USER = '/user/delete/{userId}'

ROUTES = {
    (MethodHttp.GET, SEARCH_USER_BY_GENERAL_DATA): search_user_by_general_data,
    (MethodHttp.GET, SEARCH_USER_BY_ID): search_user_by_id,
    (MethodHttp.POST, CREATE_USER): create_user,
    (MethodHttp.PATCH, UPDATE_USER): update_user,
    (MethodHttp.DELETE, DELETE_USER): delete_user
}


def lambda_handler(event, _):
    print(f'event -> {json.dumps(event, default=str)}')

    method = event['httpMethod']
    resource = event['resource']
    # todo: esta variable debo buscar la manera de que sea enviada desde github action al momento de desplegar los
    #   ambientes dev, cert y prod
    env = 'dev'
    handler = ROUTES.get((method, resource))

    if handler:
        return handler(event=event, env=env)

    return {
        "statusCode": 400,
        "body": "ummmmmm ocurrio un error.!"
    }
