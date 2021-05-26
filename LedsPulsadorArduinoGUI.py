import pyfirmata
import tkinter as tk

#contador inicia en 0
count=0
#Conexion con la placa arduino
PlacaMega= pyfirmata.Arduino('COM3')
#Activar arduino para ingreso de datos
IngresoDatos = pyfirmata.util.Iterator(PlacaMega)
#Iniciar
IngresoDatos.start()
#Pin para ingreso de datos
PinEntrada=PlacaMega.digital[10]
#Activar el pin para entrada
PinEntrada.mode = pyfirmata.INPUT

#Botones de control de Leds funciones
def LedAzulON():
    print("Encender Led Azul")
    PlacaMega.digital[7].write(1)
def LedAzulOFF():
    print("Apagar Led Azul")
    PlacaMega.digital[7].write(0)
def LedVerdeON():
    print("Encender Led Verde")
    PlacaMega.digital[6].write(1)
def LedVerdeOFF():
    print("Apagar Led Verde")
    PlacaMega.digital[6].write(0)
#Contador de veces pulsadas
def Pulsador():
  #Recursividad para volver a iniciar la funcion en el mainloop
  ventana.after(200, Pulsador)
  #Lectura del pin de entrada
  SalidaPulsador = PlacaMega.digital[10].read()
  #Datos de ingreso condicional
  if SalidaPulsador is True:
    #Enciende el LED de la placa y cuenta el numero de veces presionadas
    global count
    count = count + 1
    print(count)
    PlacaMega.digital[13].write(1)
    print("Pulsador ON")
    label = tk.Label(ventana, text="Número de veces presionadas:" + str(count), font=("Arial", 30), fg="white",
                     bg="black").place(x=10, y=100)
  else:
    #Apaga el Led de la placa
    PlacaMega.digital[13].write(0)
    print("Pulsador OFF")


#iniciar la pantalla
ventana=tk.Tk()
#Titulo de la pantalla
ventana.title("CONTADOR Y ENCENDIDO DE LED")
#dimensiones de la pantalla
ventana.geometry("610x610")
#Ccambio de color se pone el codigo hexadecimal
ventana.configure(background="#808b96")
#contador=Text(ventana)


#Titulo de contador
etiqueta = tk.Label(ventana, text="CONTADOR DE PULSADOR ",font=("Arial",20),bg="#d1214c").place(x=120,y=20)
#Titulo de led
etiqueta1 = tk.Label(ventana, text="CONTROL DE LEDS ",font=("Arial",20),bg="#53b62e").place(x=150,y=180)
#boton led azul encendido
b1=tk.Button(ventana,text="LED AZUL ON",activebackground="#333fff",bd=5,padx=70,pady=50,command=LedAzulON).place(x=40,y=250)
#boton led azul encendido
b2=tk.Button(ventana,text="LED AZUL OFF",activebackground="#333fff",bd=5,padx=70,pady=50,command=LedAzulOFF).place(x=320,y=250)
#botom led verde encendido
b3=tk.Button(ventana,text="LED VERDE ON",activebackground="#39b11e",bd=5,padx=70,pady=50,command=LedVerdeON).place(x=40,y=420)
#botom led verde encendido
b4=tk.Button(ventana,text="LED VERDE OFF",activebackground="#39b11e",bd=5,padx=70,pady=50,command=LedVerdeOFF).place(x=320,y=420)
#Contador de pulso inicia en 0
label = tk.Label(ventana, text="Número de veces presionadas:0",font=("Arial",30), fg="white", bg="black").place(x=10,y=100)

#tiempo para enviar a la funcion
ventana.after(200,Pulsador)
ventana.mainloop()



