from hashtable_cursos import criar_hash_table_de_cursos
from estatistica import *
from quicksort import quicksort

# FUNÇOES DO MENU
def listar_cursos(cursos_hash):
    print("\n============= Lista de Cursos =============")
    for chave, curso in cursos_hash.items():
        print(f"{chave}. {curso.nome} ")

def consultar_aprovados_por_curso(cursos_hash, curso_num):
    try:
        curso = cursos_hash.get(curso_num)
    except KeyError:
        print("Curso não encontrado.")
        return

    if curso:
        print(f"\nCurso: {curso.nome}")
        print(f"Campus: {curso.campus}")
        print(f"Município do Campus: {curso.municipio_campus}")
        print(f"Nota de corte: {curso.nota_corte}\n")
        print(f"{'    Nome':<50} {'Modalidade':<12} {'Opcao':<8} {'Nota':<7}")
        print("=== " + "=" * 46 + " " + "=" * 12 + " " + "=" * 6 + " " + "=" * 7)

        aprovados = [aluno for aluno in curso.alunos_aprovados if aluno.aprovado.lower() == 's']

        # Ordena os alunos aprovados usando QuickSort
        if len(aprovados) > 0:
            quicksort(aprovados, 0, len(aprovados) - 1)
            for idx, aluno in enumerate(aprovados, start=1):
                if aluno.modalidade_concorrencia.lower() == "ampla concorrência":
                    modalidade = "Ampla"
                else:
                    modalidade = "Cota"
                print(f"{idx:03} {aluno.nome:<50} {modalidade:<10} {aluno.opcao:<5} {aluno.nota_candidato:<7}")
        else:
            print("Nenhum aluno aprovado encontrado para este curso.")
    else:
        print("Curso não encontrado.")
def pesquisar_candidato(cursos_hash, nome_aluno):
    nome_aluno = nome_aluno.lower()
    alunos_encontrados = []

    for curso_num, curso in cursos_hash.items():
        for aluno in curso.alunos_aprovados:
            if aluno.nome.lower().startswith(nome_aluno):
                alunos_encontrados.append((curso, aluno))

    if not alunos_encontrados:
        print("Aluno não encontrado.")
    else:
        # Ordena os alunos encontrados pelo nome
        alunos_encontrados.sort(key=lambda x: x[1].nome)

        # Imprime os resultados ordenados
        for idx, (curso, aluno) in enumerate(alunos_encontrados, start=1):
            modalidade = "Cota" if aluno.modalidade_concorrencia.lower() != "ampla concorrência" else "Ampla Concorrência"
            print(f"{idx:03d} {aluno.nome:<50} {aluno.sexo:<8} {aluno.data_nascimento:<10} "
                  f"{aluno.aprovado:<3} {aluno.nota_candidato:<6.2f} {modalidade:<20} {aluno.opcao:<20} {curso.nome}")

# MENU PRINCIPAL INTERAÇÃO COM USUÁRIO
def main():
    arquivo_csv = 'chamada_regular_sisu_2022_2.csv'
    instituicao_filtro = 'UFPB'  
    estatistica = Estatistica()

    # Criação da hash table de cursos
    
    cursos_hash, estatistica = criar_hash_table_de_cursos(arquivo_csv, instituicao_filtro)

    # Imprimir estatísticas
    #estatistica.imprimir_estatisticas()
    while True:
        print("\nIES: UNIVERSIDADE FEDERAL DA PARAÍBA")
        print("\n============= Menu Principal ==============")
        print("(c) Consultar aprovados por curso")
        print("(l) Listar Cursos")
        print("(p) Pesquisar candidato")
        print("(s) Sair")
        opcao = input("Escolha uma opção: ").strip().lower()

        if opcao == 'c':
            listar_cursos(cursos_hash)
            try:
                curso_num = int(input("\nDigite o número do curso para consultar aprovados: "))
                consultar_aprovados_por_curso(cursos_hash, curso_num)
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
            except KeyError as e:
                print(e)

        elif opcao == 'l':
            listar_cursos(cursos_hash)

        elif opcao == 'p':
            nome_candidato = input("Digite o nome do aluno para consulta: ").strip()
            pesquisar_candidato(cursos_hash, nome_candidato)

        elif opcao == 's':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()