import psycopg2

def creteTableFuncionario():
    sql = ('''
    Create Table "Funcionário"(
    "ID_Funcionario" integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome_Func"  varchar(255) NOT NULL,
    "CPF_Func" char(11) UNIQUE NOT NULL,
    "Func_Salário" money,
    "ID_Dept" int default 1,
    CONSTRAINT fk_departamento 
        FOREIGN KEY ("ID_Dept")
        REFERENCES "Departamento"("ID_Dept")
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
    )
    ''')
    return sql

def createTableDepartamento():

    sql = ('''
    Create Table "Departamento"(
    "ID_Dept" integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome_Dept" varchar(255) NOT NULL,
    "ID_Chefe" int
    )
    ''')

    return sql

def consultarFuncionario(id):
    cursor.execute(f'''
    Select * From "Funcionário"
    Where "Nome_Func" = {id}''')





try:

    conn = psycopg2.connect(dbname = "NovaEmpresa", host = "localhost", port = "5432", user = "postgres", password = "postgres")
    cursor = conn.cursor()
    print("Conectado com sucesso")  

    conn.commit()
    conn.close()
    
except(Exception, psycopg2.Error) as error:
    print("Ocorreu um erro ao tentar a conexão:", error)






