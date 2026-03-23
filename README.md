# ¡Mi primer proyecto CDK con Python!

Este es un proyecto en blanco para el desarrollo de CDK con Python.

El archivo `cdk.json` le indica al CDK Toolkit cómo ejecutar tu aplicación.

Este proyecto está configurado como un proyecto estándar de Python. El proceso de inicialización también crea un entorno virtual dentro de este proyecto, almacenado en el directorio `.venv`. Para crear el entorno virtual, se asume que existe un ejecutable de `python3` (o `python` en Windows) en tu PATH con acceso al paquete `venv`. Si por alguna razón falla la creación automática del entorno virtual, puedes crearlo manualmente.

Para crear manualmente un entorno virtual en MacOS y Linux:

```
$ python -m venv .venv
```

Una vez que el proceso de inicialización termine y se cree el entorno virtual, puedes usar el siguiente comando para activarlo.

```
$ source .venv/bin/activate
```

Si estás en la plataforma Windows, activarías el entorno virtual de la siguiente manera en CMD:

```
% .venv\Scripts\activate.bat
```

Si estás en la plataforma Windows, activarías el entorno virtual de la siguiente manera en PowerShell:

```
% .venv\Scripts\Activate.ps1
```

Una vez que el entorno virtual esté activado, puedes instalar las dependencias requeridas.

```
$ pip install -r requirements.txt
```

En este punto, ya puedes sintetizar la plantilla de CloudFormation para este código.

# 1. Preparar el entorno (Solo la primera vez)
```
$ cdk bootstrap
```

# 2. Sintetizar el proyecto
```
$ cdk synth
```

# 3. Ver qué va a pasar (Opcional pero recomendado)
```
$ cdk diff
```

# 4. Desplegar aceptando cambios de seguridad automáticamente
```
$ cdk deploy

NOTA: Si se despliega más de un stack, se debe especificar el stack a desplegar o usar --all
$ cdk deploy --all
```

# 5. Eliminar el stack
```
$ cdk destroy

NOTA: Si se despliega más de un stack, se debe especificar el stack a eliminar o usar --all
$ cdk destroy --all
```

# 6. Observación
En caso de usted haber borrado el bucket manualmente, deberá realizar los siguientes pasos:

1. Eliminar el stack `aws cloudformation delete-stack --stack-name CDKToolkit`
2. Ejecutar el comando `cdk bootstrap`
3. Ejecutar el comando `cdk deploy`

Para agregar dependencias adicionales, por ejemplo, otras bibliotecas de CDK, simplemente agrégalas a tu archivo `requirements.txt` y vuelve a ejecutar el comando `python -m pip install -r requirements.txt`.

## Comandos útiles

 * `cdk ls`          lista todos los stacks en la aplicación
 * `cdk synth`       emite la plantilla sintetizada de CloudFormation
 * `cdk deploy`      despliega este stack a tu cuenta/región de AWS por defecto
 * `cdk diff`        compara el stack desplegado con el estado actual
 * `cdk docs`        abre la documentación de CDK

¡Disfrútalo!
