class Candidato:
    def __init__(nome, sexo, nascimento, aprovado):
        self.nome = nome
        self.sexo = sexo
        self.nascimentos = nascimento
        self.aprovado = aprovado

    def __str__(self):
        return f"{self.nome}: {self.sexo}: {self.nascimento}: {self.aprovado}"