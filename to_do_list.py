import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = 'tasks.json'


root = tk.Tk()
root.title('Список задач')
root.geometry('400x400')


top_frame = tk.Frame(root).pack(pady = 10, padx = 10, fill = tk.X)
entry = tk.Entry(top_frame).pack(padx = (0, 5), expand = True, fill = tk.X, side = tk.LEFT)
btn = tk.Button(top_frame, text = 'Добавить').pack(side = tk.LEFT)
mid_frame = tk.Frame(root).pack(padx = 10, pady = (0, 10), expand = True, fill = tk.BOTH)


scrollbar = tk.Scrollbar(mid_frame).pack(fill = tk.Y, side = tk.RIGHT)

listbox = tk.Listbox(mid_frame, selectmode = tk.SINGLE).pack(fill = tk.BOTH, side = tk.LEFT, expand = True)

scrollbar.config(command = listbox.yview)


bot_frame = tk.Frame(root).pack(padx = 10, pady = 10)

done_btn = tk.Button(bot_frame, text = 'сделано').pack(padx = 5, side = tk.LEFT)






root.mainloop()