import customtkinter as ctk

main = ctk.CTk()
main.geometry('330x560')
main.configure(fg_color='#eaeaea')
main.resizable(False, False)
main.title('Calculator')
main.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform='a')
main.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')

i = ''
o = ''
eq = []

button_0 = ctk.CTkButton(main, width=34, command=lambda: b_0(), height=34, font=ctk.CTkFont('Helvetica', 26), text='0',
                         fg_color='#fcfcfc', hover_color='#eaeaea', text_color='#454545', corner_radius=2)
button_1 = ctk.CTkButton(main, width=34, command=lambda: b_1(), height=34, font=ctk.CTkFont('Helvetica', 26), text='1',
                         fg_color='#fcfcfc', hover_color='#eaeaea', text_color='#454545', corner_radius=2)
button_2 = ctk.CTkButton(main, width=34, command=lambda: b_2(), height=34, font=ctk.CTkFont('Helvetica', 26), text='2',
                         fg_color='#fcfcfc', hover_color='#eaeaea', text_color='#454545', corner_radius=2)
button_3 = ctk.CTkButton(main, width=34, command=lambda: b_3(), height=34, font=ctk.CTkFont('Helvetica', 26), text='3',
                         fg_color='#fcfcfc', hover_color='#eaeaea', text_color='#454545', corner_radius=2)
button_4 = ctk.CTkButton(main, width=34, command=lambda: b_4(), height=34, font=ctk.CTkFont('Helvetica', 26), text='4',
                         fg_color='#fcfcfc', hover_color='#eaeaea', text_color='#454545', corner_radius=2)
button_5 = ctk.CTkButton(main, width=34, command=lambda: b_5(), height=34, font=ctk.CTkFont('Helvetica', 26), text='5',
                         fg_color='#fcfcfc', hover_color='#eaeaea', text_color='#454545', corner_radius=2)
button_6 = ctk.CTkButton(main, width=34, command=lambda: b_6(), height=34, font=ctk.CTkFont('Helvetica', 26), text='6',
                         fg_color='#fcfcfc', hover_color='#eaeaea', text_color='#454545', corner_radius=2)
button_7 = ctk.CTkButton(main, width=34, command=lambda: b_7(), height=34, font=ctk.CTkFont('Helvetica', 26), text='7',
                         fg_color='#fcfcfc', hover_color='#eaeaea', text_color='#454545', corner_radius=2)
button_8 = ctk.CTkButton(main, width=34, command=lambda: b_8(), height=34, font=ctk.CTkFont('Helvetica', 26), text='8',
                         fg_color='#fcfcfc', hover_color='#eaeaea', text_color='#454545', corner_radius=2)
button_9 = ctk.CTkButton(main, width=34, command=lambda: b_9(), height=34, font=ctk.CTkFont('Helvetica', 26), text='9',
                         fg_color='#fcfcfc', hover_color='#eaeaea', text_color='#454545', corner_radius=2)
button_Eql = ctk.CTkButton(main, width=34, command=lambda: b_Eql(), height=34, font=ctk.CTkFont('Helvetica', 28),
                           text='=', fg_color='#007dfe', hover_color='#0071ea', text_color='white', corner_radius=2)
button_Per = ctk.CTkButton(main, width=34, command=lambda: b_Per(), height=34, font=ctk.CTkFont('Helvetica', 28),
                           text='%', fg_color='#fcfcfc', hover_color='#eaeaea', text_color='#454545', corner_radius=2)
button_Pnt = ctk.CTkButton(main, width=34, command=lambda: b_Pnt(), height=34, font=ctk.CTkFont('Helvetica', 30),
                           text='.', fg_color='#fcfcfc', hover_color='#eaeaea', text_color='#454545', corner_radius=2)
button_Pos = ctk.CTkButton(main, width=34, command=lambda: b_Pos(), height=34, font=ctk.CTkFont('Helvetica', 30),
                           text='+', fg_color='#f5f5f5', hover_color='#b0afac', text_color='#007dfe', corner_radius=2)
