
# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this: CMD

```
% .venv\Scripts\activate.bat
```

If you are a Windows platform, you would activate the virtualenv like this: PowerShell

```
% .venv\Scripts\Activate.ps1
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

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
$ cdk deploy --require-approval never
```

# 5. Eliminar el stack
```
$ cdk destroy
```

To add additional dependencies, for example other CDK libraries, just add
them to your `requirements.txt` file and rerun the `python -m pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
