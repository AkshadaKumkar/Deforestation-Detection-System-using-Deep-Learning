from tkinter import *
import tkinter as tk
import Deforestation_Detection_init


def center_window(w,h):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
def read_input(): 
    
    forestofficername=textBox1.get()
    forest_officer_number=textBox2.get()
    
    print(forestofficername) 
    
    print(forest_officer_number)
    Deforestation_Detection_init.initDetection(forest_officer_number,forestofficername)
    


    

    
root=Tk()
root.configure(background='#6495ED')
root.title("DEFORESTATION DETECTION SYSTEM")
center_window(1400, 800)


username = Label(root,text = "DEFORESTATION DETECTION SYSTEM", font=("Courier", 30,'bold'),fg='#f00',bg='#6495ED').place(x = 250,y = 60)


# code to create label 
label1 = Label(root,text = "Forest Officer Name: ",bg='#6495ED',font=("Ariel", 10)).place(x = 350,y = 205)
label2 = Label(root, text = "Forest Office Mobile No. : ",bg='#6495ED',font=("Ariel", 10)).place(x = 350,y = 265)  
   


#code to insert textbox
textBox1 = tk.Entry(root, width = 40)
textBox1.place(x = 600,y = 200,height=30)
textBox2 = Entry(root, width =40)
textBox2.place(x = 600,y = 260,height=30)






#command=lambda: retrieve_input() >>> just means do this when i press the button
button=Button(root, height=1, width=13, font=("Ariel", 10,'bold'),text="Submit", command=lambda: read_input()).place(x=530,y=460)
# Button for closing
exit_button = Button(root, height=1, width=13, font=("Ariel", 10,'bold'),text="Exit", command=root.destroy).place(x=700,y=460)


mainloop()

