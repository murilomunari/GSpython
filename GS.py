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


def CREATE_TABLE_AREA():
    conn = getConnection()
    cursor = conn.cursor()
    sql_AREAS = """
    CREATE TABLE TB_AREAS(
    ID_AREA INT NOT NULL,
    REGIAO VARCHAR2(255),
    CEP INT NOT NULL,
    CONSTRAINT PK_ID_AREA PRIMARY KEY (ID_AREA)
    )"""
    try:
        cursor.execute(sql_AREAS)
        print("tabela AREAS criada")
    except Exception as e:
        print(f"Erro ao criar a tabela AREAS: {e}")
    finally:
        cursor.close()
        conn.close()

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
    sql_query = "INSERT INTO TB_AREAS (ID_AREA, REGIAO, CEP) VALUES (:0, :1, :2)"
    try:
        cursor.execute(sql_query, (lista_de_dados_area[0], lista_de_dados_area[1], lista_de_dados_area[2]))
        conn.commit()
        print("Registro da área inserido com sucesso.")
    except Exception as e:
        print(f"Erro ao inserir o registro da área: {e}")
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
    CONSTRAINT PK_ID_PACIENTE PRIMARY KEY (ID_PACIENTE)
    )"""
    try:
        cursor.execute(sql_Paciente)
        print("Tabela PACIENTE criada")
    except Exception as e:
        print(f"Erro ao criar a tabela PACIENTE: {e}")
    finally:
        cursor.close()
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
    sql_query = "INSERT INTO TB_PACIENTE (ID_PACIENTE, NM_PACIENTE, CPF, NASCIMENTO) VALUES (:0, :1, :2, TO_DATE(:3, 'DD/MM/YYYY'))"
    try:
        cursor.execute(sql_query, (lista_de_dados_paciente[0], lista_de_dados_paciente[1], lista_de_dados_paciente[2], lista_de_dados_paciente[3]))
        conn.commit()
        print("Registro do paciente inserido com sucesso.")
    except Exception as e:
        print(f"Erro no registro do paciente: {e}")
    finally:
        cursor.close()
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
        cursor.execute(sql_query, (lista_de_dados_ramo[0], lista_de_dados_ramo[1]))
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
    CREATE TABLE TB_EMPRESA(
    ID_EMPRESA NUMBER(19,0),
    NM_EMPRESA VARCHAR2(255),
    E_MAIL VARCHAR(50),
    NR_CNPJ VARCHAR2(14),
    RAMO NUMBER(19,0),
    CONSTRAINT PK_ID_EMPRESA PRIMARY KEY (ID_EMPRESA),
    CONSTRAINT fk_TB_EMPRESA_TB_RAMO FOREIGN KEY (RAMO) REFERENCES TB_RAMO(ID_RAMO)
    )"""
    try:
        cursor.execute(sql_EMPRESA)
        print("Tabela EMPRESSA criada")
    except Exception as e:
        print(f"Erro ao criar a tabela EMPRESA: {e}")
    finally:
        cursor.close()
        conn.close()


def cadastrarEmpresa():
    print("Cadastre uma empresa!")
    lista_de_dados_empresa = []
    ID_EMPRESA = int(input("id: "))
    lista_de_dados_empresa.append(ID_EMPRESA)

    NM_EMPRESA = input("Nome da empresa: ")
    lista_de_dados_empresa.append(NM_EMPRESA)

    E_MAIL = input("Digite o email da empresa: ")
    lista_de_dados_empresa.append(E_MAIL)

    NR_CNPJ = input("Digite o cnpj da empresa: ")
    lista_de_dados_empresa.append(NR_CNPJ)

    RAMO = int(input("Digite o ramo da empresa: "))
    lista_de_dados_empresa.append(RAMO)

    return lista_de_dados_empresa


