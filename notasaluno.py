import PySimpleGUI as sg

class TelaBoletimEscola:
    def __init__(self):
        # Defina o tema para 'DarkBlue17'
        sg.theme('DarkBlue17')

        # Defina o layout da janela
        layout = [[]]

        # Crie a janela
        self.window = sg.Window('Tela Vazia', layout, size=(600, 450))

    def iniciar(self):
        # Loop de eventos para manter a janela aberta
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
        self.window.close()


# Feche a janela ao sair do loop
if __name__ == "__main__":
    tela_boletim_escola = TelaBoletimEscola()
    tela_boletim_escola.iniciar()
