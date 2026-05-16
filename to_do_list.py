import tkinter as tk
from tkinter import messagebox
import json
import os
import logging

TASKS_FILE = 'tasks.json'

logging.basicConfig(
    filename = 'to_do.log',
    encoding = 'utf-8',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

root = tk.Tk()
root.title('Список задач')
root.geometry('400x400')

logging.info('ПРИЛОЖЕНИЕ ЗАПУЩЕНО')

# функции для работы с задачами

def add_task():
    text = entry.get()
    if not text:
        messagebox.showwarning('ОШИБКА', 'ВВЕДИТЕ ЗАДАЧУ')
        return
    tasks.append({
        'text': text,
        'done': False
    })
    logging.info(f'ДОБАВЛЕНА ЗАДАЧА:{text}')
    entry.delete(0, tk.END)
    save_task()
    refresh_listbox()
    
def load_task():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r', encoding = 'utf-8') as f:
            return json.load(f)
    return []

def save_task():
    with open(TASKS_FILE, 'w', encoding = 'utf-8') as f:
        json.dump(tasks, f, ensure_ascii = False, indent = 4)

def refresh_listbox():
    listbox.delete(0, tk.END)
    for i in tasks:
        if i['done']:
            listbox.insert(tk.END, f'✅ {i['text']}')
        else: 
            listbox.insert(tk.END, i['text'])
    update_count()

def update_count():
    total = len(tasks)
    completed = sum(i['done'] for i in tasks)
    count_releble.config(text = f'всего: {total} | выпонено: {completed} ')

def task_done():
    selected = listbox.curselection()
    if not selected: return
    index = selected[0]
    tasks[index]['done'] = True
    logging.info(f'ЗАДАЧА ВЫПОЛНЕНА: {tasks[index]['done']}')
    save_task()
    refresh_listbox()

def task_del():
    selected = listbox.curselection()
    if not selected: return
    answer = messagebox.askyesno('ПОТВЕРЖДЕНИЕ', 'ВЫ ТОЧНО ХОТИТЕ УДАЛИТЬ ЗАДАЧУ?')
    if not answer: return
    index = selected[0]
    tasks.pop(index)
    logging.info('ЗАДАЧА УДАЛЕНА')
    save_task()
    refresh_listbox()

def edit_task(event):
    selected = listbox.curselection()
    if not selected: return
    index = selected[0]
    win_edit = tk.Toplevel(root)
    win_edit.title('Редактировать задачу')
    win_edit.geometry('300x150')

    new_entry = tk.Entry(win_edit, width = 42)
    new_entry.pack(padx = 10, pady = 10)
    new_entry.insert(0, tasks[index]['text'])
    new_entry.focus()

    def save_new_task():
        new_text = new_entry.get().strip()
        if not new_text:
            messagebox.showwarning('ОШИБКА!', 'ВВЕДИ ТЕКСТ ЗАДАЧИ!')
            return
        tasks[index]['text'] = new_text
        save_task()
        refresh_listbox()
        win_edit.destroy()
    
    save_btn = tk.Button(win_edit, text = 'СОХРАНИТЬ', command = save_new_task)
    save_btn.pack(pady = 7)

top_frame = tk.Frame(root)
top_frame.pack(pady = 10, padx = 10, fill = tk.X)
entry = tk.Entry(top_frame)
entry.pack(padx = (0, 5), expand = True, fill = tk.X, side = tk.LEFT)
entry.focus()
entry.bind('<Return>', lambda event: add_task())
btn = tk.Button(top_frame, text = 'Добавить', command = add_task)
btn.pack(side = tk.LEFT)
mid_frame = tk.Frame(root)
mid_frame.pack(padx = 10, pady = (0, 10), expand = True, fill = tk.BOTH)


scrollbar = tk.Scrollbar(mid_frame)
scrollbar.pack(fill = tk.Y, side = tk.RIGHT)

listbox = tk.Listbox(mid_frame, selectmode = tk.SINGLE)
listbox.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)

listbox.bind('<Double-Button-1>', edit_task)

scrollbar.config(command = listbox.yview)


bot_frame = tk.Frame(root)
bot_frame.pack(padx = 10, pady = 10)

count_releble = tk.Label(root, text = '')
count_releble.pack(pady = (0, 10))

done_btn = tk.Button(bot_frame, text = 'сделано', width = 15, height = 2, font = ('Arial', 15), command = task_done)
done_btn.pack(padx = 5, side = tk.LEFT)

del_btn = tk.Button(bot_frame, text = "Удалить", width = 15, height = 2, font = ('Arial', 15), command = task_del)
del_btn.pack(padx = 5, side = tk.LEFT)




tasks = load_task()
refresh_listbox()
root.mainloop()