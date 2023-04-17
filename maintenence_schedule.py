import get_vehicle_list from .get_vehicle_list

#Highlight and display the vehicle that needs mainenece

def get_vehicle_list():
    vehicle_list = []
    for vehicle in vehicles:
        vehicle_list.append(vehicle[0])
    return vehicle_list

def get_vehicle(vehicle_id):
    for vehicle in vehicles:
        if vehicle[0] == vehicle_id:
            return vehicle
        
def get_vehicle_km(vehicle_id):
    for vehicle in vehicles:
        if vehicle[0] == vehicle_id:
            return vehicle[3]