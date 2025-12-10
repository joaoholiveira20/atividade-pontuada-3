# João Henrique Santos Sousa de Oliveira 
# Delane "Sebastian" Miranda Maia Filho 

from dataclasses import dataclass
import time
import os

os.system("cls")

class Reserva:
    def __init__(self, numero_aviao, nome_passageiro):
        self.numero_aviao = numero_aviao
        self.nome_passageiro = nome_passageiro
    
def mostrar_menu ():
    os.system("cls")
    print("\nMenu de Opções Sweet Fligth:")
    print("1- Registrar número do avião")
    print("2- Registrar quantidade de assentos disponiveis no avião")
    print("3- Reservar passagem aérea")
    print("4- Realizar consulta por avião")
    print("5- Realizar consulta por passageiro")
    print("0- Encerrar programa")

def encontrar_aviao(avioes, numero_aviao):
    if numero_aviao in  avioes:
        return avioes.index(numero_aviao)
    return -1

def main():
    avioes = [0] * 4
    assentos = [0] * 4
    reservas = []
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        match opcao: #OPÇÕES DE REGISTRAR O AVIÃO
            case "1":
                for i in range(4):
                    num = int(input(f"Digite o número do avião {i+1}: "))
                    avioes[i] = num
                print("Números dos aviões registrados com sucesso.")
                time.sleep(2)

            case "2": #OPCÃO 2 REGISTRAR QUANTIDADE DE ASSENTOS
                 #verifica se os aviões foram cadastrados
                 if avioes[0] == 0 and avioes[1] == 0 and avioes[2] == 0 and avioes[3] == 0:
                     print("Nenhum avião cadastrado. Por favor, registre os aviões primeiro.")
                     time.sleep(2)
                 else:
                     print("\nCadastrando assentos disponíveis para os aviões:")
                     for i in range(4):
                          qtd=int(
                                input(f"Digite a quantidade de assentos disponíveis para o avião {avioes[i]}: ")
                          )
                          assentos[i] = qtd
                     print("Quantidade de assentos registrada com sucesso.")
                     time.sleep(2)
                     
            case "3": #OPÇÃO 3 FAZER RESERVA
                if len(reservas) >= 20:
                    print("Limite máximo de reservas atingido.")
                    time.sleep(2)
                    continue
                numero_aviao = int(input("Digite o número do avião para a reserva: "))
                indice_aviao = encontrar_aviao(avioes, numero_aviao)
                if indice_aviao == -1 :
                    print("Avião inexistente.")
                    time.sleep(2)
                else:
                    if assentos[indice_aviao] <= 0:
                        print("Sem assentos disponíveis.")
                        time.sleep(2)
                    else:
                        nome_passageiro = input("Digite o nome do passageiro: ")
                        nova_reserva = Reserva(numero_aviao, nome_passageiro)
                        reservas.append(nova_reserva)
                        assentos[indice_aviao] -= 1
                        print("Reserva concluída com sucesso.")
                        time.sleep(2)

            case "4": #OPÇÃO 4 CONSULTAR RESERVAS POR AVIÃO
                numero_aviao = int(input("Digite o número do avião para consulta: "))
                indice_aviao = encontrar_aviao(avioes, numero_aviao)
                if indice_aviao == -1 :
                    print("Avião inexistente. ")
                    time.sleep(2)
                else:
                    encontrou = False
                    print(f"Reservas para o avião {numero_aviao}:")
                    for r in reservas:
                        if r.numero_aviao == numero_aviao:
                            print(f"- Passageiro: {r.nome_passageiro}")
                            time.sleep(2)
                            encontrou = True
                        if not encontrou:
                            print("Nenhuma reserva encontrada para este avião.")
                            time.sleep(2)

            case "5": #OPÇÃO 5 CONSULTAR RESERVAS POR PASSAGEIRO
                nome_passageiro = input("Digite o nome do passageiro para consulta: ")
                encontrou = False
                print(f"Reservas para o passageiro {nome_passageiro}:")
                for r in reservas:
                    if r.nome_passageiro.lower() == nome_passageiro.lower():
                        print(f"- Avião: {r.numero_aviao}")
                        time.sleep(2)
                        encontrou = True
                        if not encontrou:
                            print("Nenhuma reserva encontrada para este passageiro.")
                            time.sleep(2)

            case "0": #OPÇÃO 0 ENCERRAR PROGRAMA
                print("Encerrando o programa. Obrigado por usar a Sweet Flight!")
                break
            
            case _:
                print("Opção inválida. Tente novamente.")
                time.sleep(2)
if __name__ == "__main__":
    main()