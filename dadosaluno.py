import PySimpleGUI as sg
import aluno

class TelaDadosAluno:
    def __init__(self):
        # Defina o tema para 'DarkBlue17'
        sg.theme('DarkBlue17')

        font_size = ('Helvetica', 12)

        # Defina o layout da janela
        layout_1 = [
            [
                [sg.Text('Dados Pessoais', font=('Helvetica', 20), justification='center')],
                [sg.Frame('Informações',
                          [
                              [sg.Text('Nome Completo: Anderson Freiras ', font=font_size)],
                              [sg.Text('Turma: 8', font=font_size)],
                              [sg.Text('CPF: 431.345.034-52', font=font_size)],
                          ]
                          )],
                [sg.Frame('Horários e Disciplinas',
                          [
                              [sg.Text('     Dias:                  | Segunda-feira | Terça-feira | Quarta-feira | Quinta-feira | Sexta-feira', font=font_size)],
                              [sg.Text('8:00 - 9:30:             | Matemática      | Português  | História        | Matemática | Geografia', font=font_size)],
                              [sg.Text('9:30 - 11:00:           | Inglês                | Redação    |  Literatura    | Física           | Matemática', font=font_size)],
                              [sg.Text('11:00 - 12:00:         | Química            | Sociologia | Filosofia      | Artes             | Biologia', font=font_size)],
                              [sg.Text('12:00 - 13:00:         | Intervalo            | Intervalo     | Intervalo       | Intervalo        | Intervalo', font=font_size)],
                              [sg.Text('13:00 - 14:00:         | Matemática      | Biologia     | Física          | História         | Geografia', font=font_size)],
                              [sg.Text('14:00 - 15:00:         | Informática       | Literatura    | Interp. Tex. | Ed. Física     | Física', font=font_size)],
                              [sg.Text('15:00 - 16:00:         | Biologia            | Artes          | Inglês           | Química        | História ', font=font_size)],
                          ]
                          )]
            ]
        ]

        layout_botao = [
            [sg.Push(),sg.Button('Voltar', button_color=('white', 'red'), size=(6, 1), key='-VOLTAR-')]
        ]

        # Combine os layouts
        layout_final = layout_1 + layout_botao

        # Crie a janela
        self.window = sg.Window('Dados do Aluno', layout_final, size=(800, 500))

        # Loop de eventos para manter a janela aberta

    def iniciar(self):
        while True:
            event, values = self.window.read()
            if event == '-VOLTAR-':
                self.window.close()
                tela_aluno_escola = aluno.TelaAlunoEscola()
                tela_aluno_escola.iniciar()

            if event == sg.WIN_CLOSED:
                break

        self.window.close()

if __name__ == "__main__":
    tela_dados_aluno = TelaDadosAluno()
    tela_dados_aluno.iniciar()