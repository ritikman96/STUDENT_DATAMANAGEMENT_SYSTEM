#frontend using python default interface function tkinter

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import main
 
 
 #MAIN BODY
 # window name is root
root=tk.Tk() # create main function window
root.title("STUDENT MANGEMENT SYSTEM")
root.geometry("1200x700")
root.resizable(False,False)


#BACKGROUND IMAGE
image=Image.open("background.jpg") #tells to open background image
image=image.resize((1200,700)) #resizing according to window

background_image = ImageTk.PhotoImage(image)

background = tk.Label(
    root,
    image=background_image
)

background.place(
    x=0, y=0,
    relwidth=1, relheight=1
)

#GUI Function which will clear interface after adding data
def clear_fields():
    
    id_entry.delete(0,tk.END)
    name_entry.delete(0,tk.END)
    age_entry.delete(0,tk.END)
    course_entry.delete(0,tk.END)
    marks_entry.delete(0,tk.END)
    
    
#Refresh table
def refresh_table():
    for row in table.get_children():  #imp function  to list of all data in tkinter
        table.delete(row)
        
    for index, student in  main.df.iterrows():
            
        table.insert(
            "",
            "end",
            values=(
                student["ID"],
                student["NAME"],
                student["AGE"],
                student["COURSE"],
                student["MARKS"]
                    
            )
        )
            
#Adding GUI fucntion to retrive data from main
def add_student_gui():
   
    try:
        sid=int(id_entry.get())
        name=name_entry.get()
        age=int(age_entry.get())
        course=course_entry.get()
        marks=int(marks_entry.get())
        
        sucess, message=main.add_student(
            sid,
            name,
            age,
            course,
            marks
            
        )
        if sucess:
            
            messagebox.showinfo(
                "sucess",
                message
            )
            
            clear_fields()
            refresh_table()
        else:
            messagebox.showerror(
                "ERROR",
                message
            )       
            
    except ValueError:
        messagebox.showerror(
        "INVALID INPUT",
        "ID, AGE and MARKS must be number"
        )
        

#now adding frames 
header= tk.Frame(
    root,
    bg="#163A63"
    )

header.place(
    x=0,
    y=0,
    width=1200,
    height=80
)

#adding the title

title=tk.Label(
    header,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Arial",24,"bold"),
    bg="blue",
    fg="green"
)

title.pack(    # this function is used to add  title inside the header
    pady=20
)

#Creating the form
form_frame=tk.Frame(
    root,
    bg="white"
)

form_frame.place(
    x=300,
    y=120,
    width=600,
    height=350
)

#creating label student Id
tk.Label(
    form_frame,
    text="STUDENT ID",
    font=("Arial",12,"bold"),
    bg="white",
).grid(   #this is the function which creates '______'  
        row=0,
        column=0,
        padx=20,  #adds horizontal space,
        pady=15  #add vertical space,
)

id_entry=tk.Entry(  #this is the text box
    form_frame,
    font=("Arial",12)
)

#putting this entry box in grid 
id_entry.grid(
    column=1,
    row=0,
    padx=20,
    pady=15
)
#Name field
tk.Label(
    form_frame,
    text="NAME",
    font=("Arial",12,"bold"),
    bg="white"
).grid(
    column=0,
    row=1,
    pady=15,
    padx=20
)

name_entry=tk.Entry(
    form_frame,
    font=("Arial",12)
)
name_entry.grid(
    row=1,
    column=1,
    padx=20,
    pady=15
    )

#AGE
tk.Label(
    form_frame,
    text="AGE",
    font=("Arial",12,"bold"),
    bg="white"
).grid(
    column=0,
    row=2,
    padx=20,
    pady=15
)
age_entry=tk.Entry(
    form_frame,
    font=("Arial",12)
)
age_entry.grid(
    row=2,
    column=1,
    padx=20,
    pady=15
    
)
tk.Label(
    form_frame,
    text="Course",
    font=("Arial", 12, "bold"),
    bg="white"
).grid(row=3, column=0, padx=20, pady=15)

course_entry = tk.Entry(
    form_frame,
    font=("Arial", 12)
)

course_entry.grid(
    row=3,
    column=1,
    padx=20,
    pady=15
)
tk.Label(
    form_frame,
    text="Marks",
    font=("Arial", 12, "bold"),
    bg="white"
).grid(row=4, column=0, padx=20, pady=15)

marks_entry = tk.Entry(
    form_frame,
    font=("Arial", 12)
)

marks_entry.grid(
    row=4,
    column=1,
    padx=20,
    pady=15
)

add_button=tk.Button(
    root,
    text="ADD STUDENT",
    font=("Arial",11,"bold"),
    bg="#163A63",
    fg="white",
    command=add_student_gui
)

add_button.place(
    x=450,
    y=490,
    width=180,
    height=45
)

table_frame=tk.Frame(
    root,
    bg="white"
)
table_frame.place(
    x=150,
    y=550,
    width=900,
    height=120
)

#adding structure that will represent the data in tablular form

table=ttk.Treeview(
    table_frame,
    columns=(
        "ID",
        "NAME",
        "AGE",
        "COURSE",
        "MARKS"
    ),
    show="headings"
)
table.heading("ID",text="ID")
table.heading("NAME",text="NAME")
table.heading("AGE",text="AGE")
table.heading("COURSE",text="COURSE")
table.heading("MARKS",text="MARKS")
    
table.column("ID", width=100)
table.column("NAME", width=200)
table.column("AGE", width=100)
table.column("COURSE", width=200)
table.column("MARKS", width=100)

table.pack(
    fill="both",
    expand=True
)
refresh_table()
root.mainloop()

