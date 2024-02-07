import datetime
import socket
import xmlrpc.client

class OdooActions:
    def __init__(self,url,db,username,password):

        self.url = url
        self.db = db
        self.username = username
        self.password = password
        self.connect()

    def connect(self):
        try:
            timeout = 10
            socket.setdefaulttimeout(timeout)

            common = xmlrpc.client.ServerProxy("{}/xmlrpc/2/common".format(self.url))
            self.models = xmlrpc.client.ServerProxy("{}/xmlrpc/2/object".format(self.url))

            self.uid = common.authenticate(self.db, self.username, self.password, {})
            print(f"Conectado a la base de datos {self.db}")
        
        except socket.timeout:
            print(f"Error al conectarse a la base de datos {self.db}")
            
        except Exception as e:
            print(f"Error al conectarse a la base de datos {self.db}")
            print(e)

    def search_record(self, model, domain):
        try:
            record_id = self.models.execute_kw(self.db, self.uid, self.password, model, 'search',[domain])
            if record_id:
                print(f"{self.db} Se encontró el registro con id {record_id}")
                return record_id
            else:
                print("No se encontró el registro")
                return False
            
        except Exception as e:
            print(e)
            return False
        
    def update_record(self, model, record_id, values):
        try:
            update = self.models.execute_kw(self.db, self.uid, self.password, model, 'write',[record_id, values])
            if update:
                print(f"{self.db} Se actualizó el registro con id {record_id}")
            else:
                print("No se actualizó el registro")
        except Exception as e:
            print(e)
            return False
        
    def create_record(self, model, values):
        try:
            record_id = self.models.execute_kw(self.db, self.uid, self.password, model, 'create',[values])
            print(f"{self.db} Se creó el registro con id {record_id}")
            return record_id
        except Exception as e:
            print(e)
            return False
