import tkinter 
from tkinter import window, button, 

#from control.matlab import * #a biblioteca de controle tem dois tipos de sintaxe, nesse script utilizaremos a que se
import matplotlib.pyplot as plt #parece com a do matlab.
import numpy as np


import matplotlib.pyplot as plt #parece com a do matlab.

def FunBotao1(FuncaoControlador):
    print(FuncaoControlador)

def FunBotao2(FuncaoPlanta):
    print(FuncaoPlanta)

def FunBotao3(FuncaoSensor):
    print(FuncaoSensor)

window = tkinter.Tk()
window.title("Programa de Simulação")
window.minsize("800","450")

window.resizable(False, False)

Imagem = PhotoImage(file= "control.png")
label = Label(window, image = Imagem)
label.pack()

Controlador = Label(window, text = "Código do Controlador")
Controlador.place(x= 10, y = 275)

ControladorInput = StringVar()
ControladorInput = Entry(window, textvariable = ControladorInput)
ControladorInput.place(x= 150, y = 275)

Planta = Label(window, text = "Código da Planta")
Planta.place(x= 300, y = 275)

PlantaInput = StringVar()
PlantaInput = Entry(window, textvariable = PlantaInput)
PlantaInput.place(x= 400, y = 275)

Sensor = Label(window, text = "Código do Sensor")
Sensor.place(x= 560, y = 275)

SensorInput = StringVar()
SensorInput = Entry(window, textvariable = SensorInput)
SensorInput.place(x= 660, y = 275)

Botao1 = Button(window,text="Botao 1", command = lambda: FunBotao1(ControladorInput.get()))
Botao1.place(x= 200, y = 350)

Botao2 = Button(window,text="Botao 2", command = lambda: FunBotao2(PlantaInput.get()))
Botao2.place(x= 400, y = 350)

Botao3 = Button(window,text="Botao 3", command = lambda: FunBotao3(SensorInput.get()))
Botao3.place(x= 600, y = 350)

window.mainloop()