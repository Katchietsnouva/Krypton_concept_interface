import tkinter
import tkinter.ttk as ttk
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Create the main application window
app = customtkinter.CTk()
app.title('Krypton Concept Interface')
app.geometry('1000x700')

# Define your functions
def select_callback(choice):
    choice = variable.get()
    print("display_selected", choice)

def widget_click():
    print("widget clicked")

def set_new_scaling(scaling):
    customtkinter.set_window_scaling(scaling)
    customtkinter.set_widget_scaling(scaling)

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

def exit_application():
    app.quit()

# STRUCTURE
combined_hemispheres = customtkinter.CTkFrame(master=app)
left_hemisphere = customtkinter.CTkFrame(master=combined_hemispheres)
right_hemisphere = customtkinter.CTkFrame(master=combined_hemispheres)

# CREATE HEADER GROUP
header_group = customtkinter.CTkFrame(master=left_hemisphere)
switch_group = customtkinter.CTkFrame(master=header_group)
switch_group1 = customtkinter.CTkFrame(master=switch_group)
switch_1 = customtkinter.CTkSwitch(master=switch_group1, text="Dark Mode", command=widget_click)
switch_2 = customtkinter.CTkSwitch(master=switch_group1, text="Airplane Mode", command=widget_click)

# switch_1.pack(padx=20, pady=(0))
# switch_2.pack(padx=20, pady=(0))
switch_1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
switch_2.grid(row=1, column=0, padx=10, pady=10, sticky="w")


switch_group2 = customtkinter.CTkFrame(master=switch_group)
switch_3 = customtkinter.CTkSwitch(master=switch_group2, text="switch_1", command=widget_click)
switch_4 = customtkinter.CTkSwitch(master=switch_group2, text="switch_1", command=widget_click)

# switch_3.pack(padx=20, pady=(0))
# switch_4.pack(padx=20, pady=(0))
switch_3.grid(row=0, column=0, padx=10, pady=10, sticky="w")
switch_4.grid(row=1, column=0, padx=10, pady=10, sticky="w")

switch_group1.pack(side='left', padx=5, pady=0)
switch_group2.pack(side='left', padx=5, pady=0)


# EXIT BUTTON
button_exit = customtkinter.CTkButton(master=switch_group, text="Exit", command=exit_application)
button_exit.pack(side= 'left', padx = 10, pady=10)  
switch_group.pack()
header_group.pack(padx=20, pady=10)

countries = ['Bahamas', 'Canada', 'Cuba', 'United States', "long sdhfhjgdshjafghdgshfhjdsfj"]
variable = tkinter.StringVar()
variable.set("test")

# OPTION GROUP 1
# option_and_scroll_view = ttk.Frame(master=app)
option_and_scroll_view = customtkinter.CTkFrame(master=left_hemisphere)
options_frame = customtkinter.CTkFrame(master=option_and_scroll_view)

optionmenu_1 = customtkinter.CTkOptionMenu(master=options_frame, variable=variable, values=countries, command=select_callback)
optionmenu_2 = customtkinter.CTkOptionMenu(master=options_frame, variable=variable, values=countries, command=select_callback)
optionmenu_3 = customtkinter.CTkOptionMenu(master=options_frame, variable=variable, values=countries, command=select_callback)
optionmenu_4 = customtkinter.CTkOptionMenu(master=options_frame, variable=variable, values=countries, command=select_callback)
optionmenu_5 = customtkinter.CTkOptionMenu(master=options_frame, variable=variable, values=countries, command=select_callback)
optionmenu_6 = customtkinter.CTkOptionMenu(master=options_frame, variable=variable, values=countries, command=select_callback)
optionmenu_7 = customtkinter.CTkOptionMenu(master=options_frame, variable=variable, values=countries, command=select_callback, dynamic_resizing=False)

optionmenu_1.pack(pady=4, padx=10)
optionmenu_2.pack(pady=4, padx=10)
optionmenu_3.pack(pady=4, padx=10)
optionmenu_4.pack(pady=4, padx=10)
optionmenu_5.pack(pady=4, padx=10)
optionmenu_6.pack(pady=4, padx=10)
optionmenu_7.pack(pady=4, padx=10)
options_frame.pack(side='left', pady=10, padx=10)

