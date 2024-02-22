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
            timeout = 30
            socket.setdefaulttimeout(timeout)

            common = xmlrpc.client.ServerProxy("{}/xmlrpc/2/common".format(self.url))
            self.models = xmlrpc.client.ServerProxy("{}/xmlrpc/2/object".format(self.url))

            self.uid = common.authenticate(self.db, self.username, self.password, {})
            print(f"Connected to the database: {self.db}")
        
        except socket.timeout:
            print(f"Connection timed out for: {self.db}")
            
        except Exception as e:
            print(f"Error connecting to the database: {self.db}")
            print(e)

    def search_record(self, model, domain):
        try:
            record_id = self.models.execute_kw(self.db, self.uid, self.password, model, 'search',[domain])
            if record_id:
                print(f"{self.db}: Record found with the ID: {record_id}")
                return record_id
            else:
                print("The record was not found")
                return False
            
        except Exception as e:
            print(e)
            return False
        
    def update_record(self, model, record_id, values):
        try:
            update = self.models.execute_kw(self.db, self.uid, self.password, model, 'write',[record_id, values])
            if update:
                print(f"{self.db}: The record with id {record_id} has been updated.")
            else:
                print(f"The record {record_id} was not updated")
        except Exception as e:
            print(e)
            return False
        
    def create_record(self, model, values):
        try:
            record_id = self.models.execute_kw(self.db, self.uid, self.password, model, 'create',[values])
            print(f"{self.db}: The record with id {record_id} has been created.")
            return record_id
        except Exception as e:
            print(e)
            return False

    def execute_model_method(self, model, method, id, *args, **kwargs):
        try:
            result = self.models.execute_kw(self.db, self.uid, self.password, model, method, [int(id)] + list(args), kwargs)
            print(f"{self.db}: The method {method} has been executed.")
            return result
        except Exception as e:
            print(f"An error occurred while executing method {method} on model {model}: {e}")
            return False
        

    def read_record(self, model, record_id):
        try:
            record = self.models.execute_kw(self.db, self.uid, self.password, model, 'read',[record_id])
            print(f"{self.db}: The record with id {record_id} has been read.")
            return record
        except Exception as e:
            print(e)
            return False
