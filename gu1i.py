#from tkinter import *
import tkinter as tk
#import modulos

#funcion inserta elemento en un caja de texto
def listar(fin):
    agenda = open("agendatelefonica.csv")
    numero = 0
    for i in range(0,fin):
        lectura = agenda.readline()
        #print(lectura.replace(",","\t\t"))
        lista.insert(tk.END,lectura.replace(",","  "))
        numero = numero + 1
    agenda.close()

#ventana contenedora
f =tk.Frame(width=300,height=300)
f.pack(padx=15,pady=15)

#cargar imagen
img = tk.PhotoImage(file="Bart.gif")
logo = tk.Label(f,image=img)
logo.pack(side=tk.TOP,padx=10,pady=10)

#f variable del contenedor fg color font fuentes
titulo =tk. Label(f,text="Agenda Telefonica V1.0",fg="black",font=("Arial",24))
titulo.pack(side=tk.TOP,padx=10,pady=10)

autor = tk.Label(f,text="Developer: Juan Manuel Chaguendo")
autor.pack(side=tk.TOP,padx=10,pady=10)

#botones y eventos(command mas lambda permite pasar parametros al metodo de otro modulo)
#Entry.get() obtiene el dato de un input,   buton 2 de salir  28/2/20 x guille

btn2 = tk.Button(f,text="salir",command=quit)
btn2.pack(side=tk.BOTTOM,padx=10,pady=10)

btn1 =tk.Button(f,text="Listar Elementos",command=lambda:listar(int(tk.Entry.get(campo))))
btn1.pack(side=tk.BOTTOM,padx=10,pady=10)




#campos de Entrada
campo = tk.Entry(f,textvariable=5)
campo.pack(side=tk.TOP,padx=10,pady=10)

#campos de lista
lista =tk.Listbox(f)
lista.pack(side=tk.TOP,padx=20,pady=10)
