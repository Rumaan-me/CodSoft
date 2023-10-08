import tkinter

import customtkinter as ctk
import random


class PassCodeGenerator:
    def __init__(self, window):

        self.main = window
        self.main.geometry('300x500')
        self.main.resizable(False, False)
        self.main.title('Password Generator')
        self.main.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform='a')
        self.main.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
        self.var1 = ctk.StringVar(value=tkinter.NORMAL)
        self.var2 = ctk.StringVar(value=tkinter.NORMAL)
        self.name = ctk.CTkLabel(self.main, text='Password Generator', fg_color='#3b3b3b', width=250,
                                 corner_radius=7).pack(
            padx=5, pady=10)

        self.option = ctk.CTkButton(self.main, text='Customize your password', width=100, corner_radius=7, hover=False)
        self.option.pack(padx=5, pady=15)
        self.generateButton = ctk.CTkButton(self.main, text='Generate', command=lambda: self.generate(),
                                            font=ctk.CTkFont('Helvetica'),
                                            height=27, width=50, corner_radius=25)
        self.passLength = ctk.CTkEntry(self.main, height=27, width=240, placeholder_text='Enter Length of Password...')
        self.selectUpper = ctk.CTkCheckBox(self.main, height=10, offvalue='n', onvalue='y', text='Upper Case', )
        self.selectLower = ctk.CTkCheckBox(self.main, height=10, offvalue='n', onvalue='y', text='Lower Case', )
        self.selectNumber = ctk.CTkCheckBox(self.main, height=10, offvalue='n', onvalue='y', text='Numbers', )
        self.selectSpecial = ctk.CTkCheckBox(self.main, height=10, offvalue='n', onvalue='y', text='Special Keys')

        self.choice = ctk.CTkComboBox(self.main, command=self.refresh, width=240,
                                      values=['Easy to Say...', 'Easy to Write...', 'All Characters...'])
        self.choice.set('All Characters...')
        self.selectUpper.place(x=30, y=110)
        self.selectLower.place(x=160, y=110)
        self.selectNumber.place(x=30, y=160)
        self.selectSpecial.place(x=160, y=160)
        self.choice.place(x=30, y=220)
        self.passLength.place(x=30, y=270)
        self.generateButton.place(x=107, y=320)
        self.caps = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        self.low = 'qwertyuiopasdfghjklzxcvbnm'
        self.dig = '1234567890'
        self.spec = '!"£$%^&*()-_+={}[]@#,:;?/\\'
        self.pasCode = ctk.CTkEntry(self.main, 240, )
        self.x = ''

    def refresh(self, n):
        if self.choice.get() == 'All Characters...':
            self.selectUpper.select()
            self.selectLower.select()
            self.selectSpecial.select()
            self.selectNumber.select()
            self.selectSpecial.configure(state=tkinter.NORMAL)
            self.selectNumber.configure(state=tkinter.NORMAL)
        elif self.choice.get() == 'Easy to Write...':
            self.selectUpper.select()
            self.selectLower.select()
            self.selectSpecial.deselect()
            self.selectNumber.select()
            self.selectSpecial.configure(state='disabled')
            self.selectNumber.configure(state=tkinter.NORMAL)
        elif self.choice.get() == 'Easy to Say...':
            self.selectUpper.select()
            self.selectLower.select()
            self.selectSpecial.deselect()
            self.selectNumber.deselect()
            self.selectNumber.configure(state='disabled')
            self.selectSpecial.configure(state='disabled')

    def copyPrint(self, code):
        print(code)

    def generate(self):
        self.pasCode.place(x=30, y=360)
        self.temp = []
        self.password = ''
        self.upper = self.selectUpper.get()
        self.lower = self.selectLower.get()
        self.digit = self.selectNumber.get()
        self.special = self.selectSpecial.get()
        self.temp_1 = [self.upper, self.lower, self.digit, self.special]
        self.temp_2 = [self.caps, self.low, self.dig, self.spec]
        if self.passLength.get().isdigit():
            self.length = int(self.passLength.get())
        else:
            self.length = 0
        if self.upper == 'y':
            self.temp.append(0)
        if self.lower == 'y':
            self.temp.append(1)
        if self.digit == 'y':
            self.temp.append(2)
        if self.special == 'y':
            self.temp.append(3)
        if self.length < len(self.temp):
            self.pasCode.insert(0, 'Length should be greater than number of choices.')
            self.passLength.delete(0, self.length)
        if self.length >= len(self.temp) > 0:
            for i in range(self.length):
                ran = random.choice(self.temp)
                if self.length >= 6:
                    if i == 1 or i == 2 or i == 3 or i == 4:
                        if self.temp_1[i - 1] == 'y':
                            valid = random.choice(self.temp_2[i - 1])
                            self.password += valid
                        else:
                            valid = random.choice(self.temp_2[ran])
                            self.password += valid
                    else:
                        valid = random.choice(self.temp_2[ran])
                        self.password += valid
                elif self.length <= 5:
                    if i == 0 and self.upper == 'y':
                        valid = random.choice(self.caps)
                    elif i == 1 and self.special == 'y':
                        valid = random.choice(self.spec)
                    elif i == 2 and self.digit == 'y':
                        valid = random.choice(self.dig)
                    elif i == 3 and self.lower == 'y':
                        valid = random.choice(self.lower)
                    elif self.temp_1[ran] == 'y':
                        valid = random.choice(self.temp_2[ran])
                    self.password += valid
            self.passLength.delete(0, self.length)
            self.pasCode.delete(0, len(self.pasCode.get()))
            self.pasCode.insert(0, str(self.password))
            copyBut = ctk.CTkButton(self.main, command=lambda: self.copyPrint(self.password), text='Print', height=27,
                                    width=65, corner_radius=25).place(x=115, y=400)
        else:
            self.passLength.delete(0, self.length)
            self.pasCode.delete(0, len(self.pasCode.get()))
            self.pasCode.insert(0, 'Password length & selection cannot be 0.')


main = ctk.CTk()
ctk.set_default_color_theme("green")
app = PassCodeGenerator(main)
main.mainloop()
