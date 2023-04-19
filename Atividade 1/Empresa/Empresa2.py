# Deve conter as seguintes entidades Funcionários e Departamentos
# Requisitos:
# - Ver lista de funcionários
# - Ver lista de departamentos
# - Ver informações de funcionários específicos(Deve conter o nome do Departamento de que faz parte)
# - Ver lista de funcionários de um departamento específico
# - Opcional: Funcionário gerente e login antes de usar o sistema
# - Inserção de Funcionários e Departamentos
# - Atualização de informações de Funcionários e Departamentos
# - Remoção de Funcionários e Departamentos

# Entidade Funcionária:

# Id_Func: inteiro GERADO AUTOMATICAMENTE (PK)
# Nome_Func: char(255) NOT NULL
# Salário_Func: float(2) NOT NULL default 0.00
# Cargo_Func: char(255) NOT NULL default Autônomo
# Id_Departamento: integer (FK)

# Departamento da Entidade:

# Id_Departamento: integer AUTO GENERATED (PK)
# Nome_Departamento: char(255)
# #Id_Gerente: integer (FK) (OPCIONAL)

import psycopg2

try:
    conn = psycopg2.connect(dbname = "Empresa", host = "localhost", port = "5432", user = "postgres", password = "postgres")

    cursor = conn.cursor()

    print("Conexão bem sucedida!")

    conn.close()

except(Exception, psycopg2.Error) as error:
    print("Ocorreu um erro ao tentar a conexão:", error)

def verFuncionarioUnico(id):

    cursor.execute(f'''
    Select * from "Funcionário"
    Where "ID" = '{id}
    ''')

    funcionario = cursor.fetchone()

    if funcionario:

        cursor.execute(f'''
        Select * from "Departamento"
        Where "ID" = '{funcionario[4]}'
        ''')

        departamento = cursor.fetchone()
        

        print(f'''
        ID: {funcionario[0]}
        Nome: {funcionario[1]}
        Salário R$: {funcionario[2]}
        Cargo: {funcionario[3]}
        Departamento: {funcionario[4]}
        ''')

    else:
        print("Funcionário não encontrado.")

def verDepartamentoUnico(id):

    cursor.execute(f'''
    Select * from "Departamentos"
    WHERE "Id" = '{id}'
    ''')

    departamento = cursor.fetchone()

    if departamento:
        print(f'''
        ID: {departamento[0]}
        Nome: {departamento[1]}
        ''')

    else:
        print("Departamento não encontrado.")

def verFuncionarios():

    cursor.execute('''
                SELECT * FROM "Funcionário"
                ORDER BY "Id" ASC
                ''')

    listaFuncionarios = cursor.fetchall()
    print("ID - Nome")
    for funcionario in listaFuncionarios:
        print(f"{funcionario[0]} - {funcionario[1]}")

    idEscolhido = input("Digite o id de um funcionário que deseja ver mais informações:(0 = Voltar) ")

    if idEscolhido != "0":
        verFuncionarioUnico(idEscolhido)
    else:
        print("Voltando para o menu principal.")


def verDepartamentos():

    cursor.execute('''
                SELECT * FROM "Departamentos"
                ORDER BY "Id" ASC
                ''')

    listaDepartamentos = cursor.fetchall()
    print("ID - Nome")
    for departamento in listaDepartamentos:
        print(f"{departamento[0]} - {departamento[1]}")

    idEscolhido = input("Digite o id de um departamento que deseja ver mais informações:(0 = Voltar) ")

    if idEscolhido != "0":
        verDepartamentoUnico(idEscolhido)
    else:
        print("Voltando para o menu principal.")

def inserirFuncionario():
    print("Você está cadastrando um funcionário.")

    novoFuncionarioNome = input("Digite o nome do novo funcionário: ")
    novoFuncionarioSalario = input("Digite o salário do novo funcionário: ")
    novoFuncionarioCargo = input("Digite o cargo do novo funcionário: ")
    novoFuncionarioIdDepartamento = input("Digite o departamento do novo funcionário: ")

    cursor.execute(f'''
    INSERT INTO "Funcionário"
    Values(default, '{novoFuncionarioNome}', '{novoFuncionarioSalario}', '{novoFuncionarioCargo}', '{novoFuncionarioIdDepartamento}')
    
    ''')

    conn.commit()

    print("Funcionário Inserido!")

def inserirDepartamento():
    print("Você está cadastrando um departamento.")

    novoDepartamentoNome = input("Digite o nome do novo departamento: ")


    cursor.execute(f'''
    INSERT INTO "Departamentos"
    Values(default, '{novoDepartamentoNome}')
    
    ''')

    conn.commit()

    print("Departamento Inserido!")


while True:
    try:

        print('''
   Bem vindo a Empresa
Escolha uma opção do menu:
1 - Ver Funcionários
2 - Ver Departamentos
3 - Inserir Funcionário
4 - Inserir Departamento
0 - Sair
 ''')

        op = input("Digite a opção escolhida:")

        match op:
            case "1":
                verFuncionarios()

            case "2":
                verDepartamentos()

            case "3":
                inserirFuncionario()

            case "4":
                inserirDepartamento()

            case "0":
                print("Saindo do programa...")
                cursor.close()
                conn.close()
                break
            case _:
                print("Opção inválida. Digite novamente!")

        input("Tecle enter para continuar.")

    except (Exception, psycopg2.Error) as error:

        print("Ocorreu um erro", error)




