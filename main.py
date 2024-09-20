from hashtable import *

ht = HashTable()

with open("chamada_regular_sisu_2022_2.csv", "r", encoding="latin1") as arquivo:
    cabecalho = arquivo.readline().strip().split(",")
    data = [linha.strip().split(",") for linha in arquivo]

print(cabecalho)
#print(data)

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