def INSERIR_DADOS_EMPRESA(lista_de_dados_empresa):
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "INSERT INTO TB_EMPRESA (ID_EMPRESA, NM_EMPRESA, E_MAIL, NR_CNPJ, RAMO) VALUES (:0, :1, :2, :3, :4)"
    try:
        cursor.execute(sql_query, (lista_de_dados_empresa[0], lista_de_dados_empresa[1], lista_de_dados_empresa[2], lista_de_dados_empresa[3], lista_de_dados_empresa[4]))
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


def CREATE_TABLE_FUNCIONARIO():
    conn = getConnection()
    cursor = conn.cursor()
    sql_FUNCIONARIO = """
    CREATE TABLE TB_FUNCIONARIOS(
    ID_FUNCIONARIO NUMBER(19,0),
    NM_FUNCIONARIO VARCHAR2(255),
    NR_CPF VARCHAR2(11),
    SETOR VARCHAR2(255),
    EMPRESA NUMBER(19,0),
    CONSTRAINT PK_ID_FUNCIONARIO PRIMARY KEY (ID_FUNCIONARIO),
    CONSTRAINT fk_TB_FUNCIONARIOS_TB_EmpresaTerceira FOREIGN KEY (EMPRESA) REFERENCES TB_EMPRESA(ID_EMPRESA)
    )"""
    try:
        cursor.execute(sql_FUNCIONARIO)
        print("Tabela FUNCIONARIO criada")
    except Exception as e:
        print(f"Erro ao criar a tabela FUNCIONARIO: {e}")
    finally:
        cursor.close()
        conn.close()

def cadastrarFuncionario():
    print("Cadastre um funcionario de determinada empresa")
    lista_de_dados_funcionario = []
    ID_FUNCIONARIO = int(input("id: "))
    lista_de_dados_funcionario.append(ID_FUNCIONARIO)

    NM_FUNCIONARIO = input("Nome do funcionario")
    lista_de_dados_funcionario.append(NM_FUNCIONARIO)

    NR_CPF = input("Numero do cpf")
    lista_de_dados_funcionario.append(NR_CPF)

    SETOR = input("Digite o setor do funcionario")
    lista_de_dados_funcionario.append(SETOR)

    EMPRESA = int(input("insira o ID da empresa: "))
    lista_de_dados_funcionario.append(EMPRESA)

    return lista_de_dados_funcionario

def INSERIR_DADOS_FUNCIONARIO(lista_de_dados_funcionario):
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "INSERT INTO TB_FUNCIONARIOS (ID_FUNCIONARIO, NM_FUNCIONARIO, NR_CPF, SETOR, EMPRESA) VALUES (:0, :1, :2, :3, :4)"
    try:
        cursor.execute(sql_query, (lista_de_dados_funcionario[0], lista_de_dados_funcionario[1], lista_de_dados_funcionario[2], lista_de_dados_funcionario[3], lista_de_dados_funcionario[4]))
        conn.commit()
        print("Registro do funcionário inserido com sucesso.")
    except Exception as e:
        print(f"Erro ao inserir o registro do funcionário: {e}")
    finally:
        cursor.close()
        conn.close()

def DROP_TABLE_FUNCIONARIO():
    conn = getConnection()
    cursor = conn.cursor()
    sql_enderecodrop = """
    DROP TABLE FUNCIONARIO
    """
    try:
        cursor.execute(sql_enderecodrop)
        print("tabela FUNCIONARIO dropada")
    except Exception as e:
        print(f"Erro ao dropar a tabela FUNCIONARIO: {e}")
    finally:
        cursor.close
        conn.close

def CREATE_TABLE_SERVICO():
    conn = getConnection()
    cursor = conn.cursor()
    sql_SERVICO = """
    CREATE TABLE TB_SERVICOS(
    ID_SERVICO NUMBER(19,0),
    DS_SERVICO VARCHAR2(255),
    TIPO VARCHAR2(255),
    CONSTRAINT PK_ID_SERVICO PRIMARY KEY (ID_SERVICO)
    )"""
    try:
        cursor.execute(sql_SERVICO)
        print("tabela SERVICO criada")
    except Exception as e:
        print(f"Erro ao criar a tabela SERVICO: {e}")
    finally:
        cursor.close()
        conn.close()

