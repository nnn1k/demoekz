import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from typing import List

win = tk.Tk()
win.geometry('1820x900+0+0')

form_x = 10
entry_width = 20
tickets = []

def gen_form_y(start: int, step: int):
    y = start
    while True:
        yield y
        y += step


gen_y = gen_form_y(start=10, step=30)

def add_ticket():
    ticket = []
    try:
        for item in range(len(form_list)):
            ticket.append(form_list[item].get())
    except Exception:
        showerror('Ошибка', 'Заявка не добавлена')
    else:
        tickets.append(ticket)
        showinfo('Успешно', "Заявка добавлена")
        print_ticket()


def update_ticket():
    id = form_list[0].get()
    for index, el in enumerate(tickets):
        if id == el[0]:
            for item in range(1, len(form_list)):
                el[item] = form_list[item].get() if form_list[item].get() else el[item]
            tickets[index] = el
            print(tickets[index])
            break
    showinfo('Успешно', 'Заявка обновлена')
    print_ticket()

def print_ticket():
    tree.delete(*tree.get_children())
    for item in tickets:
        tree.insert('', 'end', values=item)

def create_form(x: int, width: int, label_list: List[str], entry_list: List[tk.Entry]):
    for item in label_list:
        tk.Label(win, text=item).place(x=x, y=next(gen_y))
        obj = tk.Entry(win, width=width)
        obj.place(x=x, y=next(gen_y))
        entry_list.append(obj)


label_form_list = [
    'Номер заявки',
    'Дата добавления',
    'Вид техники',
    'Модель',
    'Описание проблемы',
    'ФИО клиента',
    'Номер телефона',
    ]

form_list = []
create_form(form_x, entry_width, label_form_list, form_list)
status_label = 'Статус заявки'
tk.Label(win, text=status_label).place(x=form_x, y=next(gen_y))
form_list.append(ttk.Combobox(win, width=entry_width, values=['Новая', 'в процессе ремонта', 'Завершена']))
label_form_list.append(status_label)
form_list[-1].current(0)
form_list[-1].place(x=form_x, y=next(gen_y))


add = tk.Button(win, width=entry_width, text='Добавить заявку', command=add_ticket)
add.place(x=form_x, y=next(gen_y))

update = tk.Button(win, width=entry_width, text='Изменить заявку', command=update_ticket)
update.place(x=form_x, y=next(gen_y))

tree = ttk.Treeview(win, show="headings", columns=label_form_list, height=30)
for i in label_form_list:
    tree.heading(i, text=i)

tree.place(x=200, y=0)

win.mainloop()
