import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_21_12")

def getConnection():
    try:
        connection = cx_Oracle.connect("RM551463", "040304", "oracle.fiap.com.br/ORCL")
        # connection = cx_Oracle.connect(user="a", password="b", host="c", port="1521", service="ORCL")
        print("conexão: ", connection.version)
        return connection
    except Exception as e:
        print(f'Erro ao obter conexão: {e}')

def CREATE_TABLE_AREAS():
    conn = getConnection()
    cursor = conn.cursor()
    sql_AREAS = """
    CREATE TABLE TB_AREAS(
    ID_AREA INT NOT NULL,
    REGIAO VARCHAR2(255),
    CEP INT NOT NULL,
    CONSTRAINT PK_ID_AREA PRIMARY KEY (ID_AREA)
    ); 
    """
    try:
        cursor.execute(sql_AREAS)
        print("tablea AREAS criada")
    except Exception as e:
        print(f"Erro ao cirar a tabela AREAS: {e}")
    finally:
        cursor.closa
        conn.close

def cadastrarArea():
    print("Cadastre uma nova area em nosso banco!")
    lista_de_dados_area = []
    ID_AREA = int(input("id:"))
    lista_de_dados_area.append(ID_AREA)

    REGIAO = input("Digite a região requirida: ")
    lista_de_dados_area.append(REGIAO)

    CEP = input("Digite o CEP da região: ")
    lista_de_dados_area.append(CEP)

    return lista_de_dados_area

def INSERIR_DADOS_AREA(lista_de_dados_area):
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "INSERT INTO AREAS (ID_AREA, REGIAO, CEP) VALUES(:0, :1, :2)"
    try:
        cursor.execute(sql_query(lista_de_dados_area[0], lista_de_dados_area[1], lista_de_dados_area[2]))
        conn.commit()
        print("registro de area inserido com sucesso.")
    except Exception as e:
        print(f"Erro ao inserir o registro da area: {e}")
    finally:
        cursor.close()
        conn.close()

def DROP_TABLE_AREA():
    conn = getConnection()
    cursor = conn.cursor()
    sql_enderecodrop = """
    DROP TABLE AREAS;
    """
    try:
        cursor.execute(sql_enderecodrop)
        print("Tabela AREAS dropada")
    except Exception as e:
        print(f"Erro ao dropar a tabela AREAS: {e}")
    finally:
        cursor.close
        conn.close

def CREATE_TABLE_PACIENTE():
    conn = getConnection()
    cursor = conn.cursor()
    sql_Paciente = """
    CREATE TABLE TB_PACIENTE(
    ID_PACIENTE INT NOT NULL,
    NM_PACIENTE VARCHAR2(255),
    CPF VARCHAR2(11),
    NASCIMENTO DATE,
    CONSTRAINT PK_ID_PACIENTE PRIMARY KEY (ID_PACIENTE),
    );
    """
    try:
        cursor.excute(sql_Paciente)
        print("Tabela PACIENTE criada")
    except Exception as e:
        print(f"Erro ao criar a tabela PACIENTE: {e}")
    finally:
        cursor.closa()
        conn.close()

def cadastrarPaciente():
    print("Faça seu cadastro para saber o seu resultado")
    lista_de_dados_paciente = []
    ID_PACIENTE =  int(input("id: "))
    lista_de_dados_paciente.append(ID_PACIENTE)

    NM_PACIENTE = input("Nome: ")
    lista_de_dados_paciente.append(NM_PACIENTE)

    CPF = input("CPF: ")
    lista_de_dados_paciente.append(CPF)

    DT_NASCIMENTO = input("Data de nascimento: ")
    lista_de_dados_paciente.append(DT_NASCIMENTO)

def INSERIR_DADOS_PACIENTE(lista_de_dados_paciente):
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "INSERT INTO PACIENTE(ID_PACIENTE, NM_PACIENTE, CPF, DT_NASCIMENTO) VALUES(:0, :1, :2, (:3, dd/mm/yyyy))"
    try:
        cursor.excute(sql_query, (lista_de_dados_paciente[0], lista_de_dados_paciente[1], lista_de_dados_paciente[2], lista_de_dados_paciente[3], lista_de_dados_paciente[4]))
        conn.commit()
        print("Registro realizado com sucesso.")
    except Exception as e:
        print(f"Erro no registro do paciente: {e}")
    finally:
        cursor.closa()
        conn.close()

def DROP_TABLE_PACIENTE():
    conn = getConnection()
    cursor = conn.cursor()
    sql_endercodrop = """
    DROP TABLE PACIETE
    """
    try:
        cursor.execute(sql_endercodrop)
        print("tabela PACIENTE dropada")
    except Exception as e:
        print(f"Erro ao dropar a tabela PACIENTE: {e}")
    finally:
        cursor.close
        conn.close



