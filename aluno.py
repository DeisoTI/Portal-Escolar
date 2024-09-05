import PySimpleGUI as sg

import dadosaluno
import frequenciaaluno
import login
import notasaluno


class TelaAlunoEscola:
    def __init__(self):
        # Define o tema
        sg.theme('DarkBlue17')

        font_size = ('Helvetica', 12)

        # Define a interface gráfica
        layout_esquerda = [
            [sg.Text('Aluno', font=('Helvetica', 20), justification='center')],
            [sg.Text('Seja bem-vindo!', font=('Helvetica', 13), text_color='LightGreen')],

            [sg.Button('Boletim', size=(10, 2), font=font_size, key='-BOLETIM-')],
            [sg.Button('Frequência', size=(10, 2), font=font_size, key='-FREQUENCIA-')],
            [sg.Button('Dados Pessoais', size=(10, 2), font=font_size, key='-DADOSPESSOAIS-')],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Button('Log out', button_color=('white', 'red'), size=(6, 1), pad=(10, 10), key='-LOGOUT-')]
        ]

        layout_direita = [
            [sg.Text(''), sg.Image('logo2.png', pad=(0, (0, 50)))],
            [sg.Text('')],
            [sg.Text('')]
        ]

        layout = [

            [sg.Column(layout_esquerda), sg.Column(layout_direita)]

        ]

        # Cria a janela
        self.window = sg.Window('Minha Aplicação', layout, size=(600, 450))

    def iniciar(self):
        # Loop de eventos
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break
            if event == '-LOGOUT-':
                self.window.close()
                tela_login_escola = login.TelaLoginEscola()
                tela_login_escola.iniciar()
            if event == '-BOLETIM-':
                self.window.close()
                tela_boletim_escola = notasaluno.TelaBoletimEscola()
                tela_boletim_escola.iniciar()
            if event == '-FREQUENCIA-':
                self.window.close()
                tela_frequencia_escola = frequenciaaluno.TelaFrequenciaEscola()
                tela_frequencia_escola.iniciar()
            if event == '-DADOSPESSOAIS-':
                self.window.close()
                tela_dados_aluno = dadosaluno.TelaDadosAluno()
                tela_dados_aluno.iniciar()



            # Fecha a janela ao sair do loop
            self.window.close()


if __name__ == "__main__":
    tela_aluno = TelaAlunoEscola()
    tela_aluno.iniciar()
