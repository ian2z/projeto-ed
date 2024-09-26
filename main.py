from hashtable import *
from candidato import Candidato


with open("chamada_regular_sisu_2022_2.csv", "r", encoding="UTF-8") as arquivo:
    cabecalho = arquivo.readline().strip().split("|")
    dados = [linha.strip().split("|") for linha in arquivo]

#print(cabecalho)
#print(dados)

ht = HashTable()

ies = "UFPB"
indice_ies = cabecalho.index("SIGLA_IES")

nome = cabecalho.index("INSCRITO")
campus = cabecalho.index("NOME_CAMPUS")
nome_ies = cabecalho.index("NOME_IES")
teste_ufpb = []


for linha in dados:
    if linha[indice_ies] == ies:
        teste_ufpb.append(linha[campus])

    
print(teste_ufpb)


# def menu_principal():
#     while True:
#         print("\n============= Menu Principal =============")
#         print("(c) Consultar aprovados por curso")
#         print("(l) Listar Cursos")
#         print("(p) Pesquisar candidato")
#         print("(s) Sair")
#         opcao = input("Escolha uma opção: ")

#         if opcao == 'c':
#             consultar_aprovados_por_curso()
#         elif opcao == 'l':
#             listar_cursos()
#         elif opcao == 'p':
#             pesquisar_candidato()
#         elif opcao == 's':
#             break
#         else:
#             print("Opção inválida!")