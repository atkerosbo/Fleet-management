import tkinter as tk 
from PIL import ImageTk
from vehicle_list import VehicleList

root = tk.Tk()
#run app

root.title("Fleet management system")


#placing the window in the center of the screen
x = (root.winfo_screenwidth() // 2) 
y = int(root.winfo_screenheight() * 0.1)

bg_color = "#6B6E77"

def load_frame2():
    #load thevehicle list
    frame2 = tk.Frame(root, width=800, height=800, bg=bg_color)
    frame2.grid_propagate(False)
    frame2.grid(row=0, column=0, sticky="nsew")

    for vehicle_id in VehicleList:
        tk.Label(frame2, text=vehicle_id, bg=bg_color, fg="white", font=("Tkmenu", 16)).pack()
    
    tk.Button(frame2, text="Go back", bg="#D74B1B", fg="white", font=("Tkmenu", 16), activebackground="#ED8B01", command=lambda:load_frame1()).pack()

def load_frame1():
    frame1 = tk.Frame(root, width=800, height=800, bg=bg_color)
    frame1.grid_propagate(False)
    frame1.grid(row=0, column=0, sticky="nsew")

    logo_img = ImageTk.PhotoImage(file="images/fleema_logo.png")
    logo_widget = tk.Label(frame1, image =logo_img)
    logo_widget.image_names = logo_img
    logo_widget.pack()

    tk.Label(frame1, text="Fleet management system", bg=bg_color, fg="white", font=("Tkmenu", 16)).pack()
    tk.Button(frame1, text="Let's Go!", bg="#D74B1B", fg="white", font=("Tkmenu", 16), activebackground="#ED8B01", command=lambda:load_frame2()).pack()

load_frame1()
root.mainloop()