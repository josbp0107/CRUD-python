import csv
import os
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
    
    def update_client(self, updated_client):
        clients = self.list_clients()
        updated_clients = []

        for client in clients:
            if client['uid'] == updated_client.uid:
                updated_clients.append(updated_client.to_dict())
            else:
                updated_clients.append(client)

        self._save_to_disk(updated_clients)

    def _save_to_disk(clients):
        tmp_table_name = self.table_name + '.tmp'
        with open(tmp_table_name) as f:
            writer = csv.DictWriter(f, fieldnames= Client.schema())
            writerow.writerows(clients)
        
        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)