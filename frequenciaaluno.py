import PySimpleGUI as sg
import aluno

class TelaFrequenciaEscola:
    def __init__(self):
        sg.theme('DarkBlue17')

        font_size = ('Helvetica', 12)

        # Defina o layout da janela
        layout_1 = [
            [
                [sg.Text('Frequência', font=('Helvetica', 20), justification='center')],
                [sg.Text('Anderson Freiras', font=('Helvetica', 15), justification='center')],
                sg.Frame('Frequência',
                          [
                              [sg.Text('Dias Letivos no ano: 180   Faltas totais até o momento: 4/27', font=font_size)],
                              [sg.Text('1º BIMESTRE: 2 FALTAS ', font=font_size)],
                              [sg.Text('2º BIMESTRE: 0 FALTAS ', font=font_size)],
                              [sg.Text('3º BIMESTRE: 2 FALTAS ', font=font_size)],
                              [sg.Text('4º BIMESTRE: - FALTAS ', font=font_size)],
                              [sg.Text('Porcentagem de faltas até o momento: 2,5% / 15%', font=font_size)]
                          ]
                )
            ]
        ]

        layout_botao = [
            [sg.Push(),sg.Button('Voltar', button_color=('white', 'red'), size=(6, 1), key='-VOLTAR-')]
        ]

        # Combine os layouts
        layout_final = layout_1 + layout_botao

        # Crie a janela
        self.window = sg.Window('Dados do Aluno', layout_final, size=(600, 450))

    def iniciar(self):

        # Loop de eventos para manter a janela aberta
        while True:
            event, values = self.window.read()
            if event == ('-VOLTAR-'):
                self.window.close()
                tela_aluno_escola = aluno.TelaAlunoEscola()
                tela_aluno_escola.iniciar()
            if event == sg.WIN_CLOSED:
                break

        # Feche a janela ao sair do loop
        self.window.close()

if __name__ == "__main__":
    tela_frequencia_aluno = TelaFrequenciaEscola()
    tela_frequencia_aluno.iniciar()

