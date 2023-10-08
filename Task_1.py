import customtkinter as ctk


# --------------------------------------------------------------------------------------
class ToDo:
    def __init__(self, main, tasks):
        self.main = main
        self.main.geometry('330x560')
        self.main.configure(fg_color='black')
        self.main.resizable(False, False)
        self.main.title('To Do List')

        # ---------------------------------------------------------------------
        self.tabs = ctk.CTkTabview(main, width=290, height=480, corner_radius=20)
        self.tabs.place(x=20, y=10)
        self.tabs.add('All')
        self.tabs.add('Imp')
        self.tabs.add('Completed')
        self.tabs.set('All')

        self.task_list = ctk.CTk
        self.imp_label = ctk.CTkLabel(main, text='Tick Check box if Task is very Completed!')
        self.addButton = ctk.CTkButton(main, text='Add Task', command=lambda: self.add(), font=ctk.CTkFont('Helvetica'),
                                       height=27,
                                       width=50)

        self.impCheck = ctk.CTkCheckBox(main, text='', height=25)
        self.entryTask = ctk.CTkEntry(main, height=27, width=180, placeholder_text='Enter Task to Do...')

        self.entryTask.place(x=50, y=500)
        self.impCheck.place(x=20, y=500)
        self.addButton.place(x=240, y=500)
        self.imp_label.place(x=45, y=527)

        self.all_task = tasks

    def update(self):
        temp_y = 0
        tpImp_y = 0
        tp_y = 0
        for i in self.all_task:
            if self.tabs.tab('Completed'):
                if i[1] == '1':
                    if i[0] == '1':
                        label = ctk.CTkLabel(self.tabs.tab('Completed'), text=i[2:], height=30, width=180,
                                             text_color='red')
                    else:
                        label = ctk.CTkLabel(self.tabs.tab('Completed'), text=i[2:], height=30, width=180)
                    label.place(x=25, y=tp_y + 5)
                    tp_y += 30
            if self.tabs.tab('Imp'):
                if i[0] == '1' and i[1] == '0':
                    label = ctk.CTkLabel(self.tabs.tab('Imp'), text=i[2:], height=30, width=180, text_color='red')
                    check = ctk.CTkCheckBox(self.tabs.tab('Imp'), text='', width=0, checkbox_height=17,
                                            checkbox_width=17,
                                            border_width=2, command=lambda x=i: self.complete(x), corner_radius=4)
                    delButton = ctk.CTkButton(self.tabs.tab('Imp'), text='Delete', command=lambda x=i: self.delete(x),
                                              height=20,
                                              width=45, corner_radius=10)
                    delButton.place(x=170, y=tpImp_y + 5)
                    editButton = ctk.CTkButton(self.tabs.tab('Imp'), text='Edit', command=lambda x=i: self.edit(x),
                                               height=20,
                                               width=45, corner_radius=10)
                    editButton.place(x=123, y=tpImp_y + 5)
                    check.place(x=0, y=tpImp_y + 4)
                    label.place(x=-25, y=tpImp_y)
                    tpImp_y += 30

            if i[0] == '1' and i[1] == '0':
                label = ctk.CTkLabel(self.tabs.tab('All'), text=i[2:], height=30, width=180, text_color='red')
                check = ctk.CTkCheckBox(self.tabs.tab('All'), text='', width=0, checkbox_height=17, checkbox_width=17,
                                        border_width=2, command=lambda x=i: self.complete(x), corner_radius=4)
                delButton = ctk.CTkButton(self.tabs.tab('All'), text='Delete', command=lambda x=i: self.delete(x),
                                          height=20,
                                          width=45, corner_radius=10)
                delButton.place(x=170, y=temp_y + 5)
                editButton = ctk.CTkButton(self.tabs.tab('All'), text='Edit', command=lambda x=i: self.edit(x),
                                           height=20,
                                           width=45, corner_radius=10)
                editButton.place(x=123, y=temp_y + 5)
                check.place(x=0, y=temp_y + 4)
                label.place(x=-25, y=temp_y)
                temp_y += 30


            elif i[0] == '0' and i[1] == '0':
                label = ctk.CTkLabel(self.tabs.tab("All"), text=i[2:], height=30, width=190)
                check = ctk.CTkCheckBox(self.tabs.tab('All'), text='', width=0, checkbox_height=17, checkbox_width=17,
                                        border_width=2, command=lambda x=i: self.complete(x), corner_radius=4)
                delButton = ctk.CTkButton(self.tabs.tab('All'), text='Delete', command=lambda x=i: self.delete(x),
                                          height=20,
                                          width=45, corner_radius=10)
                delButton.place(x=170, y=temp_y + 5)
                editButton = ctk.CTkButton(self.tabs.tab('All'), text='Edit', command=lambda x=i: self.edit(x),
                                           height=20,
                                           width=45, corner_radius=10)
                editButton.place(x=123, y=temp_y + 5)
                check.place(x=0, y=temp_y + 4)
                label.place(x=-25, y=temp_y)
                temp_y += 30
            elif i == 'the':
                if self.tabs.tab('Imp'):
                    label = ctk.CTkLabel(self.tabs.tab("Imp"), text='', height=30, width=300)
                    label.place(x=-25, y=tpImp_y)
                    tpImp_y += 30

                label = ctk.CTkLabel(self.tabs.tab("All"), text='', height=30, width=300)
                label.place(x=-25, y=temp_y)
                self.all_task.pop(self.all_task.index('the'))
                temp_y += 30

    def add(self):
        if len(self.entryTask.get()) > 0 and self.impCheck.get():
            self.all_task.insert(0, '10' + self.entryTask.get())
            self.update()
        elif self.entryTask.get():
            self.all_task.insert(0, '00' + self.entryTask.get())
            self.update()
        self.entryTask.delete(0, len(self.entryTask.get()))

    def delete(self, index):
        self.all_task.remove(index)
        self.all_task.append('the')
        self.update()

    def edit(self, index):
        global edEntry, edButton
        var = ctk.StringVar(value=index[2:])
        edEntry = ctk.CTkEntry(self.tabs.tab('All'), height=27, width=180, textvariable=var)
        edEntry.place(x=25, y=300)
        edButton = ctk.CTkButton(self.tabs.tab('All'), height=30, width=150, text='Change', corner_radius=25,
                                 command=lambda: self.change(index))
        edButton.place(x=40, y=350)

    def change(self, index):
        global edEntry, edButton
        if len(edEntry.get()) > 0:
            self.all_task[self.all_task.index(index)] = index[:2] + edEntry.get()
        edEntry.destroy()
        edButton.destroy()
        self.update()

    def complete(self, index):
        self.all_task.append(index[0] + '1' + index[2:])
        self.delete(index)


all_task = ['11Play Cricket', '10Go for Walk', '00Do Homework', '00Rest Time', '10Sleep', '00Play Games',
            '01Eat Cookies']
if __name__ == '__main__':
    main = ctk.CTk()
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    app = ToDo(main, all_task)
    app.update()
    main.mainloop()
