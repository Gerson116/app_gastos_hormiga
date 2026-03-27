
REGION_NAME = 'us-east-1'

class Environment:
    DEV = "dev"
    CERT = "cert"
    PROD = "prod"

class AccountEnvironment:
    NO_PROD = "no-prod"
    PROD = "prod"

class ProyectName:
    GASTOS_HORMIGAS = "gastos-hormigas"


def full_project_name(account_environment: str) -> str:
    return f"{ProyectName.GASTOS_HORMIGAS}-{account_environment}"

class MethodHttp:
    GET = "GET"
    POST = "POST"
    PATCH = "PATCH"
    DELETE = "DELETE"

class UserState:
    ACTIVE = 'AC'
    INACTIVE = 'IN'