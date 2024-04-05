#!/usr/bin/env python
# coding: utf-8

# In[12]:


import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import pickle

def add_task():
    task = entry_tasks.get()
    if task.strip() != "":
        tasks.append((task, False))
        update_listbox()
        entry_tasks.delete(0, END)
    else:
        mb.showwarning(title="Warning!", message="You must enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        del tasks[task_index]
        update_listbox()
    except IndexError:
        mb.showwarning(title='Warning!', message="You must select a task.")


def mark_completed():
    try:
        task_index = listbox_tasks.curselection()[0]
        task, status = tasks[task_index]
        tasks[task_index] = (task, not status)
        update_listbox()
    except IndexError:
        mb.showwarning(title='Warning!', message="You must select a task.")

def update_listbox():
    listbox_tasks.delete(0, END)
    for i, (task, status) in enumerate(tasks):
        symbol = "✔️" if status else "❌"
        listbox_tasks.insert(END, f"{symbol} {task}")


def load_tasks():
    global tasks
    try:
        with open("tasks.dat", "rb") as f:
            tasks = pickle.load(f)
        update_listbox()
    except FileNotFoundError:
        mb.showwarning(title="Warning!", message="Cannot find tasks.dat.")

def save_tasks():
    with open("tasks.dat", "wb") as f:
        pickle.dump(tasks, f)
    mb.showinfo(title="Save", message="Tasks saved successfully.")

def reset_entries():
    tasks.clear()
    update_listbox()

root = tk.Tk()
root.title("To-Do List")
root.config(bg="white")
root.geometry("1500x1100")

tasks = []

frame_tasks = tk.Frame(root)
frame_tasks.pack()

scrollbar_tasks = tk.Scrollbar(frame_tasks, orient=VERTICAL)
scrollbar_tasks.pack(side=RIGHT, fill=Y)

listbox_tasks = Listbox(frame_tasks, yscrollcommand=scrollbar_tasks.set, font=("Times New Roman", 12, "bold"), height=18, width=150)
listbox_tasks.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_tasks = tk.Entry(root, font=("Times New Roman", 15, "bold"), width=150)
entry_tasks.pack()

button_add_tasks = tk.Button(root, text="Add Task", font=("Times New Roman", 18, "bold"), bg='#4CAF50', fg='white', width=150, command=add_task)
button_add_tasks.pack()

button_delete_tasks = tk.Button(root, text="Delete Task", font=("Times New Roman", 18, "bold"), bg='#FFC107', width=150, command=delete_task)
button_delete_tasks.pack()

button_load_tasks = tk.Button(root, text="Load Task", font=("Times New Roman", 18, "bold"), bg='#FF5722', fg='white',  width=150, command=load_tasks)
button_load_tasks.pack()

button_save_tasks = tk.Button(root, text="Save Task", font=("Times New Roman", 18, "bold"), bg='#E91E63', fg='white', width=150, command=save_tasks)
button_save_tasks.pack()

complete_button = tk.Button(root, text="Mark as Completed", font=("Times New Roman", 18, "bold"), bg='#4273b3', fg='white',  width=150, command=mark_completed)
complete_button.pack()

button_reset_tasks = tk.Button(root, text="Reset Task", font=("Times New Roman", 18, "bold"), bg='#8BC34A', width=150, command=reset_entries)
button_reset_tasks.pack()

root.mainloop()


# In[ ]:




