import tkinter as tk
from tkinter import *
#from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


import numpy as np 
import control as co


#from control.matlab import * #a biblioteca de controle tem dois tipos de sintaxe, nesse script utilizaremos a que se
import matplotlib.pyplot as plt #parece com a do matlab.
import numpy as np

cplr = np.array([ 0.01828922,  0.01972157,  0.02342053, 0.25928021, 0.26352547,  0.26883406])

def limparString(original_string, characters_to_remove):
    new_string = original_string
    for character in characters_to_remove:
        new_string = new_string.replace(character, characters_to_remove)
    
    return new_string


def FunBotao1(FuncaoControlador):
    print(FuncaoControlador)
    print(type(FuncaoControlador))

    x,y = FuncaoControlador.split(';')
    print(x)
    print(type(x))
    print(y)
    print(type(y))

    x = np.fromstring(x, dtype=int, sep = ',')
    y = np.fromstring(y, dtype=int, sep = ',')
    print(x)
    print(type(x))
    print(y)
    print(type(y))

    
    G1 = co.tf(x, y)
    print(G1)
    G1

    t = np.linspace(0, 10, 100)
    t1, y1 = co.impulse_response(G1,t)



    plt.plot(t1, y1)
    plt.xlabel('time(s)')
    plt.ylabel('amplitude')
    plt.grid()
    plt.show()


def FunBotao2(FuncaoPlanta):
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show();

def FunBotao3(FuncaoSensor):
    print(FuncaoSensor)
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()
    
window = tk.Tk()
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
