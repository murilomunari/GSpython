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

    return lista_de_dados_paciente

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

def CREATE_TABLE_RAMO():
    conn = getConnection()
    cursor = conn.cursor()
    sql_RAMO = """
    CREATE TABLE TB_RAMO(
    ID_RAMO NUMBER(19,0),
    NM_RAMO VARCHAR2(255),  
    CONSTRAINT PK_ID_RAMO PRIMARY KEY (ID_RAMO)
);
"""
    try:
        cursor.execute(sql_RAMO)
        print("Tabela RAMO criada")
    except Exception as e:
        print(f"erro ao criar a tabela RAMO: {e}")
    finally:
        cursor.close
        conn.close


def cadastrarRamo():
    print("Cadastre um ramo a seguir")
    lista_de_dados_ramo = []
    ID_RAMO = int(input("id: "))
    lista_de_dados_ramo.append(ID_RAMO)

    NM_RAMO = input("digite o nome do rmao: ")
    lista_de_dados_ramo.append(NM_RAMO)

    return lista_de_dados_ramo

def INSERIR_DADOS_RAMO(lista_de_dados_ramo):
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "INSERT INTO RAMO (ID_RAMO, NM_RMAO) VALUES (:0, :1)"
    try:
        cursor.execute(sql_query(lista_de_dados_ramo[0], lista_de_dados_ramo[1]))
        conn.commit()
    except Exception as e:
        print(f"Erro ao inserir o registro do ramo: {e}")
    finally:
        cursor.close()
        conn.close()

def DROP_TABLE_RAMO():
    conn = getConnection()
    cursor = conn.cursor()
    sql_enderecodrop = """
    DROP TABLE RAMO;
"""
    try:
        cursor.execute(sql_enderecodrop)
        print("tabela RAMO dropada")
    except Exception as e:
        print(f"Erro ao dropar a tabela RAMO: {e}")
    finally:
        cursor.close()
        conn.close()

def CREATE_TABLE_EMPRESA():
    conn = getConnection()
    cursor = conn.cursor()
    sql_EMPRESA = """
    ID_EMPRESA NUMERIC(19,0),
    NM_EMPRESA VARCHAR2(255),
    E_MAIL VARCHAR(50),
    NR_CNPJ VARCHAR2(14),
    RAMO NUMBER(19,0),
    CONSTRAINT PK_ID_EMPRESA PRIMARY KEY (ID_EMPRESA),
    CONSTRAINT fk_TB_EMPRESA_TB_RAMO FOREIGN KEY (ID_RAMO) REFERENCES TB_RAMO(ID_RAMO)
);
"""
    try:
        cursor.execute(sql_EMPRESA)
        print("Tabela EMPRESSA criada")
    except Exception as e:
        print(f"Erro ao criar a tabela EMPRESA: {e}")
    finally:
        cursor.close
        conn.close

def cadastrarEmpresa():
    print("Cadastre uma empresa!")
    lista_de_dados_empresa = []
    ID_EMPRESA = int(input("id: "))
    lista_de_dados_empresa.append(ID_EMPRESA)

    NM_EMPRESA = input("Nome da empresa: ")
    lista_de_dados_empresa.append(NM_EMPRESA)

    E_MAIL = input("Digite o email da empresa: ")
    lista_de_dados_empresa(E_MAIL)

    NR_CNPJ = input("Digite o cnpj da empresa: ")
    lista_de_dados_empresa.append(NR_CNPJ)

    RAMO = int(input("Digite o ramo da empresa: "))
    lista_de_dados_empresa.append(RAMO)

    return lista_de_dados_empresa


def INSERIR_DADOS_EMPRESA(lista_de_dados_empresa):
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "INSET INTO EMPRESA (ID_EMPRESA, NM_EMPRESA, E_MAIL, NR_CNPJ, RAMO ) VALUES (:0, :1, :2, :3, :4)"
    try:
        cursor.excute(sql_query(lista_de_dados_empresa[0], lista_de_dados_empresa[1], lista_de_dados_empresa[2], lista_de_dados_empresa[3], lista_de_dados_empresa[4]))
        conn.commit()
        print("Registro da empresa inserido com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir o registro da empresa: {e}")
    finally:
        cursor.close()
        conn.close()

def DROP_TABLE_EMPRESA():
    conn = getConnection()
    cursor = conn.cursor()
    sql_enderecodrop ="""
    DROP TABLE EMPRESA;
"""
    try:
        cursor.execute(sql_enderecodrop)
        print("Tabela EMPRESA dropada")
    except Exception as e:
        print(f"Erro ao dropar a tabela EMPRESA: {e}")
    finally:
        cursor.close
        conn.close

