import sys

clients = 'Luis, Jose, Carlos'


def _get_name_client():
    client_name = None

    while not client_name:

        client_name = input('What is the client name? ').capitalize()
        # Rompe el ciclo cuando se ingresa la palabra exit por consola
        if client_name == 'Exit':
            client_name = None
            break
    # Si se agrego la palabra exit termina el programa.
    if not client_name:
        sys.exit()

    return client_name


def add_clients(client_name):
    global clients
    if client_name not in clients:
        clients += f', {client_name}'
        list_clients()
    else:
        print('The name is already')


def update_client():
    global clients

    client_name = input("What is the client name to change? ").capitalize()
    update_name = input(f"New name of {client_name} is: ").capitalize()

    if client_name in clients:
        clients = clients.replace(client_name, update_name)
    else:
        return print(f'{client_name} is not in client list')


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
        list_clients()
    else:
        print('Client is not in Clients list')


def search_client(client_name):
    #global clients
    client_list = clients.split(', ')  # Nos permite generar un separador

    for client in client_list:
        if client != client_name:
            continue
        else:
            return True


def list_clients():
    global clients
    print(clients)


def menu():
    print('WELCOME TO THE CUSTOMER CRUD')
    print('*' * 50)
    print("[C]reate a new cliente")
    print("[R]ead list clients")
    print("[U]pdate client name")
    print("[D]elete a client")
    print("[S]earch a client")

    option = input(str('Choose an option: '))
    option = option.upper()

    if option == 'C':
        client_name = _get_name_client()
        add_clients(client_name)
    elif option == 'R':
        list_clients()
    elif option == 'U':
        update_client()
        list_clients()
    elif option == 'D':
        client_name = _get_name_client()
        delete_client(client_name)
    elif option == 'S':
        client_name = _get_name_client()
        found = search_client(client_name)

        if found:
            print(f'The client {client_name} is in client list')
        else:
            print(f"{client_name} is not in client list")


if __name__ == '__main__':
    menu()
    list_clients()