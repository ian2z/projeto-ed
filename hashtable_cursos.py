import csv
from entidades import Curso, Aluno
from estatistica import Estatistica
from LinearProbingLoadFactor import HashTable

def criar_hash_table_de_cursos(arquivo_csv, instituicao_filtro):
    hash_table = HashTable()
    contador_curso = 1
    estatistica = Estatistica()

    try:
        with open(arquivo_csv, 'r', newline='', encoding='latin1') as file:
            csv_reader = csv.DictReader(file, delimiter='|')
            for row in csv_reader:
                if row['SIGLA_IES'] == instituicao_filtro:
                    nome_curso = row['NOME_CURSO']
                    municipio_campus = row.get('MUNICIPIO_CAMPUS', 'N/A')

                    curso_existente = None
                    for _, curso in hash_table.items():
                        if curso.nome == nome_curso and curso.municipio_campus == municipio_campus:
                            curso_existente = curso
                            break

                    if not curso_existente:
                        curso = Curso(
                            nome=nome_curso,
                            nota_corte=row.get('NOTA_CORTE', '0'),
                            modalidade_concorrencia=row.get('MOD_CONCORRENCIA', 'N/A'),
                            campus=row.get('NOME_CAMPUS', 'N/A'),
                            municipio_campus=municipio_campus,
                            quantidade_vagas=row.get('QT_VAGAS_CONCORRENCIA', '0')
                        )
                        hash_table.put(contador_curso, curso)
                        contador_curso += 1
                        curso_existente = curso

                    modalidade_concorrencia = row.get('MOD_CONCORRENCIA', 'N/A')
                    quantidade_vagas = int(row.get('QT_VAGAS_CONCORRENCIA', '0'))

                    if modalidade_concorrencia not in curso_existente.modalidade_vagas:
                        curso_existente.modalidade_vagas[modalidade_concorrencia] = quantidade_vagas

                    aluno_nome = row.get('NOME_ALUNO', row['INSCRITO'])
                    aluno = Aluno(
                        inscrito=row['INSCRITO'],
                        nome=aluno_nome,
                        nota_candidato=row.get('NOTA_CANDIDATO', '0'),
                        sexo=row.get('SEXO', 'N/A'),
                        data_nascimento=row.get('DATA_NASCIMENTO', 'N/A'),
                        aprovado=row.get('APROVADO', 'N/A'),
                        opcao=row.get('OPCAO', 'N/A'),
                        modalidade_concorrencia=row.get('MOD_CONCORRENCIA', 'N/A')
                    )
                    curso_existente.adicionar_aluno(aluno)
                    
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {arquivo_csv}")
    
    estatistica.calcular_estatisticas(hash_table)
    estatistica.imprimir_estatisticas()
    

    return hash_table,estatistica.calcular_estatisticas(hash_table)
    
    