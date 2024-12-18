import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from typing import List


class WorkerWin(tk.Tk):

    def __init__(self):
        super().__init__()

        self.geometry('1820x900+0+0')

        self.form_x = 10
        self.entry_width = 20
        self.tickets = []

        gen_y = self.gen_form_y(start=10, step=30)

        label_form_list = [
            'Вид техники',
            'Модель',
            'Описание проблемы',
            'ФИО клиента',
            'Номер телефона',
        ]

        form_list = []
        status_label = 'Статус заявки'
        tk.Label(self, text=status_label).place(x=self.form_x, y=next(gen_y))
        form_list.append(ttk.Combobox(self, width=self.entry_width, values=['Новая', 'в процессе ремонта', 'Завершена']))
        label_form_list.append(status_label)
        form_list[-1].current(0)
        form_list[-1].place(x=self.form_x, y=next(gen_y))

        add = tk.Button(self, width=self.entry_width, text='Добавить заявку', command=self.add_ticket)
        add.place(x=self.form_x, y=next(gen_y))

        update = tk.Button(self, width=self.entry_width, text='Изменить заявку', command=self.update_ticket)
        update.place(x=self.form_x, y=next(gen_y))

        tree = ttk.Treeview(self, show="headings", columns=label_form_list, height=30)
        for i in label_form_list:
            tree.heading(i, text=i)

        tree.place(x=200, y=0)




    def add_ticket(self):
        ticket = []
        try:
            for item in range(len(self.form_list)):
                ticket.append(self.form_list[item].get())
        except Exception:
            showerror('Ошибка', 'Заявка не добавлена')
        else:
            self.tickets.append(ticket)
            showinfo('Успешно', "Заявка добавлена")
            self.print_ticket()

    def update_ticket(self):
        id = self.form_list[0].get()
        for index, el in enumerate(self.tickets):
            if id == el[0]:
                for item in range(1, len(self.form_list)):
                    el[item] = self.form_list[item].get() if self.form_list[item].get() else el[item]
                self.tickets[index] = el
                print(self.tickets[index])
                break
        showinfo('Успешно', 'Заявка обновлена')
        self.print_ticket()

    def print_ticket(self):
        self.tree.delete(*self.tree.get_children())
        for item in self.tickets:
            self.tree.insert('', 'end', values=item)

    def create_form(self, x: int, width: int, label_list: List[str], entry_list: List[tk.Entry]):
        for item in label_list:
            tk.Label(self, text=item).place(x=x, y=next(self.gen_y))
            obj = tk.Entry(self, width=width)
            obj.place(x=x, y=next(self.gen_y))
            entry_list.append(obj)


workerWin = WorkerWin()
workerWin.mainloop()