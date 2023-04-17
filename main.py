import tkinter as tk 
from PIL import ImageTk


root = tk.Tk()
#run app

root.title("Fleet management system")
#placing the window in the center of the screen
x = (root.winfo_screenwidth() // 2) 
y = int(root.winfo_screenheight() * 0.1)

#root.geometry('800x600' + str(x) + '+' + str(y) )


frame1 = tk.Frame(root, width=500, height=500, bg="#6B6E77")
frame1.grid(row=0, column=0, sticky="nsew")

logo_img = ImageTk.PhotoImage(file="images/fleema_logo.png")
logo_widget = tk.Label(frame1, image =logo_img)
logo_widget.image_names = logo_img


root.mainloop()
