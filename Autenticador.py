class Autenticador:
    def __init__(self):
        self.usuarios = {
            'Anderson Freira Freiras': {'senha': '123456789'},
            'Eduardo Valente': {'senha': '98363253295'}
        }

    def autenticar(self, usuario, senha):
        if usuario in self.usuarios and self.usuarios[usuario]['senha'] == senha:
            return True
        return False