import tkinter as tk
from typing import List


class AuthWin(tk.Tk):

    def __init__(self):
        super().__init__()

        self.geometry('500x500')

        self.label_list = ['Логин', 'Пароль']
        self.entry_list = []
        self.gen_y = self.gen_form_y(10, 60)
        self.create_form(150, 20, self.label_list, self.entry_list)


    def create_form(self, x: int, width: int, label_list: List[str], entry_list: List[tk.Entry]):
        for item in label_list:
            tk.Label(self, text=item).place(x=x, y=next(self.gen_y))
            obj = tk.Entry(self, width=width)
            obj.place(x=x, y=next(self.gen_y))
            entry_list.append(obj)

    @staticmethod
    def gen_form_y(start: int, step: int):
        y = start
        while True:
            yield y
            y += step


auth = AuthWin()
auth.mainloop()
