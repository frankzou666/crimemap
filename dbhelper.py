

import pymysql

class DBHelper:
     def __init__(self,db_host,db_port,db_user,db_password,db_name):
         self.db_host =db_host
         self.db_port = db_port
         self.db_user = db_user
         self.db_password = db_password
         self.db_name = db_name

     def connect(self):

       return pymysql.connect(host=self.db_host,port=self.db_port,
                 user=self.db_user,
                 passwd=self.db_password,
                 db=self.db_name)

     def get_all_inputs(self):
       connection = self.connect()
       try:
         query = "SELECT description FROM crimes;"
         with connection.cursor() as cursor:
           cursor.execute(query)
         return cursor.fetchall()
       finally:
         connection.close()

     def add_input(self, data):
       connection = self.connect()
       try:
         # The following introduces a deliberate security flaw.
         query = "INSERT INTO crimes (description) VALUES ('{}');".format(data)
         with connection.cursor() as cursor:
           cursor.execute(query)
           connection.commit()
       finally:
         connection.close()

     def clear_all(self):
       connection = self.connect()
       try:
         query = "DELETE FROM crimes;"
         with connection.cursor() as cursor:
           cursor.execute(query)
           connection.commit()
       finally:
         connection.close()