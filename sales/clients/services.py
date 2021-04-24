import csv
from clients.models import Client


class ClientService:
    def __init__(self, table_name):
        self.table_name = table_name
    
    def create_client(self, client):
        with open(self.table_name, 'a', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(client.to_dict())
