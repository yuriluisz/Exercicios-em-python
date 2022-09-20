import PySimpleGUI as sg
import random as random

sg.theme('BluePurple')
layout = [[sg.Text('O resultado do sorteio aparecera aqui: '), sg.Text(size=(15,1), key='sorteado')],
          [sg.Text("Numero de alunos PRESENTES:"),sg.Input(key="num")],
          [sg.Text("Insira os nomes dos alunos:"),sg.Input(key="nom")],
          [sg.Button("Nomes"),sg.Button("Sortear!"), sg.Button("Sair")]]

window = sg.Window("Sorteador foda", layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WINDOW_CLOSED or "Sair":
        break
    if event == "Nomes":
        sg.Popup("sexo")
        #sg.popup(sg.Text("Insira um nome:"),sg.Input(key="Nomes"))

window.close()