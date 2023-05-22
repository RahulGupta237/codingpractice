"""
In general if an abstract class contain only abstract methods 
such type of abstract class is consider as Interface
"""
from abc import *
class DBInterface(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass
class Oracle(DBInterface):
    def connect(self):
        print("Connect To Oracle Data base")
    def disconnect(self):
        print("Disconnect to Oracle data base")

class Mysql(DBInterface):
    def connect(self):
        print("Connect To MYSQL Data base")
    def disconnect(self):
        print("Disconnect to MYSQL data base")

class Mongo(DBInterface):
    def connect(self):
        print("Connect To Mongo Data base")
    def disconnect(self):
        print("Disconnect to Mongo data base")

dbname=input("Enter Database Name:")
classname=globals()[dbname]
x=classname()
x.connect()
x.disconnect()
