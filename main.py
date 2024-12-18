import datetime
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from typing import List, Tuple

users = [
    {'login': 'admin', 'password': 'admin'},
    {'login': 'worker', 'password': 'worker'},
    {'login': '1', 'password': '1'},
]

ENTRY_WIDTH = 20
BUTTON_WIDTH = 15

def generator_func(start, step):
    counter = start
    while True:
        yield counter
        counter += step

def create_form(
        win: tk.Tk, x: int, form_objects: List[Tuple[str, str, Tuple]], generator: generator_func
) -> List:
    object_list = []
    for text, obj_type, values in form_objects:
        match obj_type:
            case 'entry':
                tk.Label(win, text=text).place(x=x, y=next(generator))
                obj = tk.Entry(win, width=ENTRY_WIDTH)
                obj.place(x=x, y=next(generator))
                object_list.append(obj)
            case 'combobox':
                tk.Label(win, text=text).place(x=x, y=next(generator))
                obj = ttk.Combobox(win, values=values)
                obj.current(0)
                obj.place(x=x, y=next(generator))
                object_list.append(obj)
            case 'button':
                button = tk.Button(win, text=text, width=BUTTON_WIDTH, command=values)
                button.place(x=x, y=next(generator))
            case _:
                pass
    return object_list

def swap_windows(win1: tk.Tk, win2: tk.Tk):
    win1.withdraw()
    win2.deiconify()

def authenticate():
    login = auth_win.auth_object[0].get()
    password = auth_win.auth_object[1].get()
    for user in users:
        if user['login'] == login and user['password'] == password:
            swap_windows(auth_win, admin_win)

def print_applications():
    admin_win.tree.delete(*admin_win.tree.get_children())
    for application in admin_win.applications:
        admin_win.tree.insert('', 'end', values=application)


def add_application():
    application = list()
    application.append(next(admin_win.id_generator))
    application.append(datetime.datetime.now())
    for item in admin_win.admin_object:
        application.append(item.get())
    admin_win.applications.append(application)
    print_applications()

def update_application():
    current_tree = admin_win.tree.focus()
    id = admin_win.tree.item(current_tree).get('values')[0]
    for index, el in enumerate(admin_win.admin_object):
        admin_win.applications[id-1][index + 2] = el.get()

    print_applications()


class AuthWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('600x400')

        auth_form_object_list = [
            ('Логин', 'entry', ()),
            ('Пароль', 'entry', ()),
            ('Войти', 'button', authenticate)
        ]

        self.auth_object = create_form(self, 200, auth_form_object_list, generator_func(50, 30))

class AdminWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1820x800+10+10')

        admin_object_list = [
            ('Вид оргтехники', 'entry', ()),
            ('Модель', 'entry', ()),
            ('Описание проблемы', 'entry', ()),
            ('ФИО клиента', 'entry', ()),
            ('Номер телефона', 'entry', ()),
            ('Статус заявки', 'combobox', ('Новая', 'В работе', 'Завершена')),
            ('Добавить заявку', 'button', add_application),
            ('Изменить заявку', 'button', update_application),
        ]

        columns = [
            'Номер техники', 'Дата добавления',
            'Вид оргтехники', 'Модель',
            'Описание проблемы', 'ФИО клиента',
            'Номер телефона', 'Статус заявки'
        ]
        self.applications = []
        self.id_generator = generator_func(1, 1)
        self.tree = ttk.Treeview(self, columns=columns, show='headings', height=30)
        for i in columns:
            self.tree.heading(i, text=i)
        self.tree.place(x=200, y=20)
        self.admin_object = create_form(self, 10, admin_object_list, generator_func(50, 30))


auth_win = AuthWindow()
admin_win = AdminWindow()

admin_win.withdraw()
auth_win.mainloop()
