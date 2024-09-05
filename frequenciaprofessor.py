import PySimpleGUI as sg

# Defina o tema para 'DarkBlue17'
sg.theme('DarkBlue17')

# Defina o layout da janela
layout = [[]]

# Crie a janela
window = sg.Window('Tela Vazia', layout, size=(600, 450))

# Loop de eventos para manter a janela aberta
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

# Feche a janela ao sair do loop
window.close()
