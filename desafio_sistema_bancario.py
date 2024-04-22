menu = """
Digite a opção desejada:

[1] Depósito
[2] Saque
[3] Extrato
[0] Sair

"""

saldo = 0
limite = 500
extrato = """"""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

# deposito
    if opcao == 1:
        valor = float(input("Digite o valor que deseja depositar: \n"))
        if valor <= 0:
            print("Valor incorreto, favor informar um valor válido")

        else:
            saldo += valor
            extrato = extrato + f"""\nDeposito: R$ {valor:.2f}"""         
            print(f"Realizado o deposito de R$ {valor:.2f}")

# saque            
    elif opcao == 2:

        if numero_saques == LIMITE_SAQUES:
            print("Limite de saques atingido")
            continue

        else:

            valor = float(input("Digite o valor que deseja sacar: \n"))
            if valor > float(500):
                print("Limite de saque não disponível")
            elif valor > saldo:
                print("Valor de saque não dispoível")
            else:
                numero_saques += 1
                saldo -= valor
                extrato = extrato + f"""\nSaque: R$ {valor:.2f}"""         
                print(f"Realizado o saque de R$ {valor:.2f}")
        
            
            
            
        print()

# extrato        
    elif opcao == 3:
        print(f"""Extrato:
              {extrato}""")
    elif opcao == 0:
        print()
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
