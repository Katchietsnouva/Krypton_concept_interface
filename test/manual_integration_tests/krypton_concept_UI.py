import tkinter
import tkinter.ttk as ttk
from typing import Self
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


# Define the App class
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('Krypton Concept Interface')
        self.geometry('400x800')

        # app = customtkinter.CTk()
        # app.title('Krypton Concept Interface')
        # app.geometry('400x800')


        def select_callback(choice):
            choice = variable.get()
            print("display_selected", choice)


        def widget_click():
            print("widget clicked")


        switch_1 = customtkinter.CTkSwitch(
            master=app, text="switch_1", command=widget_click)
        switch_1.pack(padx=20, pady=(20, 10))

        countries = ['Bahamas', 'Canada', 'Cuba',
                    'United States', "long sdhfhjgdshjafghdgshfhjdsfj"]

        variable = tkinter.StringVar()
        variable.set("test")

        # optionmenu_tk = tkinter.OptionMenu(app, variable, *countries, command=select_callback)
        # optionmenu_tk.pack(pady=10, padx=10)

        options_frame = ttk.Frame(master=app)

        optionmenu_1 = customtkinter.CTkOptionMenu(
            master=options_frame, variable=variable, values=countries, command=select_callback)
        optionmenu_2 = customtkinter.CTkOptionMenu(master=options_frame, variable=variable, values=countries, command=select_callback,
                                                dynamic_resizing=False)
        optionmenu_1.pack(side='left', pady=20, padx=10)
        optionmenu_2.pack(side='left', pady=20, padx=10)
        options_frame.pack()

        # combobox_tk = ttk.Combobox(app, values=countries, textvariable=variable)
        # combobox_tk.pack(pady=10, padx=10)

        combobox_1 = customtkinter.CTkComboBox(
            app, variable=variable, values=countries, command=select_callback, width=300)
        combobox_1.pack(pady=20, padx=10)


        def set_new_scaling(scaling):
            customtkinter.set_window_scaling(scaling)
            customtkinter.set_widget_scaling(scaling)


        scaling_slider = customtkinter.CTkSlider(
            app, command=set_new_scaling, from_=0, to=2)
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


        openfile_frame = ttk.Frame(master=app)
        openfile_frame_sub1 = ttk.Frame(master=openfile_frame)

        button_open_file = customtkinter.CTkButton(
            openfile_frame_sub1, text="Open File Dialog", command=open_file_dialog)
        button_open_file_name = customtkinter.CTkButton(
            openfile_frame_sub1, text="Open File Name Dialog", command=open_file_name_dialog)
        button_open_directory = customtkinter.CTkButton(
            openfile_frame_sub1, text="Open Directory Dialog", command=open_directory_dialog)

        openfile_frame_sub2 = ttk.Frame(master=openfile_frame)

        button_save_as_file = customtkinter.CTkButton(
            openfile_frame_sub2, text="Save As File Dialog", command=save_as_file_dialog)
        button_save_as_file_name = customtkinter.CTkButton(
            openfile_frame_sub2, text="Save As File Name Dialog", command=save_as_file_name_dialog)

        button_open_file.pack(pady=10, padx=10)
        button_open_file_name.pack(pady=10, padx=10)
        button_open_directory.pack(pady=10, padx=10)

        button_save_as_file.pack(pady=10, padx=10)
        button_save_as_file_name.pack(pady=10, padx=10)
        openfile_frame_sub1.pack(side='left', pady=10, padx=10)
        openfile_frame_sub2.pack(side='left', pady=10, padx=10)
        openfile_frame.pack()

        # ...


        def exit_application():
            app.quit()


        button_exit = customtkinter.CTkButton(
            app, text="Exit", command=exit_application)
        button_exit.pack(pady=10)

        entry_3 = customtkinter.CTkEntry(app, placeholder_text="placeholder")
        entry_3.pack(pady=(40, 20))
        entry_3.insert(0, "sdfjk")
        entry_3.delete(0, "end")

        entry_4 = customtkinter.CTkEntry(app, placeholder_text="password", show="*")
        entry_4.pack(pady=(20, 20))
        entry_4.insert(0, "sdfjk")
        entry_4.delete(0, 2)

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(
            self, label_text="CTkScrollableFrame")
        self.scrollable_frame.grid(row=1, column=2, padx=(
            20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        for i in range(100):
            switch = customtkinter.CTkSwitch(
                master=self.scrollable_frame, text=f"CTkSwitch {i}")
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)


# Create the application instance and start the main loop
if __name__ == "__main__":
    app = App()
    app.mainloop()
