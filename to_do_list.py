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


srollbar = tk.Scrollbar(mid_frame).pack(fill = tk.Y, side = tk.RIGHT)








root.mainloop()