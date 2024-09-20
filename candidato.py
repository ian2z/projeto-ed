class Candidato:
    def __init__(self, nome, sexo, nascimento, aprovado):
        self.nome = nome
        self.sexo = sexo
        self.nascimento = nascimento
        self.aprovado = aprovado

    def __str__(self):
        return f"{self.nome}: {self.sexo}: {self.nascimento}: {self.aprovado}"
    
    def __lt__(self, outro):
        return self.nome < outro.nome

    def __gt__(self, outro):
        return self.nome > outro.nome
    
    def __eq__(self, outro):
        return self.nome == outro.nome