from database.dbcon import dbconnection
#import drivers from the database

dbconnection()
class Driver: #class for the driver
    def __init__(self, driver_id, name, dob, expirience, km):
        super().__init__()
        self.c.execute("SELECT * FROM driver")
        self.drivers = self.c.fetchall()
        self.id = driver_id
        self.name = name
        self.dob = dob
        self.expirience = expirience
        self.km = km
        self.c.close()

    def __del__(self):
        self.conn.close()

    def get_drivers(self):
        return self.drivers

    def get_driver(self, driver_id):
        for driver in self.drivers:
            if driver[0] == driver_id:
                return driver

    def add_driver(self, driver):
        self.c.execute("INSERT INTO driver VALUES (?,?,?,?,?,?,?,?,?)", driver)