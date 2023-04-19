import psycopg2

try:
    
    conn = psycopg2.connect(dbname = "Escola2", host = "localhost", port = "5432", user = "postgres", password = "postgres")
    cursor = conn.cursor()
    print("Conectado com sucesso")

    # cursor.execute('''
    # create table "Matricula"(
    # "Nro_Matricula" serial,
    # "Cod_Disciplina" integer NOT NULL,
    # "Semestre" integer default 0,
    # "Ano" integer default '2023',
    # "Nota" numeric(2) default 0,
    # "Nro_Faltas" integer default 0,
    # Primary Key ("Nro_Matricula")
    # )
    # ''')

    cursor.execute('''
    insert into "Matricula"
    values (default, '2', default, '2001', '8', default)
    ''')
   
    conn.commit()

    conn.close()

except(Exception, psycopg2.Error) as error:
    print("Ocorreu um erro!", error)