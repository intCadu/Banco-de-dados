import psycopg2

def criarTabelaFuncionario():

    sql = '''
    create Table "Funcionário"(
    "ID" integer Generated Always as Identity Primary Key,
    "Nome" varchar(255) NOT NULL,
    "Salário" money NOT NULL default 0,
    "Cargo" varchar(255) NOT NULL default 'Autônomo',
    "Id_Dept" int
    )
    '''
    return sql

def criarTabelaDepartamentos():

    sql = '''
    create Table "Departamento"(
    "ID" integer Generated Always as Identity Primary Key,
    "Nome" varchar(255) NOT NULL
    -- "Id_Gerente" int NOT NULL 1
    )
    '''
    return sql

try:
    conn = psycopg2.connect(dbname = "Empresa", host = "localhost", port = "5432", user = "postgres", password = "postgres")

    cursor = conn.cursor()

    cursor.execute(criarTabelaFuncionario())
    conn.commit()

    cursor.execute(criarTabelaDepartamentos())
    conn.commit()

    print("Conexão bem sucedida!")

    conn.close()

except(Exception, psycopg2.Error) as error:
    print("Ocorreu um erro ao tentar a conexão:", error)