# OPTION GROUP 2
# Create scrollable frame
scrollable_frame = customtkinter.CTkScrollableFrame(master=option_and_scroll_view, label_text="Krypton Options")
scrollable_frame.pack(fill="both", expand=True)
scrollable_frame.grid_columnconfigure(0, weight=1)
scrollable_frame_switches = []
for i in range(100):
    switch = customtkinter.CTkSwitch(master=scrollable_frame, text=f"KryptonOptions {i}")
    switch.grid(row=i, column=0, padx=10, pady=(0, 10))
    scrollable_frame_switches.append(switch)

scrollable_frame.pack(side="left", padx = 10, pady=10)
option_and_scroll_view.pack(padx = 10, pady=10)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
left_hemisphere.pack(side='left', padx=20, pady=20)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# COMBO BOX
combobox_1 = customtkinter.CTkComboBox(right_hemisphere, variable=variable, values=countries, command=select_callback, width=300)
combobox_1.pack(pady=10, padx=10)
combobox_2 = customtkinter.CTkComboBox(right_hemisphere, variable=variable, values=countries, command=select_callback, width=300)
combobox_2.pack(pady=10, padx=10)

# SLIDER
scaling_slider = customtkinter.CTkSlider(right_hemisphere, command=set_new_scaling, from_=0, to=2)
scaling_slider.pack(pady=10, padx=10)

# ENTRY BOXES
entry_field = customtkinter.CTkFrame(master=right_hemisphere)
entry_field_left = customtkinter.CTkFrame(master=entry_field)
entry_field_right = customtkinter.CTkFrame(master=entry_field)

entry_1 = customtkinter.CTkEntry(master = entry_field_left, placeholder_text="placeholder")
entry_1.pack(pady=(10, 10))
entry_1.insert(0, "sdfjk")
entry_1.delete(0, "end")

entry_2 = customtkinter.CTkEntry(master = entry_field_left, placeholder_text="placeholder")
entry_2.pack(pady=(10, 10))
entry_2.insert(0, "sdfjk")
entry_2.delete(0, "end")

entry_1.pack(padx = 10)
entry_2.pack(padx = 10)
entry_field_left.pack(side='left', padx = 10, pady = 10)

entry_3 = customtkinter.CTkEntry(master = entry_field_right, placeholder_text="placeholder")
entry_3.pack(pady=(10, 10))
entry_3.insert(0, "sdfjk")
entry_3.delete(0, "end")

entry_4 = customtkinter.CTkEntry(master = entry_field_right, placeholder_text="password", show="*")
entry_4.pack(pady=(10, 10))
entry_4.insert(0, "sdfjk")
entry_4.delete(0, 2)

entry_3.pack(padx = 10)
entry_4.pack(padx = 10)
entry_field_right.pack(side='left', padx = 10, pady = 10)
entry_field.pack()

# OPEN FILE AND SAVE FILE, FOLDER BUTTONS
openfile_frame = customtkinter.CTkFrame(master=right_hemisphere)
openfile_frame_sub1 = customtkinter.CTkFrame(master=openfile_frame)
openfile_frame_sub2 = customtkinter.CTkFrame(master=openfile_frame)

button_open_file = customtkinter.CTkButton(openfile_frame_sub1, text="Open File", command=open_file_dialog)
button_open_directory = customtkinter.CTkButton(openfile_frame_sub1, text="Open Directory", command=open_directory_dialog)

button_save_as_file = customtkinter.CTkButton(openfile_frame_sub2, text="Save File As", command=save_as_file_dialog)
button_save_as_file_name = customtkinter.CTkButton(openfile_frame_sub2, text="Save File Name As", command=save_as_file_name_dialog)

button_open_file.pack(pady=10, padx=10)
button_open_directory.pack(pady=10, padx=10)

button_save_as_file.pack(pady=10, padx=10)
button_save_as_file_name.pack(pady=10, padx=10)

openfile_frame_sub1.pack(side='left', pady=10, padx=10)
openfile_frame_sub2.pack(side='left', pady=10, padx=10)
openfile_frame.pack(pady=10, padx=10)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
right_hemisphere.pack(side='left', padx=20,pady=20)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
combined_hemispheres.pack()


# Start the main loop
app.mainloop()
