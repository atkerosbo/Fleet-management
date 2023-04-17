import dbcon from .database.dbcon
#import drivers from the database
class DriverList(dbcon):
    def __init__(self):
        super().__init__()
        self.c.execute("SELECT * FROM driver")
        self.drivers = self.c.fetchall()
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