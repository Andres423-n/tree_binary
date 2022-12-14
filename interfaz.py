from tkinter import *
import heapq
import graphviz

    

list = [] #creacion de lista para agregar nodos de arbol
ventana= Tk() #ventana pricipal de tkinter
ventana.title("Tree Heap")
ventana.geometry("600x280+520+250")#geometry da tamaño a nuestra ventana
ventana.resizable(0,0)

ventana.config(bg="black")#color a ventana
menuBar = Menu(ventana)#creamos nuestra variable de menu
ventana.config(menu=menuBar)#le damos la configuracion de menu a la variable

#agregar imagenes 
AgregarImg = PhotoImage(file ="Agregar.png")
EliminarImg = PhotoImage(file ="Eliminar.png")
GraficarImg = PhotoImage(file ="Graficar.png")
FondoImg = PhotoImage(file ="FondoBinary.png")
TreeIcon = PhotoImage(file ="TreeIcon.png")


lblFondo=Label(ventana,image=FondoImg,bd=0).place(x=300,y=50)
lblTreeIcon=Label(ventana,image=TreeIcon,bd=0).place(x=140,y=25)



#funcion encargada de agregar los datos a la lista utilizando el metodo de monticulos
def agregar_lista():
    numero = num.get()
    heapq.heappush(list,numero)
    imprimir2.config(text=list)
    entrada1.delete(0,"end")
    graficar()


#funcion para eliminar utilizando el metodo de monticulos
def eliminarD():
    heapq.heappop(list)
    imprimir2.config(text =list)
    graficar()

#funcion encargada de graficar utilizando graphviz
def graficar():
    d = graphviz.Digraph(filename='Graphics.gv')
    
    long = len(list)
    print(list)
    key = 0
    cont = 1
    #ciclo encargado de conectar los nodos utilizando .edge el cual es una funcion de graphviz
    while cont < long:
        d.edge(str(list[key]),str(list[cont]))
        if cont % 2 == 0:
            key = key + 1
        cont = cont + 1
    d.view()
                        
heapq.heapify(list) #ordenamiento de datos mediante el metodo de monticulos

num =IntVar()


#etiquetas de texto 

etiqueta = Label(ventana, text="Andres Marin",bd=2, bg="black",fg="white")
etiqueta.place(x=210,y=290)

etiqueta1 = Label(ventana ,  text= "Binary Heap", bg="Black",  bd=0,fg="Green",font="Courier 15")
etiqueta1.place(x=100 , y=85)

etiqueta01 = Label(ventana ,  text= "List[", bg="Black",  bd=0,fg="Green",font="Courier 15")
etiqueta01.place(x=40 , y=230)

# entrada de texto el cual tiene asiganada una variable llamda num
entrada1 =  Entry(ventana, bd=4,textvariable=num)
entrada1.place(x= 100, y=130)
entrada1.delete(0,"end")

#boton encargado de agregar nodos al arbol
Agregar = Button(ventana, image=AgregarImg, command= agregar_lista, bg="black", bd=0)
Agregar.place(x=110, y=170)


EliminarNodo = Button(ventana, image=EliminarImg,command=eliminarD, bg="black", bd=0)
EliminarNodo.place(x=200,y=170)


imprimir = Label(ventana , bg ="black", fg="red", font="Courier 10")
imprimir.place(x=100,y=227)

imprimir.config(font="calibri")

imprimir2 = Label(ventana , bg ="black", fg="red", font="Courier 10")
imprimir2.place(x=100,y=227)
imprimir2.config(font="calibri")

ventana.mainloop()
