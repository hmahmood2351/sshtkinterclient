import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x500")

def connection():
    print("SSH connection established & command executed")
    print(entry.get())
    print(entry2.get())

label = customtkinter.CTkLabel(master=app, text="SSH Connection")
label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

entry = customtkinter.CTkEntry(master=app, placeholder_text="Type in SSH Connection")
entry.place(relx=0.5, rely=0.2, width=200, anchor=tkinter.CENTER)

label2 = customtkinter.CTkLabel(master=app, text="SSH Command")
label2.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

entry2 = customtkinter.CTkEntry(master=app, placeholder_text="Type in SSH Connection")
entry2.place(relx=0.5, rely=0.4, width=100, anchor=tkinter.CENTER)

button1 = customtkinter.CTkButton(master=app, text="Submit command", command=connection)
button1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)



app.mainloop()