import pandas as pd
import numpy as np
from joblib import load

from dbcon import DBCon

model_saved = load('predictive_maintenence_model.h5')

def vehicle_data(vehicle_id):
    conn_str = ('DRIVER={SQL Server};'
            'SERVER=DESKTOP-HH6PBH8;'
            'DATABASE=fleet_mng_vehicles;'
            'uid=sa;'
            'pwd=hubbabubba2020;'
            'Trusted_Connection=yes;'
           )
    db = DBCon(conn_str)
    vehicle = db.execute("SELECT * FROM [fleet_mng_vehicles].[dbo].[vehicle] WHERE vehicle_id = {}".format(vehicle_id))
    vehicle_str = ""
    for vehicle in vehicles:
            vehicle_str += "\nVehicle ID:{}\nMake:{}\nYear:{}\nKm-run:{}\nFuel:{}\nService-Interval:{}\nNext-service-prediction:{}".format(
                vehicle[0],
                vehicle[1],
                vehicle[2], 
                vehicle[3],
                vehicle[4],
                vehicle[5],
                vehicle[6],)
    return(vehicle_str[5])

regular_interval = vehicle_data(vehicle_id)

def maintenence_prediction(regular_interval, prediction_coef)
    regular_interval = ''
    prediction_coef = model_saved.predict(np.array([regular_interval]))[0]
    return(regular_interval * prediction_coef)
