class Curso:
    def __init__(self, nome, nota_corte, modalidade_concorrencia, campus, municipio_campus, quantidade_vagas):
        self.nome = nome
        try:
            self.nota_corte = float(nota_corte.replace(',', '.').strip())
        except ValueError:
            self.nota_corte = 0.0
        self.modalidade_concorrencia = modalidade_concorrencia
        self.campus = campus
        self.municipio_campus = municipio_campus
        self.modalidade_vagas = {}
        try:
            self.quantidade_vagas = int(quantidade_vagas)
        except ValueError:
            self.quantidade_vagas = 0
        self.alunos_aprovados = []

    def adicionar_aluno(self, aluno):
        self.alunos_aprovados.append(aluno)

class Aluno:
    def __init__(self, inscrito, nome, nota_candidato, sexo, data_nascimento, aprovado, opcao, modalidade_concorrencia):
        self.inscrito = inscrito
        self.nome = nome
        try:
            self.nota_candidato = float(nota_candidato.replace(',', '.').strip())
        except ValueError:
            self.nota_candidato = 0.0
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.aprovado = aprovado
        self.opcao = opcao
        self.modalidade_concorrencia = modalidade_concorrencia
        if self.modalidade_concorrencia.lower() != "ampla concorrência":
            modalidade_concorrencia = "Cota"
        else:
            modalidade_concorrencia = self.modalidade_concorrencia