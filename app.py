#!/usr/bin/env python3

from app_gastos_hormigas.lib.gastos_hormigas_dynamo_stack import GastosHormigasDynamoStack
import os

import aws_cdk as cdk

from app_gastos_hormigas.lib.gastos_hormigas_lambda_stack import GastosHormigasLambdaStack
from app_gastos_hormigas.constants.constants import Environment, AccountEnvironment, full_project_name

app = cdk.App()

# 1. Obtener la variable de entorno, por defecto 'dev'
env = app.node.try_get_context("env") or "dev"

# 2. Validar que sea un entorno permitido
if env not in [Environment.DEV, Environment.CERT, Environment.PROD]:
    raise ValueError(f"Entorno no válido: {env}. Debe ser dev, cert o prod.")

# 3. Definir nombre del ambiente segun lo que se invoque.

if env not in [Environment.DEV, Environment.CERT]:
    account_env = AccountEnvironment.PROD
else:
    account_env = AccountEnvironment.NO_PROD

full_name = full_project_name(account_env)

dynamo_stack = GastosHormigasDynamoStack(app, f"{full_name}-dynamo", env=env)

GastosHormigasLambdaStack(app, f"{full_name}-lambda", env=env, dynamo_tables=dynamo_stack.tables)

app.synth()
