import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = 'tasks.json'


root = tk.Tk()
root.title('Список задач')
root.geometry('400x400')

# функции для работы с задачами

def add_task():
    text = entry.get()
    if not text:
        messagebox.showwarning('ОШИБКА', 'ВВЕДИТЕ ЗАДАЧУ')
        return

top_frame = tk.Frame(root)
top_frame.pack(pady = 10, padx = 10, fill = tk.X)
entry = tk.Entry(top_frame)
entry.pack(padx = (0, 5), expand = True, fill = tk.X, side = tk.LEFT)
btn = tk.Button(top_frame, text = 'Добавить', command = add_task)
btn.pack(side = tk.LEFT)
mid_frame = tk.Frame(root)
mid_frame.pack(padx = 10, pady = (0, 10), expand = True, fill = tk.BOTH)


scrollbar = tk.Scrollbar(mid_frame)
scrollbar.pack(fill = tk.Y, side = tk.RIGHT)

listbox = tk.Listbox(mid_frame, selectmode = tk.SINGLE)
listbox.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)

scrollbar.config(command = listbox.yview)


bot_frame = tk.Frame(root)
bot_frame.pack(padx = 10, pady = 10)

done_btn = tk.Button(bot_frame, text = 'сделано', width = 15, height = 2, font = ('Arial', 15))
done_btn.pack(padx = 5, side = tk.LEFT)

del_btn = tk.Button(bot_frame, text = "Удалить", width = 15, height = 2, font = ('Arial', 15))
del_btn.pack(padx = 5, side = tk.LEFT)








root.mainloop()