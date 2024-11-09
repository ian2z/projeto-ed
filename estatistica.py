class Estatistica:
    
    def __init__(self):
        self.ies_nome = ""
        self.ies_sigla = ""
        self.lista_campus = set()
        self.cursos_ofertados = {}
        self.total_candidatos = 0
        self.candidatos_ampla = 0
        self.candidatos_cota = 0
        self.curso_maior_nota_corte = None
        self.curso_menor_nota_corte = None
        self.curso_mais_concorrido = None
        self.curso_menos_concorrido = None

       

    def calcular_estatisticas(self, cursos_hash):
       
        for curso in cursos_hash.values():
            self.lista_campus.add(curso.municipio_campus)
            self.cursos_ofertados[curso.nome] = calcular_total_vagas(curso)

            candidatos_curso = len(curso.alunos_aprovados)
            self.total_candidatos += candidatos_curso

            if self.curso_mais_concorrido is None or candidatos_curso > len(self.curso_mais_concorrido.alunos_aprovados):
                self.curso_mais_concorrido = curso
            if self.curso_menos_concorrido is None or candidatos_curso < len(self.curso_menos_concorrido.alunos_aprovados):
                self.curso_menos_concorrido = curso

            if self.curso_maior_nota_corte is None or curso.nota_corte > self.curso_maior_nota_corte.nota_corte:
                self.curso_maior_nota_corte = curso
            if self.curso_menor_nota_corte is None or curso.nota_corte < self.curso_menor_nota_corte.nota_corte:
                self.curso_menor_nota_corte = curso

            for aluno in curso.alunos_aprovados:
                if aluno.modalidade_concorrencia.lower() == "ampla concorrência":
                    self.candidatos_ampla += 1
                else:
                    self.candidatos_cota += 1

    def imprimir_estatisticas(self):
        print(f"IES processada : UNIVESRIDADE FEDERAL DA PARAÍBA\n")
        print(f"Sigla da IES   : UFPB \n")
        print(f"Lista de Campus: {', '.join(sorted(self.lista_campus))}\n")
        print("Cursos Ofertados:\n")
        for curso, vagas in self.cursos_ofertados.items():
            print(f"{curso}  ( {vagas} vagas)")

        print(f"Nº de Candidatos inscritos (total): {self.total_candidatos}")
        print(f"    Ampla concorrência: {self.candidatos_ampla}    ({self.candidatos_ampla/self.total_candidatos*100:.1f} %)")
        print(f"    Cotista...........: {self.candidatos_cota}    ({self.candidatos_cota/self.total_candidatos*100:.1f} %)")
        print(f"Curso de maior nota de corte: {self.curso_maior_nota_corte.nome}")
        print(f"Curso de menor nota de corte: {self.curso_menor_nota_corte.nome}")
        print(f"Curso mais concorrido: {self.curso_mais_concorrido.nome} ({len(self.curso_mais_concorrido.alunos_aprovados)} candidatos)")
        print(f"Curso de menor concorrência: {self.curso_menos_concorrido.nome} ({len(self.curso_menos_concorrido.alunos_aprovados)} candidatos)")

        

def calcular_total_vagas(curso):
    total_vagas = 0
    for modalidade, vagas in curso.modalidade_vagas.items():
        total_vagas += vagas
    return total_vagas