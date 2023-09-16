# import customtkinter as ctk
# ctk.set_default_color_theme('dark-blue')
# screen = ctk.CTk()
# screen.geometry('350x450')
# screen.title('Nouvagen')
# screen.mainloop()


import tkinter as tk
from tkinter import ttk

window = tk.Tk()
ttk.Style().theme_use('alt')
window.geometry('500x700')
window.title('Nouva Music')
title_label = ttk.Label(master=window, font='Calibri 24 bold', text='Input' )
title_label.pack()

input_frame = ttk.Frame(master=window)
combo1 = ttk.Combobox(master=input_frame)
entry1 = ttk.Entry(master=input_frame)
convert_button = ttk.Button(master=input_frame)

combo1.pack(side= 'left', padx=10)
entry1.pack(side= 'left',padx=10)
convert_button.pack(side= 'left')
input_frame.pack(pady=10)

output_label = ttk.Label(master=window, text= 'Output', font='Calibri 22')

window.mainloop()