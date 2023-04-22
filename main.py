import tkinter as tk 
from PIL import ImageTk
from dbcon import DBCon

root = tk.Tk()
#run app

root.title("Fleet management system")


#placing the window in the center of the screen
x = (root.winfo_screenwidth() // 2) 
y = int(root.winfo_screenheight() * 0.1)

bg_color = "#6B6E77"

def load_frame2():
    #load thevehicle list
    frame2 = tk.Frame(root, width=1800, height=1800, bg=bg_color)
    frame2.grid_propagate(False)
    frame2.grid(row=0, column=0, sticky="nsew")
    tk.Button(frame2, text="Go back", bg="#D74B1B", fg="white", font=("Tkmenu", 16), activebackground="#ED8B01", command=lambda:load_frame1()).pack()

    conn_str = ('DRIVER={SQL Server};'
            'SERVER=DESKTOP-HH6PBH8;'
            'DATABASE=fleet_mng_vehicles;'
            'uid=sa;'
            'pwd=hubbabubba2020;'
            'Trusted_Connection=yes;'
           )
    db = DBCon(conn_str)
    vehicles = db.execute("SELECT * FROM [fleet_mng_vehicles].[dbo].[vehicle]")
    vehicle_str = ""
    for vehicle in vehicles:
            vehicle_str += "\nVehicle ID:{}\nMake:{}\nYear:{}\nKm-run:{}\nFuel:{}\nNext-Service:{}\nNext-service-prediction:{}".format(
                vehicle[0],
                vehicle[1],
                vehicle[2], 
                vehicle[3],
                vehicle[4],
                vehicle[5],
                vehicle[6],)

    vehicle_text = tk.Text(frame2, bg=bg_color, fg="white", font=("Tkmenu", 16))
    vehicle_text.insert(tk.END, vehicle_str)
    vehicle_text.pack()

#loading frame 3 with drivers
def load_frame3():
    #load thevehicle list
    frame3 = tk.Frame(root, width=1800, height=1800, bg=bg_color)
    frame3.grid_propagate(False)
    frame3.grid(row=0, column=0, sticky="nsew")
    tk.Button(frame3, text="Go back", bg="#D74B1B", fg="white", font=("Tkmenu", 16), activebackground="#ED8B01", command=lambda:load_frame1()).pack()

    conn_str = ('DRIVER={SQL Server};'
            'SERVER=DESKTOP-HH6PBH8;'
            'DATABASE=fleet_mng_vehicles;'
            'uid=sa;'
            'pwd=hubbabubba2020;'
            'Trusted_Connection=yes;'
           )
    db = DBCon(conn_str)
    drivers = db.execute("SELECT * FROM [fleet_mng_vehicles].[dbo].[drivers]")
    drivers_str= ""
    for driver in drivers:
            drivers_str+= "\nDriver ID:{}\nName:{}\nDate of ecpirience:{}\nYear:{}\nKm driven:{}".format(
                driver[0],
                driver[1],
                driver[2], 
                driver[3],
                driver[4],)

    driver_text = tk.Text(frame3, bg=bg_color, fg="white", font=("Tkmenu", 16))
    driver_text.insert(tk.END, drivers_str)
    driver_text.pack()
    # db= DBCon(conn_str)
    # vehicle_list = db.execute("SELECT * FROM [fleet_mng_vehicles].[dbo].[vehicle]")

    # tk.Label(frame2, text=vehicle_list, bg=bg_color, fg="white", font=("Tkmenu", 16)).pack()
    

def load_frame1():
    frame1 = tk.Frame(root, width=1800, height=1800, bg=bg_color)
    frame1.grid_propagate(False)
    frame1.grid(row=0, column=0, sticky="nsew")

    logo_img = ImageTk.PhotoImage(file="images/fleema_logo.png")
    logo_widget = tk.Label(frame1, image =logo_img)
    logo_widget.image_names = logo_img
    logo_widget.pack()

    tk.Label(frame1, text="Fleet management system", bg=bg_color, fg="white", font=("Tkmenu", 16)).pack()
    tk.Button(frame1, text="Vehicle list", bg="#D74B1B", fg="white", font=("Tkmenu", 16), activebackground="#ED8B01", command=lambda:load_frame2()).pack()
    tk.Button(frame1, text="Drivers list", bg="#D74B1B", fg="white", font=("Tkmenu", 16), activebackground="#ED8B01", command=lambda:load_frame3()).pack()

load_frame1()
root.mainloop()