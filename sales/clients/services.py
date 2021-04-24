import csv
from clients.models import Client


class ClientService:
    def __init__(self, table_name):
        self.table_name = table_name
    
    def create_client(self, client):
        with open(self.table_name, 'a', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(client.to_dict())
    
    def list_clients(self):
        with open('../.clients.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, fieldnames=Client.schema())
            # reader al ser un iterable, es necesario convertirlo a una lista con la funcion global list
            return list(reader)
    