button_Neg = ctk.CTkButton(main, width=34, command=lambda: b_Neg(), height=34, font=ctk.CTkFont('Helvetica', 30),
                           text='−', fg_color='#f5f5f5', hover_color='#b0afac', text_color='#007dfe', corner_radius=2)
button_Div = ctk.CTkButton(main, width=34, command=lambda: b_Div(), height=34, font=ctk.CTkFont('Helvetica', 30),
                           text='÷', fg_color='#f5f5f5', hover_color='#b0afac', text_color='#007dfe', corner_radius=2)
button_Mul = ctk.CTkButton(main, width=34, command=lambda: b_Mul(), height=34, font=ctk.CTkFont('Helvetica', 30),
                           text='×', fg_color='#f5f5f5', hover_color='#b0afac', text_color='#007dfe', corner_radius=2)
button_Del = ctk.CTkButton(main, width=34, command=lambda: b_Del(), height=34,
                           font=ctk.CTkFont('Helvetica', 18, weight='bold'),
                           text='⌫', fg_color='#f5f5f5', hover_color='#b0afac', text_color='#007dfe', corner_radius=2)
button_Clr = ctk.CTkButton(main, width=34, command=lambda: b_Clr(), height=34, font=ctk.CTkFont('Helvetica', 25),
                           text='C', fg_color='#f5f5f5', hover_color='#b0afac', text_color='#007dfe', corner_radius=2)

inp = ctk.StringVar(value='')
out = ctk.StringVar(value='')
lab = ctk.CTkLabel(main, textvariable=out, font=ctk.CTkFont('Helvetica', 17), text_color='#454545', padx=12)
lab1 = ctk.CTkLabel(main, textvariable=inp, font=ctk.CTkFont('Helvetica', 35), text_color='#454545', padx=12)
lab.grid(column=0, columnspan=4, row=0, sticky='SE', )
lab1.grid(column=0, columnspan=4, row=1, sticky='E')
button_Clr.grid(column=0, row=2, sticky='NEWS', padx=.4, pady=.4)
button_Del.grid(column=3, row=2, sticky='NEWS', padx=.4, pady=.4)
button_0.grid(column=1, row=6, columnspan=1, sticky='NEWS', padx=.4, pady=.4)
button_1.grid(column=0, row=5, columnspan=1, sticky='NEWS', padx=.4, pady=.4)
button_2.grid(column=1, row=5, columnspan=1, sticky='NEWS', padx=.4, pady=.4)
button_3.grid(column=2, row=5, columnspan=1, sticky='NEWS', padx=.4, pady=.4)
button_4.grid(column=0, row=4, columnspan=1, sticky='NEWS', padx=.4, pady=.4)
button_5.grid(column=1, row=4, columnspan=1, sticky='NEWS', padx=.4, pady=.4)
button_6.grid(column=2, row=4, columnspan=1, sticky='NEWS', padx=.4, pady=.4)
button_7.grid(column=0, row=3, columnspan=1, sticky='NEWS', padx=.4, pady=.4)
button_8.grid(column=1, row=3, columnspan=1, sticky='NEWS', padx=.4, pady=.4)
button_9.grid(column=2, row=3, columnspan=1, sticky='NEWS', padx=.4, pady=.4)
button_Pnt.grid(column=2, row=6, columnspan=1, sticky='NEWS', padx=.4, pady=.4)
# l=0
button_Pos.grid(column=3, row=4, columnspan=1, sticky='NEWS', padx=.4, pady=.4)
button_Neg.grid(column=3, row=3, columnspan=1, sticky='NEWS', padx=.4, pady=.4)
button_Div.grid(column=1, row=2, columnspan=1, sticky='NEWS', padx=.4, pady=.4)
button_Mul.grid(column=2, row=2, columnspan=1, sticky='NEWS', padx=.4, pady=.4)
button_Eql.grid(column=3, row=5, rowspan=2, sticky='NEWS', padx=.4, pady=.4)
button_Per.grid(column=0, row=6, columnspan=1, sticky='NEWS', padx=.4, pady=.4)


def sol():
    global i
    global eq
    temp = ''
    # t1 = []
    for q in eq:
        temp += q
    if len(eq) > 0:
        try:
            ans = eval(temp)
        except:
            ans = 'Math Error'
        eq = list(str(ans))
        i = str(ans)
        return ans


