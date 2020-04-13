#Jose Antonio Rojas Quispe
import tkinter as tk
root = tk.Tk()

numero1 = tk.StringVar()
numero2 = tk.StringVar()
mensaje = tk.StringVar()

def sumar():
    s = int(numero1.get()) + int(numero2.get())
    mensaje.set(s)
    numero1.set('')
    numero2.set('')


def restar():
    s = int(numero1.get()) - int(numero2.get())
    mensaje.set(s)
    numero1.set('')
    numero2.set('')


def multiplicar():
    s = int(numero1.get()) * int(numero2.get())
    mensaje.set(s)
    numero1.set('')
    numero2.set('')

def dividir():
    try:
        s = int(numero1.get()) / int(numero2.get())
        mensaje.set(s)
        numero1.set('')
        numero2.set('')
    except ZeroDivisionError:
        mensaje.set("Syntax error ")
        numero1.set('')
        numero2.set('')


root.geometry('600x400')
root.title('CALCULADORA')

root.config(bg='grey')

tk.Label(root, text='CALCULADORA', bg="grey" , fg='white',font=('', 20)).place(x=200, y = 10)

#ingrese un numero
tk.Label(root, text='Ingrese un numero', bg="grey" , fg='white',font=('', 17)).place(x=10, y = 100)
tk.Entry(root, justify='center',textvariable=numero1).place(x=230, y=110)

#ingrese otro numero
tk.Label(root, text='Ingrese otro numero', bg="grey" , fg='white',font=('', 17)).place(x=10, y = 200)
tk.Entry(root, justify='center',textvariable=numero2).place(x=230, y=210)

#sumar
tk.Button(root, text='sumar', bd=0,font=('', 13), command=sumar).place(x=400, y=100)

#restar
tk.Button(root, text='restar', bd=0,font=('', 13), command=restar).place(x=500, y=100)

#multiplicar
tk.Button(root, text='multiplicar', font=('', 13), bd=0, command=multiplicar).place(x=400, y=200)

#dividir
tk.Button(root, text='dividir', bd=0, font=('', 13), command=dividir).place(x=500, y=200)


tk.Label(root,text ='Resultado',bg="grey" ,fg='white', font=('',20)).place(x=250 , y=250)
tk.Label(root,textvariable =mensaje,bg="grey" , fg='white',font=('', 30)).place(x=275 , y=280)
tk.Button(root, text='SALIR', bd=0, font=('', 13), command=root.destroy).place(x=270, y=350)


root.mainloop()