
clients = 'Jose, Carlos'


def add_clients(client_name):
    global clients
    if client_name not in clients:
        clients += f', {client_name}'
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


def delete_client():
    pass


def list_clients():
    global clients
    print(clients)


def menu():
    print('WELCOME TO THE CUSTOMER CRUD')
    print('*' * 50)
    print("[C]reate a new cliente")
    print("[U]pdate client name")
    print("[D]elete a client")

    option = input(str('Choose an option: '))
    option = option.upper()

    if option == 'C':
        client_name = input('Add name client: ')
        add_clients(client_name)
    elif option == 'U':
        update_client()
        list_clients()


if __name__ == '__main__':
    menu()
    list_clients()