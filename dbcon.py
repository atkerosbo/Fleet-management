import pyodbc as odbc


class DBCon:
    def __init__(self, conn_str):
        self.conn = odbc.connect(conn_str)
        self.cursor = self.conn.cursor()
    
    def execute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

conn_str = ('DRIVER={SQL Server};'
            'SERVER=DESKTOP-HH6PBH8;'
            'DATABASE=fleet_mng_vehicles;'
            'uid=sa;'
            'pwd=hubbabubba2020;'
            'Trusted_Connection=yes;'
           )

# db = DBCon(conn_str)
# result = db.execute("SELECT * FROM [fleet_mng_vehicles].[dbo].[drivers]")
# print(result)

# #connect the server
# conn_str = ('DRIVER={SQL Server};'
#             'SERVER=DESKTOP-HH6PBH8;'
#             'DATABASE=fleet_mng_vehicles;'
#             'uid=sa;'
#             'pwd=hubbabubba2020;'
#             'Trusted_Connection=yes;'
#                     )
# conn = odbc.connect(conn_str)



# mycursor = conn.cursor()

# mycursor.execute("""
#                SELECT * FROM [fleet_mng_vehicles].[dbo].[vehicle]
#                """)

# rows = mycursor.fetchall()

# for row in rows:
#     print(row)