def cadastrarServico():
    print("Cadastre um servico")
    lista_de_dados_servico = []
    ID_SERVICO = int(input("id: "))
    lista_de_dados_servico.append(ID_SERVICO)

    DS_SERVICO = input("Descrição do serviço: ")
    lista_de_dados_servico.append(DS_SERVICO)

    TIPO = input("Tipo do serviço: ")
    lista_de_dados_servico.append(TIPO)

    return lista_de_dados_servico

def INSERIR_DADOS_SERVICO(lista_de_dados_servico):
    conn = getConnection()
    cursor = conn.cursor()
    sql_query ="INSERT INTO TB_SERVICOS (ID_SERVICO, DS_SERVICO, TIPO) VALUES (:0, :1, :2)"
    try:
        cursor.execute(sql_query, (lista_de_dados_servico[0], lista_de_dados_servico[1], lista_de_dados_servico[2]))
        conn.commit()
        print("Registro do serviço inserido com sucesso.")
    except Exception as e:
        print(f"Erro ao inserir o registro do serviço: {e}")
    finally:
        cursor.close()
        conn.close()

def DROP_TABLE_SERVICO():
    conn = getConnection()
    cursor = conn.cursor()
    sql_enderecodrop = """
    DROP TABLE SERVICO
    """
    try:
        cursor.execute(sql_enderecodrop)
        print("tabela SERVICO dropada")
    except Exception as e:
        print(f"Erro ao dropar a tabela SERVICO: {e}")
    finally:
        cursor.close
        conn.close

def main():
    while True:
        CREATE_TABLE_AREA()
        lista_de_dados_area = cadastrarArea()
        INSERIR_DADOS_AREA(lista_de_dados_area)

        selecao = int(input("Escolha uma opção:\n1. Cadastrar Empresa e Paciente\n2. Cadastrar Funcionário\n3. Encerrar\n"))

        if selecao == 1:
            CREATE_TABLE_EMPRESA()
            lista_de_dados_empresa = cadastrarEmpresa()
            INSERIR_DADOS_EMPRESA(lista_de_dados_empresa)

            CREATE_TABLE_PACIENTE()
            lista_de_dados_paciente = cadastrarPaciente()
            INSERIR_DADOS_PACIENTE(lista_de_dados_paciente)

        elif selecao == 2:
            CREATE_TABLE_FUNCIONARIO()
            lista_de_dados_funcionario = cadastrarFuncionario()
            INSERIR_DADOS_FUNCIONARIO(lista_de_dados_funcionario)

        elif selecao == 3:
            print("Encerrando o programa.")
            break  # Sai do loop

        else:
            print("Opção inválida.")

        selecao_menu = int(input("Escolha uma opção:\n1. Cadastrar Serviço\n2. Cadastrar Área\n3. Cadastrar Ramo\n4. Encerrar\n"))

        if selecao_menu == 1:
            CREATE_TABLE_SERVICO()
            lista_de_dados_servico = cadastrarServico()
            INSERIR_DADOS_SERVICO(lista_de_dados_servico)

        elif selecao_menu == 2:
            CREATE_TABLE_AREA()
            lista_de_dados_area = cadastrarArea()
            INSERIR_DADOS_AREA(lista_de_dados_area)

        elif selecao_menu == 3:
            CREATE_TABLE_RAMO()
            lista_de_dados_ramo = cadastrarRamo()
            INSERIR_DADOS_RAMO(lista_de_dados_ramo)

        elif selecao_menu == 4:
            print("Encerrando o programa.")
            break  # Sai do loop

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

# Exemplo de uso
main()

'''
DROP_TABLE_AREA()
DROP_TABLE_PACIENTE()
DROP_TABLE_RAMO()
DROP_TABLE_FUNCIONARIO()
DROP_TABLE_EMPRESA()
DROP_TABLE_SERVICO()
'''