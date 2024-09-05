import PySimpleGUI as sg
from Autenticador import Autenticador
import professor #trocar pelo nome do arquivo da tela de professor
import aluno
# import teste_aluno #trocar pelo nome do arquivo da tela de aluno

autenticador = Autenticador()


def autenticar_usuario(tipo_usuario, nome, cpf):
    if autenticador.autenticar(nome, cpf):
        sg.popup_ok(f"{tipo_usuario.capitalize()} autenticado!")
        return True
    else:
        sg.popup_error(f"Autenticação falhou para {tipo_usuario.capitalize()}.")
        return False


class TelaLoginEscola:
    def __init__(self):

        # Cor da janela
        sg.theme('DarkBlue17')

        # Texto no topo da tela
        layout_vazio2 = [
            [sg.Text('       ')],
            [sg.Text('       ')],
        ]

        layout_login_text = [
            [sg.Text('Colégio Nicolau Maquiavel', font=('Times New Roman', 35), justification='center')],
            [sg.Text('Login', font=('Helvetica', 15), justification='center')],
        ]

        # Layout para a aba Aluno
        layout_aluno = [
            [sg.Text('                                                    '),
             sg.Image(filename='aluno.png', size=(110, 110))],
            [sg.Text('   Nome Completo:', size=(15, 1), pad=(0, 5)), sg.InputText(key='-ALUNO_NOME-')],
            [sg.Text('         Matrícula:', size=(15, 1), pad=(0, 5)), sg.InputText(key='-ALUNO_CPF-', password_char='*')],
            [sg.Button('Entrar', button_color=('white', 'green'), size=(70, 1), key='-ENTRAR_ALUNO-')]
        ]

        # Layout para a aba Professor
        layout_professor = [
            [sg.Text('                                                    '),
             sg.Image(filename='professor.png', size=(110, 110))],
            [sg.Text('   Nome Completo:', size=(15, 1), pad=(0, 5)), sg.InputText(key='-PROFESSOR_NOME-')],
            [sg.Text('            CPF:', size=(15, 1), pad=(0, 5)), sg.InputText(key='-PROFESSOR_CPF-', password_char='*')],
            [sg.Button('Entrar', button_color=('white', 'green'), size=(70, 1), key='-ENTRAR_PROFESSOR-')]
        ]

        layout_vazio = [
            [sg.Text('       ')],
        ]

        # Layout principal com sg.TabGroup
        layout = [
            [sg.Column(layout_vazio2)],
            [sg.Column(layout_login_text)],
            [sg.Column(layout_vazio)],
            [sg.TabGroup([
                [sg.Tab('Aluno', layout_aluno),
                 sg.Tab('Professor', layout_professor)]
            ], key='-TABS-')],
        ]

        # Janela
        self.window = sg.Window('Portal Acadêmico', layout, size=(600, 500))

    def iniciar(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == '-ENTRAR_ALUNO-':
                tipo_usuario = 'aluno'
                nome = values['-ALUNO_NOME-']
                cpf = values['-ALUNO_CPF-']

                if autenticar_usuario(tipo_usuario, nome, cpf):
                    self.window.close()
                    tela_aluno_escola = aluno.TelaAlunoEscola()
                    tela_aluno_escola.iniciar()
                    # Exemplo: TelaAluno().iniciar(), olhar o exemplo do professor
                    pass

            elif event == '-ENTRAR_PROFESSOR-':
                tipo_usuario = 'professor'
                nome = values['-PROFESSOR_NOME-']
                cpf = values['-PROFESSOR_CPF-']

                if autenticar_usuario(tipo_usuario, nome, cpf):
                    self.window.close()
                    tela_professor = professor.TelaProfessorEscola()
                    tela_professor.iniciar()
                    pass

        self.window.close()


if __name__ == "__main__":
    tela_login_escola = TelaLoginEscola()
    tela_login_escola.iniciar()
