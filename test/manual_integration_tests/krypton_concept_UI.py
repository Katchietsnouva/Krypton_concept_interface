import tkinter
import tkinter.ttk as ttk
import customtkinter

customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.title('Test OptionMenu ComboBox.py')
app.geometry('400x500')


def select_callback(choice):
    choice = variable.get()
    print("display_selected", choice)


countries = ['Bahamas', 'Canada', 'Cuba', 'United States', "long sdhfhjgdshjafghdgshfhjdsfj"]

variable = tkinter.StringVar()
variable.set("test")

optionmenu_tk = tkinter.OptionMenu(app, variable, *countries, command=select_callback)
optionmenu_tk.pack(pady=10, padx=10)

optionmenu_1 = customtkinter.CTkOptionMenu(app, variable=variable, values=countries, command=select_callback)
optionmenu_1.pack(pady=20, padx=10)

optionmenu_2 = customtkinter.CTkOptionMenu(app, variable=variable, values=countries, command=select_callback,
                                           dynamic_resizing=False)
optionmenu_2.pack(pady=20, padx=10)

combobox_tk = ttk.Combobox(app, values=countries, textvariable=variable)
combobox_tk.pack(pady=10, padx=10)

combobox_1 = customtkinter.CTkComboBox(app, variable=variable, values=countries, command=select_callback, width=300)
combobox_1.pack(pady=20, padx=10)

def set_new_scaling(scaling):
    customtkinter.set_window_scaling(scaling)
    customtkinter.set_widget_scaling(scaling)

scaling_slider = customtkinter.CTkSlider(app, command=set_new_scaling, from_=0, to=2)
scaling_slider.pack(pady=20, padx=10)

# Add file dialog buttons to the main application
def open_file_dialog():
    print(customtkinter.filedialog.askopenfile())

def open_directory_dialog():
    print(customtkinter.filedialog.askdirectory())

def save_as_file_dialog():
    print(customtkinter.filedialog.asksaveasfile())

def open_file_name_dialog():
    print(customtkinter.filedialog.askopenfilename())

def save_as_file_name_dialog():
    print(customtkinter.filedialog.asksaveasfilename())

button_open_file = customtkinter.CTkButton(app, text="Open File Dialog", command=open_file_dialog)
button_open_file.pack(pady=10)

button_open_directory = customtkinter.CTkButton(app, text="Open Directory Dialog", command=open_directory_dialog)
button_open_directory.pack(pady=10)

button_save_as_file = customtkinter.CTkButton(app, text="Save As File Dialog", command=save_as_file_dialog)
button_save_as_file.pack(pady=10)

button_open_file_name = customtkinter.CTkButton(app, text="Open File Name Dialog", command=open_file_name_dialog)
button_open_file_name.pack(pady=10)

button_save_as_file_name = customtkinter.CTkButton(app, text="Save As File Name Dialog", command=save_as_file_name_dialog)
button_save_as_file_name.pack(pady=10)

# ...

def exit_application():
    app.quit()

button_exit = customtkinter.CTkButton(app, text="Exit", command=exit_application)
button_exit.pack(pady=10)

app.mainloop()
