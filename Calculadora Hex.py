from tkinter import *
from tkinter import messagebox

ventana =Tk()
ventana.title("calculadora")
ventana.configure(bg="black")


#entrada
e_texto = Entry(ventana, font = ("Calibri 30"))
e_texto.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady=5)

i = 0
def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def borrar():
    e_texto.delete(0,END)
    i = 0
    
def opercacion():
    ecuacion = e_texto.get()
    resulado = eval(ecuacion)
    e_texto.delete(0,END)
    e_texto.insert(0,resulado)

def borrar2 ():
    global i
    i = i-1
    e_texto.delete(i,END)
    
def convertir_hexadecimal():
    try:
        ecuacion = e_texto.get()
        resultado_decimal = eval(ecuacion)
        resultado_hexadecimal = hex(int(resultado_decimal))
        e_texto.delete(0, END)
        e_texto.insert(0, resultado_hexadecimal.upper())
        global i
        i = 0
    except Exception as e:
        messagebox.showerror("Error", "¡SOLO PUEDES AGREGAR NUMEROS!")
        


boton1 = Button(ventana, text="1", width=5, height=2, command=lambda:click_boton(1), bg="turquoise")
boton2 = Button(ventana, text="2", width=5, height=2, command=lambda:click_boton(2), bg="turquoise")
boton3 = Button(ventana, text="3", width=5, height=2, command=lambda:click_boton(3), bg="turquoise")
boton4 = Button(ventana, text="4", width=5, height=2, command=lambda:click_boton(4), bg="turquoise")
boton5 = Button(ventana, text="5", width=5, height=2, command=lambda:click_boton(5), bg="turquoise")
boton6 = Button(ventana, text="6", width=5, height=2, command=lambda:click_boton(6), bg="turquoise")
boton7 = Button(ventana, text="7", width=5, height=2, command=lambda:click_boton(7), bg="turquoise")
boton8 = Button(ventana, text="8", width=5, height=2, command=lambda:click_boton(8), bg="turquoise")
boton9 = Button(ventana, text="9", width=5, height=2, command=lambda:click_boton(9), bg="turquoise")
boton0 = Button(ventana, text="0", width=13, height=2, command=lambda:click_boton(0), bg="turquoise")

boton_borrar = Button(ventana, text="AC", width=5, height=2, command=lambda:borrar(), bg="red")
boton_Parentesis1 = Button(ventana, text="(", width=5, height=2, command=lambda:click_boton("("), bg="green")
boton_Parentesis2 = Button(ventana, text=")", width=5, height=2, command=lambda:click_boton(")"), bg="green")
boton_Punto = Button(ventana, text=".", width=5, height=2, command=lambda:click_boton("."))

boton_div = Button(ventana, text="/", width=5, height=2, command=lambda:click_boton("/"), bg="green")
boton_mult = Button(ventana, text="x", width=5, height=2, command=lambda:click_boton("*"), bg="green")
boton_suma = Button(ventana, text="+", width=5, height=2, command=lambda:click_boton("+"), bg="green")
boton_resta = Button(ventana, text="-", width=5, height=2, command=lambda:click_boton("-"), bg="green")
boton_igual = Button(ventana, text="=", width=5, height=2, command=lambda:opercacion())
boton_borrar2 = Button(ventana, text= "<-", width=5, height=2, command=lambda:borrar2(), bg="red")
boton_hex= Button(ventana, text=("HEX"), width=5, height=2, command=lambda: convertir_hexadecimal())

#asignamos colocacion de elementos en ventana

boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_Parentesis1.grid(row=1, column=1, padx=5, pady=5)
boton_Parentesis2.grid(row=1, column=2, padx=5, pady=5)
boton_div.grid(row=1, column=3, padx=5, pady=5)
boton_borrar2.grid(row=1, column=4, padx=5, pady=5)


boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_mult.grid(row=2, column=3, padx=5, pady=5)
boton_hex.grid(row=2, column=4, padx=5, pady=5 )

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_suma.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_resta.grid(row=4, column=3, padx=5, pady=5)

boton0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
boton_Punto.grid(row=5, column=2, padx=5, pady=5)
boton_igual.grid(row=5, column=3, padx=5, pady=5)


ventana.mainloop()