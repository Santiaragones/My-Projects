from tkinter import *

raiz=Tk()

miFrame=Frame(raiz)
miFrame.pack()

#-----------------------variables-------------------------
signoDelBoton=StringVar() #numeroPantalla

operacion=""

resultado=0

reset_pantalla=False

#---------------------funciones--------------------

def textoBoton(num):

	global operacion

	if operacion!="":
		signoDelBoton.set(num)

		operacion=""

	else:

		signoDelBoton.set(signoDelBoton.get() + num)

def suma(num):
	
	global operacion

	global resultado

	resultado+=int(num)

	operacion="suma"

	signoDelBoton.set(resultado)


def el_resultado():

	global resultado

	signoDelBoton.set(resultado+int(signoDelBoton.get()))

	resultado=0


#-------------------pulsaciones teclado--------------------------

def textoBoton(num):

	global operacion

	global reset_pantalla

	if reset_pantalla!=False:

		signoDelBoton.set(num)

		reset_pantalla=False

	else:
	
		signoDelBoton.set(signoDelBoton.get() + num)


#-----------------------pantalla--------------------------
pantalla=Entry(miFrame, textvariable=signoDelBoton)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="black", fg="#03f943", justify="right") #color codigo desde photoshop

#--------------------------fila 1----------------------------------

botonBorrar=Button(miFrame, text="CE", width=3)
botonBorrar.grid(row=2, column=1)

#--------------------------fila 2----------------------------------
boton7=Button(miFrame, text="7", width=3, command=lambda:textoBoton("7"))
boton7.grid(row=3, column=1)

boton8=Button(miFrame,text="8", width=3, command=lambda:textoBoton("8"))
boton8.grid(row=3, column=2)

boton9=Button(miFrame,text="9", width=3, command=lambda:textoBoton("9"))
boton9.grid(row=3, column=3)

botonDiv=Button(miFrame,text="/", width=3)
botonDiv.grid(row=3, column=4)

#--------------------------fila 3----------------------------------
boton4=Button(miFrame, text="4", width=3, command=lambda:textoBoton("4"))
boton4.grid(row=4, column=1)

boton5=Button(miFrame,text="5", width=3, command=lambda:textoBoton("5"))
boton5.grid(row=4, column=2)

boton6=Button(miFrame,text="6", width=3, command=lambda:textoBoton("6"))
boton6.grid(row=4, column=3)

botonMult=Button(miFrame,text="x", width=3)
botonMult.grid(row=4, column=4)

#--------------------------fila 4----------------------------------
boton1=Button(miFrame, text="1", width=3, command=lambda:textoBoton("1"))
boton1.grid(row=5, column=1)

boton2=Button(miFrame,text="2", width=3, command=lambda:textoBoton("2"))
boton2.grid(row=5, column=2)

boton3=Button(miFrame,text="3", width=3, command=lambda:textoBoton("3"))
boton3.grid(row=5, column=3)

botonRest=Button(miFrame,text="-", width=3,)
botonRest.grid(row=5, column=4)

#--------------------------fila 5----------------------------------
boton0=Button(miFrame, text="0", width=3, command=lambda:textoBoton("0"))
boton0.grid(row=6, column=1)

botonComa=Button(miFrame,text=",", width=3, command=lambda:textoBoton(","))
botonComa.grid(row=6, column=2)

botonIgual=Button(miFrame,text="=", width=3, command=lambda:el_resultado())
botonIgual.grid(row=6, column=3)

botonSuma=Button(miFrame,text="+", width=3, command=lambda:suma(signoDelBoton.get()))
botonSuma.grid(row=6, column=4)








raiz.mainloop()