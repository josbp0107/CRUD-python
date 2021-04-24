import click

@click.group() # Convierte la funcion client en otro decorador
def clients():
    """ Manages the clients lifecycle"""

@clients.command()
@click.pass_context
def create(ctx, name, company, email, position):
    """Creates a new client"""

@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""

@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """Update a client"""

@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""

all = clients # all apunta a la funcion clients
