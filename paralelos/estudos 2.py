import PySimpleGUI as sg

sg.theme("DarkBlue 3")
layout = [sg.Text("Insira seu nome: "),sg.Input(key="nome"),
          sg.Text("Insira sua senha: "),sg.Input(key="senha")]
window = sg.Window("Tela foda", layout)

eevent
