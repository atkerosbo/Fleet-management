import pyodbc as odbc

#connect the server
conn_str = (r'DRIVER={SQL Server};'
            r'SERVER=DESKTOP-HH6PBH8;'
            r'DATABASE=fleet_mng_vehicles;'
            r'Trusted_Connection=yes;'
                    )
conn = odbc.connect(conn_str)


#reading the data from the database

def read(conn,table):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM "+table+";")
    for row in cursor:
        print(f"row = {row}")


#create

def create(conn):
    print("Create")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO vehicle VALUES (?,?,?,?,?,?,?);", (3, "Mercedes", 2017, 120000, 2, 1, 1))
    conn.commit()
    read(conn)   


#update

def update(conn):
    print("Update")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO vehicle VALUES (?,?,?,?,?,?,?);", (4, "Iveco", 2019, 100000, 2000, 1000, 1))
    conn.commit()
    read(conn) 

#delete
def delete(conn):
    print("Delete")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM vehicle WHERE vehicle_id = 4")
    conn.commit()
    read(conn)  


read(conn,"vehicle")







#server name DESKTOP-HH6PBH8
#database name fleet_mng_vehicles