from tkinter import *
#import modulos

#funcion inserta elemento en un caja de texto
def listar(fin):
    agenda = open("agendatelefonica.csv")
    numero = 0
    for i in range(0,fin):
        lectura = agenda.readline()
        #print(lectura.replace(",","\t\t"))
        lista.insert(END,lectura.replace(",","  "))
        numero = numero + 1
    agenda.close()

#ventana contenedora
f = Frame(width=300,height=300)
f.pack(padx=15,pady=15)

#cargar imagen
img = PhotoImage(file="Bart.gif")
logo = Label(f,image=img)
logo.pack(side=TOP,padx=10,pady=10)

#f variable del contenedor fg color font fuentes
titulo = Label(f,text="Agenda Telefonica V1.0",fg="black",font=("Arial",24))
titulo.pack(side=TOP,padx=10,pady=10)

autor = Label(f,text="Developer: Juan Manuel Chaguendo")
autor.pack(side=TOP,padx=10,pady=10)

#botones y eventos(command mas lambda permite pasar parametros al metodo de otro modulo)
#Entry.get() obtiene el dato de un input
""" btn2 para salir de la app de manera facil"""
btn2 = Button(f,text="salir",command=quit)
btn2.pack(side=BOTTOM,padx=10,pady=10)

btn1 = Button(f,text="Listar Elementos",command=lambda:listar(int(Entry.get(campo))))
btn1.pack(side=BOTTOM,padx=10,pady=10)

#campos de Entrada
campo = Entry(f,textvariable=5)
campo.pack(side=TOP,padx=10,pady=10)

#campos de lista
lista =Listbox(f)
lista.pack(side=TOP,padx=20,pady=10)
