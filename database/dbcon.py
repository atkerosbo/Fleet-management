#conecting to the local database
import pypyodbc as pyodbc

#connect the server
class dbconnection:
    def __init__(self):
        self.server = 'DESKTOP-HH6PBH8'
        self.database = 'fleet_mng_vehicles'
        self.username = 'fleetmng'
        self.password = 'hubbabubba2020'
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.conn.cursor()






#server name DESKTOP-HH6PBH8
#database name fleet_mng_vehicles