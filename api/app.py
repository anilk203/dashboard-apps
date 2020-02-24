from flask import Flask
from collections import OrderedDict 
from flask import jsonify 
from flask import request
import logging
import pymysql 
import pymysql.cursors 
app = Flask(__name__)


class DatabaseConnection:
    def __init__(self):
        pass
    
    def get_database_connection(self):
        try:
            con = pymysql.connect(host='mysqldb',
            user='root',
            password='mysql',
            db='configuration_database',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
            
            return con
        except:
            return None
        
 
    
class DatabaseConfigurationRepository:
    def __init__(self):
        pass
    
    def save(self, data): 
        dc  =  None 
        try: 
            dc  =  DatabaseConnection()
            con = dc.get_database_connection()
            
            if con != None: 
                od = [] 
                with con: 
                    cur = con.cursor()
                    sql = "insert into database_configurations (name,value) values (%s,%s)" 
                    count = cur.execute(sql, (data['name'], data['value']))
                    con.commit()
                    
                return count
        
        except pymysql.InternalError as error:
            code, message = error.args 
            app.logger.error(code, message)
            return None
        
    def find(self, name):
        dc  =  None 
        obj = None
        try: 
            dc  =  DatabaseConnection()
            con = dc.get_database_connection()
            
            if con != None: 
                od = [] 
                with con: 
                    cur = con.cursor()
                    sql = "SELECT id, name, value FROM database_configurations where name =  (%s)"
                    cur.execute(sql, (name)) 
                    rows = cur.fetchall() 
                    
                    for row in rows: 
                        obj =  row
                        break
        
            return obj
        
        except pymysql.InternalError as error:
            code, message = error.args 
            app.logger.error(code, message)
            return None        
    
    def load(self, id):
        dc  =  None 
        obj = None
        try: 
            dc  =  DatabaseConnection()
            con = dc.get_database_connection()
            
            if con != None: 
                od = [] 
                with con: 
                    cur = con.cursor()
                    sql = "SELECT id, name, value FROM database_configurations where id =  (%s)"
                    cur.execute(sq, (id)) 
                    rows = cur.fetchall() 
                    
                    for row in rows: 
                        obj =  row
                        break
        
            return obj
        
        except pymysql.InternalError as error:
            code, message = error.args 
            app.logger.error(code, message)
            return None        

    def get(self):
        dc  =  None 
        
        try: 
            dc  =  DatabaseConnection()
            con = dc.get_database_connection()
            
            if con != None: 
                od = [] 
                with con: 
                    cur = con.cursor()
                    cur.execute("SELECT id, name, value FROM database_configurations") 
                    rows = cur.fetchall() 
                    
                    for row in rows: 
                        od_local = {
                            'id': row['id'],
                            'name': row['name'],
                            'value': row['value']
                        }
                        od.append(od_local)
        
                return od
        
        except:
            return None
                
      
    
    def delete(self, id):
        dc  =  None  
        try: 
            dc  =  DatabaseConnection()
            con = dc.get_database_connection()
            
            if con != None: 
                od = [] 
                with con: 
                    cur = con.cursor()
                    sql = "delete FROM database_configurations where id =  (%s)"
                    count = cur.execute(sql, (id)) 
                    return count
        
        except pymysql.InternalError as error:
            code, message = error.args 
            app.logger.error(code, message)
            return None         
    
    
@app.route("/status", methods=["GET"])
def status():  
  dcr = DatabaseConfigurationRepository()
  if dcr.get() == None:
      return jsonify({'message': 'Database Connectivity issues...'})
  else:
      return jsonify({'message': 'Connection to database is successful!'})
      
  
      
@app.route("/save_db_configurations", methods=["POST"])
def save_db_configurations():  
  dcr = DatabaseConfigurationRepository()
  data = request.get_json()   
  found_record = dcr.find(data['name']) 
  if found_record:
      return jsonify({'status': 'failed', 'message': 'Configuration name is already taken, No Duplicates are allowed'})  
  if dcr.save(data) == None:  
      return jsonify({'status': 'failed'})
  else:
      return jsonify({'status': 'success'})
  
@app.route("/delete_db_configurations/<id>", methods=["DELETE"])
def delete_db_configurations(id): 
  dcr = DatabaseConfigurationRepository()
  count = dcr.delete(id)
  if count <=0 :  
      return jsonify({'status': 'failed', 'id': id, 'message': 'Configuration is not found to delete!'})  
  else:
      return jsonify({'status': 'success', 'id': id, 'message': 'Configuration is deleted successfully!'})  
    
@app.route("/get_db_configurations", methods=["GET"])
def get_db_configurations():
  dcr = DatabaseConfigurationRepository()
  return jsonify( {"data": dcr.get()})

@app.route("/")
def root():
  dc = DatabaseConfigurations()
  dc.get_database_configurations()
  return "Api Service is UP!"
  
if __name__ == "__main__":
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)    
    app.run(debug=True)  
  