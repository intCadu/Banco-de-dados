import psycopg2

try:
    
    conn = psycopg2.connect(dbname = "Escola2", host = "localhost", port = "5432", user = "postgres", password = "postgres")
    cursor = conn.cursor()
    print("Conectado com sucesso")

    # cursor.execute('''
    # create table "Alunos"(
    # "Nro_Matricula" serial,
    # "Nome" varchar(255) NOT NULL,
    # "CPF" char(11) NOT NULL,
    # "Endereço" varchar(255) default 'Não informado',
    # "Telefone" char(11) default 'xx-xxx',
    # "Ano Nascimento" integer,
    # Primary Key ("Nro_Matricula")
    # )
    # ''')

    # conn.commit()
    cursor.execute('''
    insert into "Alunos"
    values (default, 'Fernando', '12345678910', default, default, 2010)
    ''')
    conn.commit()

    conn.close()

except(Exception, psycopg2.Error) as error:
    print("Ocorreu um erro!", error)