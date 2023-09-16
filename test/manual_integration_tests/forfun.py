# import customtkinter as ctk
# ctk.set_default_color_theme('dark-blue')
# screen = ctk.CTk()
# screen.geometry('350x450')
# screen.title('Nouvagen')
# screen.mainloop()


import tkinter as tk
from tkinter import ttk

window = ttk.Window(themename='dark')
window = tk.Tk()
window.geometry('300x400')
window.title('Nouva Music')
title_label = ttk.Label(master=window, font='Calibri', text='Input' )
title_label.pack()
window.mainloop()