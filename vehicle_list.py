from dbcon import DBCon

#import list of the vehicles from the database
class VehicleList(connect):
    def __init__(self):
        super().__init__()
        self.execute("SELECT * FROM [fleet_mng_vehicles].[dbo].[vehicle]")
        self.vehicles = self.fetchall()
        self.c.close()

    def __del__(self):
        self.conn.close()

    def get_vehicles(self):
        return self.vehicles

    def get_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle[0] == vehicle_id:
                return vehicle

    def add_vehicle(self, vehicle):
        self.c.execute("INSERT INTO vehicle VALUES (?,?,?,?,?,?,?,?,?)", vehicle)