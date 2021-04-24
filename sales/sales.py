import click

from clients import commands as clients_commands

# Recordar:
# para poder crear el proyecto y ejecutar por cli es importante seguir los siguientes pasos:
# Cuando se tenga el archivo setup.py configurado correctamente, se procede a ejecutar el siguiente comando:
# pip install --editable . -> esto toma en la carpeta que nos encontramos.
# y para ver si funciona correctamente procedemos a verificar con el comando sales --help´
# todos los comandos que se pueden ejecutar
# sales llevar por nombre el cli que se configuró en el archivo setup, esto varia
CLIENT_TABLE = '.clients.csv'

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj['clients_table'] = CLIENT_TABLE

cli.add_command(clients_commands.all)