def b_0():
    global i
    global eq
    if inp.get() == '':
        i += '0'
    elif inp.get().find('.') != -1 or inp.get()[0] != '0':
        i += '0'
    elif (inp.get().find('*') != -1 or inp.get().find('+') != -1 or inp.get().find('-') != -1 or inp.get().find(
            '/') != -1 or inp.get().find('%') != -1):
        i += '0'
    elif inp.get()[0] == '0' and len(inp.get()) > 1 and inp.get().find('.') == -1:
        i = i[1::]

    inp.set(i)
    eq.append('0')


def b_1():
    global i
    global eq
    if len(inp.get()) > 0:
        if inp.get()[0] == '0' and len(inp.get()) >= 1 and inp.get().find('.') == -1:
            i = i[1::]
    i += '1'
    inp.set(i)
    eq.append('1')


def b_2():
    global i
    if len(inp.get()) > 0:
        if inp.get()[0] == '0' and len(inp.get()) >= 1 and inp.get().find('.') == -1:
            i = i[1::]
    i += '2'
    inp.set(i)
    eq.append('2')


def b_3():
    global i
    global eq
    if len(inp.get()) > 0:
        if inp.get()[0] == '0' and len(inp.get()) >= 1 and inp.get().find('.') == -1:
            i = i[1::]
    i += '3'
    inp.set(i)
    eq.append('3')


def b_4():
    global i
    if len(inp.get()) > 0:
        if inp.get()[0] == '0' and len(inp.get()) >= 1 and inp.get().find('.') == -1:
            i = i[1::]
    i += '4'
    inp.set(i)
    eq.append('4')


def b_5():
    global i
    global eq
    if len(inp.get()) > 0:
        if inp.get()[0] == '0' and len(inp.get()) >= 1 and inp.get().find('.') == -1:
            i = i[1::]
    i += '5'
    inp.set(i)
    eq.append('5')


def b_6():
    global i
    if len(inp.get()) > 0:
        if inp.get()[0] == '0' and len(inp.get()) >= 1 and inp.get().find('.') == -1:
            i = i[1::]
    i += '6'
    inp.set(i)
    eq.append('6')


def b_7():
    global i
    if len(inp.get()) > 0:
        if inp.get()[0] == '0' and len(inp.get()) >= 1 and inp.get().find('.') == -1:
            i = i[1::]
    i += '7'
    inp.set(i)
    eq.append('7')


def b_8():
    global i
    global eq
    if len(inp.get()) > 0:
        if inp.get()[0] == '0' and len(inp.get()) >= 1 and inp.get().find('.') == -1:
            i = i[1::]
    i += '8'
    inp.set(i)
    eq.append('8')


def b_9():
    global i
    global eq
    if len(inp.get()) > 0:
        if inp.get()[0] == '0' and len(inp.get()) >= 1 and inp.get().find('.') == -1:
            i = i[1::]
    i += '9'
    inp.set(i)
    eq.append('9')


def b_Neg():
    global i

    global eq
    i += '−'
    inp.set(i)
    eq.append('-')


def b_Pos():
    global i
    global eq

    i += '+'
    inp.set(i)
    eq.append('+')


def b_Mul():
    global i
    global eq

    i += '×'
    inp.set(i)
    eq.append('*')


def b_Div():
    global i
    global eq
    i += '÷'
    inp.set(i)
    eq.append('/')


def b_Pnt():
    global i
    global eq

    i += '.'
    inp.set(i)
    eq.append('.')


def b_Clr():
    global i

    global o
    global eq
    i = o = ''
    inp.set(i)
    out.set(o)
    eq.clear()


def b_Eql():
    global i
    global o
    global eq

    i, o = '', i
    inp.set(sol())
    out.set(o)


def b_Per():
    global i
    global eq
    i += '%'
    inp.set(i)
    eq.append('/100')


def b_Del():
    global i
    global eq
    try:
        i = i[0:-1]
        inp.set(i)
        eq.pop(-1)
    except:
        pass


main.mainloop()
