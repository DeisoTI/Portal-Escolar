import PySimpleGUI as sg
import login

class TelaProfessorEscola:
    def __init__(self):
        sg.theme('DarkBlue17')

        self.professor_info = {
            'nome': 'Eduardo Valente',
            'cpf': '544.356.213.24',
            'email': 'eduardovalente@gmail.com',
            'telefone': '(85)92356-3190',
            'endereco': 'Rua Vojvoda 34, Porangabussu',
            'atuacao': 'Informática',
        }


        # Tabelas para cada aba
        horarios_table_data = [['Sala 2', '8:00 - 9:15'],
                               ['Sala 9', '9:30 - 10:30'],
                               ['Sala 3', '10:45 - 12:00'],
                               ['Sala 6', '13:00 - 14:15'],
                               ['Sala 7', '14:30 - 15:30'],
                               ['Sala 8', '15:45 - 17:00'],
                               ['Sala 9', '17:15 - 18:30'],
                               ]

        horarios_table = [[sg.Table(values=horarios_table_data, headings=['Turma', 'Horário'], auto_size_columns=True,
                                    justification='right', key='-HORARIOS_TABLE-')]]

        aba_dados_pessoais = [
            [sg.Text('Nome:', size=(15, 1)), sg.Text(self.professor_info['nome'], size=(30, 1), key='-NOME-')],
            [sg.Text('CPF: ', size=(15, 1)), sg.Text(self.professor_info['cpf'], size=(30, 1), key='-CPF-')],
            [sg.Text('Área de Atuação: ', size=(15, 1)), sg.Text(self.professor_info['atuacao'], size=(30, 1), key='-AREA-')],
            [sg.Text('Telefone p/ Contato:', size=(15, 1)), sg.Text(self.professor_info['telefone'], size=(30, 1),
                                                                    key='-TELEFONE-'),
             sg.Button('Editar', key='-EDITARTELEFONE-')],
            [sg.Text('E-mail: ', size=(15, 1)), sg.Text(self.professor_info['email'], size=(30, 1), key='-EMAIL-'),
             sg.Button('Editar', key='-EDITAREMAIL-')],
            [sg.Text('Endereço :', size=(15, 1)), sg.Text(self.professor_info['endereco'], size=(30, 1), key='-ENDERECO-'),
             sg.Button('Editar', key='-EDITARENDERECO-')],
        ]

        layout_esquerda = [

            [sg.TabGroup([
                [sg.Text('Professor', font=('Helvetica', 20), justification='center')],
                [sg.Text('Seja bem-vindo!', font=('Helvetica', 13), text_color='LightGreen')],
                [sg.Tab('Horários', horarios_table)],
                [sg.Tab('Dados Pessoais', aba_dados_pessoais)]])],
            [sg.Button('Notas', size=(10, 1)), sg.Button('Frequências', size=(10, 1)),
             sg.Button('Log out', button_color=('white', 'red'), size=(10, 1), key='-LOGOUT-')],

        ]

        layout_direita = [

            [sg.Text(''), sg.Image('logo2.png', pad=(0, (0, 55)))],
            [sg.Text('')],
            [sg.Text('')]
        ]

        layout = [

            [sg.Column(layout_esquerda), sg.Column(layout_direita)]

        ]

        self.window = sg.Window('Portal Professor', layout, size=(1000, 450), resizable=False)

    def iniciar(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break
            elif event == '-LOGOUT-':
                self.window.close()
                tela_login_escola = login.TelaLoginEscola()
                tela_login_escola.iniciar()
            elif event == '-EDITARTELEFONE-':
                self.edit_info('telefone')
            elif event == '-EDITAREMAIL-':
                self.edit_info('email')
            elif event == '-EDITARENDERECO-':
                self.edit_info('endereco')

        self.window.close()

        # Função para abrir o pop up de erro
    def edit_info(self, field):
        if field == 'email':
            new_value = sg.popup_get_text(f'Edit {field}', default_text=self.professor_info[field])
            if new_value is not None:
                if '@' in new_value and '.com' in new_value:
                    self.professor_info[field] = new_value
                    self.update_info()
                else:
                    sg.popup_error('Formato inválido, por favor adicione "@" e(ou) ".com".')
        else:
            new_value = sg.popup_get_text(f'Edit {field}', default_text=self.professor_info[field])
            if new_value is not None:
                self.professor_info[field] = new_value
                self.update_info()

    def update_info(self):
        self.window['-NOME-'].update(self.professor_info['nome'])
        self.window['-CPF-'].update(self.professor_info['cpf'])
        self.window['-AREA-'].update(self.professor_info['atuacao'])
        self.window['-TELEFONE-'].update(self.professor_info['telefone'])
        self.window['-EMAIL-'].update(self.professor_info['email'])
        self.window['-ENDERECO-'].update(self.professor_info['endereco'])


if __name__ == "__main__":
    tela_professor_escola = TelaProfessorEscola()
    tela_professor_escola.iniciar()