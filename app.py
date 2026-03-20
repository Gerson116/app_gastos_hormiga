#!/usr/bin/env python3

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

GastosHormigasLambdaStack(app, full_name, env=env,
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

app.synth()
