import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_21_12")


def getConnection():
    try:
        connection = cx_Oracle.connect("RM94164", "200101", "oracle.fiap.com.br/ORCL")
        # connection = cx_Oracle.connect(user="a", password="b", host="c", port="1521", service="ORCL")
        print("conexão: ", connection.version)
        return connection
    except Exception as e:
        print(f'Erro ao obter conexão: {e}')


"""1 - pesquisar por ID"""


def findById_tbAreas():
    conn = getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input("Digite o ID desejado: "))
    sql_id = f"""
    SELECT * FROM TB_AREAS WHERE id_usario = {id_escolhido}
    )"""
    try:
        cursor.execute(sql_id)
        print("ID enconstrado com sucesso")
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f"ID não encontrado: {e}")
    finally:
        cursor.close()
        conn.close()


def findById_tbPaciente():
    conn = getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input("Digite o ID desejado: "))
    sql_id = f"""
    SELECT * FROM TB_PACIENTE WHERE id_usario = {id_escolhido}
    )"""
    try:
        cursor.execute(sql_id)
        print("ID enconstrado com sucesso")
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f"ID não encontrado: {e}")
    finally:
        cursor.close()
        conn.close()


def findById_tbEmpersa():
    conn = getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input("Digite o ID desejado: "))
    sql_id = f"""
    SELECT * FROM TB_EMPRESA WHERE id_usario = {id_escolhido}
    )"""
    try:
        cursor.execute(sql_id)
        print("ID enconstrado com sucesso")
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f"ID não encontrado: {e}")
    finally:
        cursor.close()
        conn.close()


def findById_tbRamo():
    conn = getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input("Digite o ID desejado: "))
    sql_id = f"""
    SELECT * FROM TB_RAMO WHERE id_usario = {id_escolhido}
    )"""
    try:
        cursor.execute(sql_id)
        print("ID enconstrado com sucesso")
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f"ID não encontrado: {e}")
    finally:
        cursor.close()
        conn.close()


def findById_tbServico():
    conn = getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input("Digite o ID desejado: "))
    sql_id = f"""
    SELECT * FROM TB_SERVICOS WHERE id_usario = {id_escolhido}
    )"""
    try:
        cursor.execute(sql_id)
        print("ID enconstrado com sucesso")
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f"ID não encontrado: {e}")
    finally:
        cursor.close()
        conn.close()


def findById_tbFuncionarios():
    conn = getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input("Digite o ID desejado: "))
    sql_id = f"""
    SELECT * FROM TB_FUNCIONARIOS WHERE id_usario = {id_escolhido}
    )"""
    try:
        cursor.execute(sql_id)
        print("ID enconstrado com sucesso")
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f"ID não encontrado: {e}")
    finally:
        cursor.close()
        conn.close()


"""2. Tudo que tem na tabela"""


def getAll_tbAreas():
    conn = getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    SELECT * FROM TB_AREAS
    """
    try:
        cursor.execute(sql_getAll)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f'Erro ao trazer informações da tabela: {e}')
    finally:
        cursor.close()
        conn.close()


def getAll_tbPaciente():
    conn = getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    SELECT * FROM tb_PACIENTE
    """
    try:
        cursor.execute(sql_getAll)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f'Erro ao trazer informações da tabela: {e}')
    finally:
        cursor.close()
        conn.close()


def getAll_tbEmpresa():
    conn = getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    SELECT * FROM TB_EMPRESA
    """
    try:
        cursor.execute(sql_getAll)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f'Erro ao trazer informações da tabela: {e}')
    finally:
        cursor.close()
        conn.close()


def getAll_tbRamo():
    conn = getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    SELECT * FROM TB_RAMO
    """
    try:
        cursor.execute(sql_getAll)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f'Erro ao trazer informações da tabela: {e}')
    finally:
        cursor.close()
        conn.close()


def getAll_tbServico():
    conn = getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    SELECT * FROM TB_SERVICOS
    """
    try:
        cursor.execute(sql_getAll)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f'Erro ao trazer informações da tabela: {e}')
    finally:
        cursor.close()
        conn.close()


def getAll_tbFuncionarios():
    conn = getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    SELECT * FROM TB_FUNCIONARIOS
    """
    try:
        cursor.execute(sql_getAll)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f'Erro ao trazer informações da tabela: {e}')
    finally:
        cursor.close()
        conn.close()


"""3.Delete por ID"""


def deleteById_tbAreas():
    conn = getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input('Digite o ID desejado: '))
    sql_id = f"""
    DELETE FROM TB_AREAS WHERE id_usuario = {id_escolhido}
"""
    try:
        cursor.execute(sql_id)
        print(f'Informações do ID {id_escolhido} apagado com sucesso!')
    except Exception as e:
        print(f'Erro ao deletar as informações do ID {id_escolhido}: {e}')
    finally:
        cursor.close
        conn.close


def deleteById_tbPaciente():
    conn = getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input('Digite o ID desejado: '))
    sql_id = f"""
    DELETE FROM TB_PACIENTE WHERE id_usuario = {id_escolhido}
"""
    try:
        cursor.execute(sql_id)
        print(f'Informações do ID {id_escolhido} apagado com sucesso!')
    except Exception as e:
        print(f'Erro ao deletar as informações do ID {id_escolhido}: {e}')
    finally:
        cursor.close
        conn.close


def deleteById_tbEmpresa():
    conn = getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input('Digite o ID desejado: '))
    sql_id = f"""
    DELETE FROM TB_EMPRESA WHERE id_usuario = {id_escolhido}
"""
    try:
        cursor.execute(sql_id)
        print(f'Informações do ID {id_escolhido} apagado com sucesso!')
    except Exception as e:
        print(f'Erro ao deletar as informações do ID {id_escolhido}: {e}')
    finally:
        cursor.close
        conn.close


def deleteById_tbRamo():
    conn = getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input('Digite o ID desejado: '))
    sql_id = f"""
    DELETE FROM TB_RAMO WHERE id_usuario = {id_escolhido}
"""
    try:
        cursor.execute(sql_id)
        print(f'Informações do ID {id_escolhido} apagado com sucesso!')
    except Exception as e:
        print(f'Erro ao deletar as informações do ID {id_escolhido}: {e}')
    finally:
        cursor.close
        conn.close


def deleteById_tbServicos():
    conn = getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input('Digite o ID desejado: '))
    sql_id = f"""
    DELETE FROM TB_SERVICOS WHERE id_usuario = {id_escolhido}
"""
    try:
        cursor.execute(sql_id)
        print(f'Informações do ID {id_escolhido} apagado com sucesso!')
    except Exception as e:
        print(f'Erro ao deletar as informações do ID {id_escolhido}: {e}')
    finally:
        cursor.close
        conn.close


def deleteById_tbFuncionarios():
    conn = getConnection()
    cursor = conn.cursor()
    id_escolhido = int(input('Digite o ID desejado: '))
    sql_id = f"""
    DELETE FROM TB_FUNCIONARIOS WHERE id_usuario = {id_escolhido}
"""
    try:
        cursor.execute(sql_id)
        print(f'Informações do ID {id_escolhido} apagado com sucesso!')
    except Exception as e:
        print(f'Erro ao deletar as informações do ID {id_escolhido}: {e}')
    finally:
        cursor.close
        conn.close


"""4. DELETE ALL"""


def deleteAll_tbArea():
    conn = getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    DELETE FROM TB_AREAS
        """
    try:
        cursor.execute(sql_getAll)
        print(sql_getAll)
    except Exception as e:
        print(f'Erro ao deletar as informações da tabela: {e}')
    finally:
        cursor.close
        conn.close


def deleteAll_tbPaciente():
    conn = getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    DELETE FROM TB_PACIENTE
        """
    try:
        cursor.execute(sql_getAll)
        print(sql_getAll)
    except Exception as e:
        print(f'Erro ao deletar as informações da tabela: {e}')
    finally:
        cursor.close
        conn.close


def deleteAll_tbEmpresa():
    conn = getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    DELETE FROM TB_EMPRESA
        """
    try:
        cursor.execute(sql_getAll)
        print(sql_getAll)
    except Exception as e:
        print(f'Erro ao deletar as informações da tabela: {e}')
    finally:
        cursor.close
        conn.close


def deleteAll_tbRamo():
    conn = getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    DELETE FROM TB_RAMO
        """
    try:
        cursor.execute(sql_getAll)
        print(sql_getAll)
    except Exception as e:
        print(f'Erro ao deletar as informações da tabela: {e}')
    finally:
        cursor.close
        conn.close


def deleteAll_tbServico():
    conn = getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    DELETE FROM TB_SERVICOS
        """
    try:
        cursor.execute(sql_getAll)
        print(sql_getAll)
    except Exception as e:
        print(f'Erro ao deletar as informações da tabela: {e}')
    finally:
        cursor.close
        conn.close


def deleteAll_tbFuncionario():
    conn = getConnection()
    cursor = conn.cursor()
    sql_getAll = """
    DELETE FROM TB_FUNCIONARIOS
        """
    try:
        cursor.execute(sql_getAll)
        print(sql_getAll)
    except Exception as e:
        print(f'Erro ao deletar as informações da tabela: {e}')
    finally:
        cursor.close
        conn.close


def update_tbArea():
    conn = getConnection()
    cursor = conn.cursor()

    try:
        id_escolhido = int(input('Digite o ID desejado: '))
        area = input('Área que deseja cadastrar em nosso banco: ')
        sql_update = f"""
            UPDATE TB_AREAS
            SET area = ?
            WHERE ID_AREA = ?
        """
        cursor.execute(sql_update, (area, id_escolhido))
        conn.commit()
        print("Informações atualizadas com sucesso!")
    except Exception as e:
        print(f'Erro ao atualizar as informações: {e}')
    finally:
        cursor.close()
        conn.close()


def update_tbPaciente():
    conn = getConnection()
    cursor = conn.cursor()

    try:
        id_escolhido = int(input('Digite o ID desejado: '))
        nome = input('Nome do paciente que deseja cadastrar em nosso banco: ')
        sql_update = """
            UPDATE TB_PACIENTE
            SET nome = ?, CPF = 'xxx.xxx.xxx-xx'
            WHERE ID_PACIENTE = ?
        """
        cursor.execute(sql_update, (nome, id_escolhido))
        conn.commit()

        print("Informações atualizadas com sucesso!")
    except Exception as e:
        print(f'Erro ao atualizar as informações: {e}')
    finally:
        cursor.close()
        conn.close()


def update_tbEmpresa():
    conn = getConnection()
    cursor = conn.cursor()

    try:
        id_escolhido = int(input('Digite o ID desejado: '))
        empresa = input('Empresa terceira que deseja cadastrar em nosso banco: ')
        sql_update = """
            UPDATE TB_EMPRESA
            SET empresa = ?, email = 'novo@email.com'
            WHERE ID_EMPRESA = ?
        """
        cursor.execute(sql_update, (empresa, id_escolhido))
        conn.commit()
        print("Informações atualizadas com sucesso!")
    except Exception as e:
        print(f'Erro ao atualizar as informações: {e}')
    finally:
        cursor.close()
        conn.close()


def update_tbRamo():
    conn = getConnection()
    cursor = conn.cursor()

    try:
        id_escolhido = int(input('Digite o ID desejado: '))
        nome = input('Ramo que deseja cadastrar em nosso banco: ')

        sql_update = """
            UPDATE TB_RAMO
            SET nome = ? WHERE ID_RAMO = ?
        """
        cursor.execute(sql_update, (nome, id_escolhido))
        conn.commit()
        print("Informações atualizadas com sucesso!")
    except Exception as e:
        print(f'Erro ao atualizar as informações: {e}')
    finally:
        cursor.close()
        conn.close()


def update_tbServico():
    conn = getConnection()
    cursor = conn.cursor()

    try:
        id_escolhido = int(input('Digite o ID desejado: '))
        nome = input('Serviço que deseja cadastrar em nosso banco: ')
        sql_update = """
            UPDATE TB_SERVICOS
            SET nome = ? WHERE ID_SERVICO = ?
        """
        cursor.execute(sql_update, (nome, id_escolhido))
        conn.commit()

        print("Informações atualizadas com sucesso!")
    except Exception as e:
        print(f'Erro ao atualizar as informações: {e}')
    finally:
        cursor.close()
        conn.close()


def update_tbFuncionario():
    conn = getConnection()
    cursor = conn.cursor()

    try:
        id_escolhido = int(input('Digite o ID desejado: '))
        nome = input('Nome do funcionário que deseja cadastrar em nosso banco: ')

        sql_update = """
            UPDATE FUNCIONARIOS
            SET nome = ? WHERE ID_FUNCIONARIO = ?
        """
        cursor.execute(sql_update, (nome, id_escolhido))
        conn.commit()

        print("Informações atualizadas com sucesso!")
    except Exception as e:
        print(f'Erro ao atualizar as informações: {e}')
    finally:
        cursor.close()
        conn.close()


"""6. informções dadas pelo o usario"""


def cadastrarArea():
    lista_de_dados_area = []

    ID_AREA = int(input("id:"))
    lista_de_dados_area.append(ID_AREA)

    REGIAO = input("Digite a região requirida: ")
    lista_de_dados_area.append(REGIAO)

    CEP = input("Digite o CEP da região: ")
    lista_de_dados_area.append(CEP)

    return lista_de_dados_area


def cadastrarPaciente():
    print("Faça seu cadastro para saber o seu resultado")
    lista_de_dados_paciente = []
    ID_PACIENTE = int(input("id: "))
    lista_de_dados_paciente.append(ID_PACIENTE)

    NM_PACIENTE = input("Nome: ")
    lista_de_dados_paciente.append(NM_PACIENTE)

    CPF = input("CPF: ")
    lista_de_dados_paciente.append(CPF)

    DT_NASCIMENTO = input("Data de nascimento: ")
    lista_de_dados_paciente.append(DT_NASCIMENTO)

    return lista_de_dados_paciente


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


def cadastrarRamo():
    print("Cadastre um ramo a seguir")
    lista_de_dados_ramo = []
    ID_RAMO = int(input("id: "))
    lista_de_dados_ramo.append(ID_RAMO)

    NM_RAMO = input("digite o nome do rmao: ")
    lista_de_dados_ramo.append(NM_RAMO)

    return lista_de_dados_ramo


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


"""7. INSERTS"""


def insert_area(local_area):
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "INSERT INTO TB_AREA (ID_AREA , LOCAL) VALUES (:0, :1)"
    try:
        cursor.execute("SELECT SQ_AREA.NEXTVAL FROM dual")
        nextval_result = cursor.fetchone()
        if nextval_result:
            area_id = nextval_result[0]
            cursor.execute(sql_query, (area_id, local_area))
            conn.commit()
            print("Registro da area inserido com sucesso. ID da area:", area_id)
        else:
            print("Erro ao obter o próximo valor da sequência")
    except Exception as e:
        print(f'Erro ao inserir o registro da area: {e}')
    finally:
        cursor.close()
        conn.close()


def insert_paciente(nome_paciente, cpf_paciente, nascimento_paciente):
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "INSERT INTO TB_PACIENTE (ID_PACIENTE, NM_PACIENTE, CPF, NASCIMENTO) VALUES (:0, :1, :2, :3)"
    try:
        cursor.execute("SELECT SQ_PACIENTE.NEXTVAL FROM dual")
        nextval_result = cursor.fetchone()
        if nextval_result:
            paciente_id = nextval_result[0]
            cursor.execute(sql_query, (paciente_id, nome_paciente, cpf_paciente, nascimento_paciente))
            conn.commit()
            print("Registro do paciente inserido com sucesso. ID do paciente:", paciente_id)
        else:
            print("Erro ao obter o próximo valor da sequência")
    except Exception as e:
        print(f'Erro ao inserir o registro do paciente: {e}')
    finally:
        cursor.close()
        conn.close()


def insert_empresa(nome_empresa, cnpj_empreja, ramo_empresa):
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "INSERT INTO TB_EMPRESA (ID_EMPRESA, NM_EMPRESA, NR_CNPJ, RAMO ) VALUES (:0, :1, :2, :3)"
    try:
        cursor.execute("SELECT SQ_EMPRESA.NEXTVAL FROM dual")
        nextval_result = cursor.fetchone()
        if nextval_result:
            empresa_id = nextval_result[0]
            cursor.execute(sql_query, (empresa_id, nome_empresa, cnpj_empreja, ramo_empresa))
            conn.commit()
            print("Registro da empresa inserido com sucesso. ID da empresa:", empresa_id)
        else:
            print("Erro ao obter o próximo valor da sequência")
    except Exception as e:
        print(f'Erro ao inserir o registro da empresa: {e}')
    finally:
        cursor.close()
        conn.close()


def insert_ramo(nome_ramo):
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "INSERT INTO TB_RAMO (ID_RAMO, NM_RAMO) VALUES (:0, :1)"
    try:
        cursor.execute("SELECT SQ_RAMO.NEXTVAL FROM dual")
        nextval_result = cursor.fetchone()
        if nextval_result:
            ramo_id = nextval_result[0]
            cursor.execute(sql_query, (ramo_id, nome_ramo))
            conn.commit()
            print("Registro do ramo inserido com sucesso. ID do ramo:", ramo_id)
        else:
            print("Erro ao obter o próximo valor da sequência")
    except Exception as e:
        print(f'Erro ao inserir o registro do ramo: {e}')
    finally:
        cursor.close()
        conn.close()


def insert_servico(descricao_servico, tipo_servico):
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "INSERT INTO TB_SERVICOS (ID_SERVICO, DS_SERVICO, TIPO) VALUES (:0, :1, :2)"
    try:
        cursor.execute("SELECT SQ_SERVICO.NEXTVAL FROM dual")
        nextval_result = cursor.fetchone()
        if nextval_result:
            servico_id = nextval_result[0]
            cursor.execute(sql_query, (servico_id, descricao_servico, tipo_servico))
            conn.commit()
            print("Registro do serviço inserido com sucesso. ID do serviço:", servico_id)
        else:
            print("Erro ao obter o próximo valor da sequência")
    except Exception as e:
        print(f'Erro ao inserir o registro do serviço: {e}')
    finally:
        cursor.close()
        conn.close()


def insert_area(nome_funcionario, cpf_funcionario, setor_funcionario, empresa_funcionario):
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "INSERT INTO TB_FUNCIONARIOS (ID_FUNCIONARIO, NM_FUNCIONARIO, NR_CPF, SETOR, EMPRESA) VALUES (:0, :1, :2, :3, :4)"
    try:
        cursor.execute("SELECT SQ_FUNCIONARIO.NEXTVAL FROM dual")
        nextval_result = cursor.fetchone()
        if nextval_result:
            funcionario_id = nextval_result[0]
            cursor.execute(sql_query,
                           (funcionario_id, nome_funcionario, cpf_funcionario, setor_funcionario, empresa_funcionario))
            conn.commit()
            print("Registro do funcionario inserido com sucesso. ID do funcionario:", funcionario_id)
        else:
            print("Erro ao obter o próximo valor da sequência")
    except Exception as e:
        print(f'Erro ao inserir o registro do funcionario: {e}')
    finally:
        cursor.close()
        conn.close()


def menu():
    print("""

Qual operação deseja fazer?

1 - tbArea
2 - tbPaciente
3 - tbEmpresa
4 - tbRamo
5 - tbServico
6 - tbFuncionario          

""")
    op = 0
    while op == 0:
        try:
            escolha = int(input('Digite a opção desejada: '))

            if escolha < 1 or escolha > 5:
                print('Opção invalida, digite novamente!')
                op = 0
            elif escolha == 1:
                tbArea()

            elif escolha == 2:
                tbPaciente()

            elif escolha == 3:
                tbEmpresa()

            elif escolha == 4:
                tbRamo()

            elif escolha == 5:
                tbServico()

            elif escolha == 6:
                tbFuncionario()

        except ValueError:
            print('Opção inválida. Por favor, digite um número.')
            op = 0


def tbArea():
    op = 0
    while op == 0:
        print("""
    Qual operação deseja fazer?
    1 - Consutar Id.
    2 - Consutar tabela inteira.
    3 - Fazer Update de informação
    4 - Deletar Id.
    5 - Deletar tudo.
    """)
        try:
            escolha = int(input('Digite a opção desejada: '))

            if escolha < 1 or escolha > 5:
                print('Opção invalida, digite novamente!')
                op = 0
            elif escolha == 1:
                findById_tbAreas()

            elif escolha == 2:
                getAll_tbAreas()

            elif escolha == 3:
                update_tbArea()

            elif escolha == 4:
                deleteById_tbAreas()

            elif escolha == 5:
                deleteAll_tbArea()
            print('''
    Deseja algo a mais nessa tabela?
    1 - sim
    2 - não
            ''')
            try:
                res = 0
                while res == 0:
                    opcao = int(input('Digite a opção desejada: '))

                    if opcao == 1:
                        res = 1
                        op = 0
                    elif opcao == 2:
                        print('''
    Deseja algo a mais nessa tabela?
    1 - sim
    2 - não
                        ''')
                        try:
                            resposta = 0
                            while resposta == 0:
                                opc = int(input('Digite a opção desejada: '))
                                if opc == 1:
                                    menu()
                                    resposta == 1
                                    res = 1
                                    op = 1
                                elif opc == 2:
                                    break

                                elif opc != 1 or opc != 2:
                                    print('Opção invalida, digite novamente!')
                        except ValueError:
                            print('Opção inválida. Por favor, digite um número.')
            except ValueError:
                print('Opção inválida. Por favor, digite um número.')
        except ValueError:
            print('Opção inválida. Por favor, digite um número.')
            op = 0


def tbPaciente():
    op = 0
    while op == 0:
        print("""
    Qual operação deseja fazer?
    1 - Consutar Id.
    2 - Consutar tabela inteira.
    3 - Fazer Update de informação
    4 - Deletar Id.
    5 - Deletar tudo.
    """)
        try:
            escolha = int(input('Digite a opção desejada: '))

            if escolha < 1 or escolha > 5:
                print('Opção invalida, digite novamente!')
                op = 0
            elif escolha == 1:
                findById_tbPaciente()

            elif escolha == 2:
                getAll_tbPaciente()

            elif escolha == 3:
                update_tbPaciente()

            elif escolha == 4:
                deleteById_tbPaciente()

            elif escolha == 5:
                deleteAll_tbPaciente()
            print('''
    Deseja algo a mais nessa tabela?
    1 - sim
    2 - não
            ''')
            try:
                res = 0
                while res == 0:
                    opcao = int(input('Digite a opção desejada: '))

                    if opcao == 1:
                        res = 1
                        op = 0
                    elif opcao == 2:
                        print('''
    Deseja algo a mais nessa tabela?
    1 - sim
    2 - não
                        ''')
                        try:
                            resposta = 0
                            while resposta == 0:
                                opc = int(input('Digite a opção desejada: '))
                                if opc == 1:
                                    menu()
                                    resposta == 1
                                    res = 1
                                    op = 1
                                elif opc == 2:
                                    break

                                elif opc != 1 or opc != 2:
                                    print('Opção invalida, digite novamente!')
                        except ValueError:
                            print('Opção inválida. Por favor, digite um número.')
            except ValueError:
                print('Opção inválida. Por favor, digite um número.')
        except ValueError:
            print('Opção inválida. Por favor, digite um número.')
            op = 0


def tbEmpresa():
    op = 0
    while op == 0:
        print("""
    Qual operação deseja fazer?
    1 - Consutar Id.
    2 - Consutar tabela inteira.
    3 - Fazer Update de informação
    4 - Deletar Id.
    5 - Deletar tudo.
    """)
        try:
            escolha = int(input('Digite a opção desejada: '))

            if escolha < 1 or escolha > 5:
                print('Opção invalida, digite novamente!')
                op = 0
            elif escolha == 1:
                findById_tbEmpersa()

            elif escolha == 2:
                getAll_tbEmpresa()

            elif escolha == 3:
                update_tbEmpresa()

            elif escolha == 4:
                deleteById_tbEmpresa()

            elif escolha == 5:
                deleteAll_tbEmpresa()
            print('''
    Deseja algo a mais nessa tabela?
    1 - sim
    2 - não
            ''')
            try:
                res = 0
                while res == 0:
                    opcao = int(input('Digite a opção desejada: '))

                    if opcao == 1:
                        res = 1
                        op = 0
                    elif opcao == 2:
                        print('''
    Deseja algo a mais nessa tabela?
    1 - sim
    2 - não
                        ''')
                        try:
                            resposta = 0
                            while resposta == 0:
                                opc = int(input('Digite a opção desejada: '))
                                if opc == 1:
                                    menu()
                                    resposta == 1
                                    res = 1
                                    op = 1
                                elif opc == 2:
                                    break

                                elif opc != 1 or opc != 2:
                                    print('Opção invalida, digite novamente!')
                        except ValueError:
                            print('Opção inválida. Por favor, digite um número.')
            except ValueError:
                print('Opção inválida. Por favor, digite um número.')
        except ValueError:
            print('Opção inválida. Por favor, digite um número.')
            op = 0


def tbRamo():
    op = 0
    while op == 0:
        print("""
    Qual operação deseja fazer?
    1 - Consutar Id.
    2 - Consutar tabela inteira.
    3 - Fazer Update de informação
    4 - Deletar Id.
    5 - Deletar tudo.
    """)
        try:
            escolha = int(input('Digite a opção desejada: '))

            if escolha < 1 or escolha > 5:
                print('Opção invalida, digite novamente!')
                op = 0
            elif escolha == 1:
                findById_tbRamo()

            elif escolha == 2:
                getAll_tbRamo()

            elif escolha == 3:
                update_tbRamo()

            elif escolha == 4:
                deleteById_tbRamo()

            elif escolha == 5:
                deleteAll_tbRamo()
            print('''
    Deseja algo a mais nessa tabela?
    1 - sim
    2 - não
            ''')
            try:
                res = 0
                while res == 0:
                    opcao = int(input('Digite a opção desejada: '))

                    if opcao == 1:
                        res = 1
                        op = 0
                    elif opcao == 2:
                        print('''
    Deseja algo a mais nessa tabela?
    1 - sim
    2 - não
                        ''')
                        try:
                            resposta = 0
                            while resposta == 0:
                                opc = int(input('Digite a opção desejada: '))
                                if opc == 1:
                                    menu()
                                    resposta == 1
                                    res = 1
                                    op = 1
                                elif opc == 2:
                                    break

                                elif opc != 1 or opc != 2:
                                    print('Opção invalida, digite novamente!')
                        except ValueError:
                            print('Opção inválida. Por favor, digite um número.')
            except ValueError:
                print('Opção inválida. Por favor, digite um número.')
        except ValueError:
            print('Opção inválida. Por favor, digite um número.')
            op = 0


def tbServico():
    op = 0
    while op == 0:
        print("""
    Qual operação deseja fazer?
    1 - Consutar Id.
    2 - Consutar tabela inteira.
    3 - Fazer Update de informação
    4 - Deletar Id.
    5 - Deletar tudo.
    """)
        try:
            escolha = int(input('Digite a opção desejada: '))

            if escolha < 1 or escolha > 5:
                print('Opção invalida, digite novamente!')
                op = 0
            elif escolha == 1:
                findById_tbServico()

            elif escolha == 2:
                getAll_tbServico()

            elif escolha == 3:
                update_tbServico()

            elif escolha == 4:
                deleteById_tbServicos()

            elif escolha == 5:
                deleteAll_tbServico()
            print('''
    Deseja algo a mais nessa tabela?
    1 - sim
    2 - não
            ''')
            try:
                res = 0
                while res == 0:
                    opcao = int(input('Digite a opção desejada: '))

                    if opcao == 1:
                        res = 1
                        op = 0
                    elif opcao == 2:
                        print('''
    Deseja algo a mais nessa tabela?
    1 - sim
    2 - não
                        ''')
                        try:
                            resposta = 0
                            while resposta == 0:
                                opc = int(input('Digite a opção desejada: '))
                                if opc == 1:
                                    menu()
                                    resposta == 1
                                    res = 1
                                    op = 1
                                elif opc == 2:
                                    break

                                elif opc != 1 or opc != 2:
                                    print('Opção invalida, digite novamente!')
                        except ValueError:
                            print('Opção inválida. Por favor, digite um número.')
            except ValueError:
                print('Opção inválida. Por favor, digite um número.')
        except ValueError:
            print('Opção inválida. Por favor, digite um número.')
            op = 0


def tbFuncionario():
    op = 0
    while op == 0:
        print("""
    Qual operação deseja fazer?
    1 - Consutar Id.
    2 - Consutar tabela inteira.
    3 - Fazer Update de informação
    4 - Deletar Id.
    5 - Deletar tudo.
    """)
        try:
            escolha = int(input('Digite a opção desejada: '))

            if escolha < 1 or escolha > 5:
                print('Opção invalida, digite novamente!')
                op = 0
            elif escolha == 1:
                findById_tbFuncionarios()

            elif escolha == 2:
                getAll_tbFuncionarios()

            elif escolha == 3:
                update_tbFuncionario()

            elif escolha == 4:
                deleteById_tbFuncionarios()

            elif escolha == 5:
                deleteAll_tbFuncionario()
            print('''
    Deseja algo a mais nessa tabela?
    1 - sim
    2 - não
            ''')
            try:
                res = 0
                while res == 0:
                    opcao = int(input('Digite a opção desejada: '))

                    if opcao == 1:
                        res = 1
                        op = 0
                    elif opcao == 2:
                        print('''
    Deseja algo a mais nessa tabela?
    1 - sim
    2 - não
                        ''')
                        try:
                            resposta = 0
                            while resposta == 0:
                                opc = int(input('Digite a opção desejada: '))
                                if opc == 1:
                                    menu()
                                    resposta == 1
                                    res = 1
                                    op = 1
                                elif opc == 2:
                                    break

                                elif opc != 1 or opc != 2:
                                    print('Opção invalida, digite novamente!')
                        except ValueError:
                            print('Opção inválida. Por favor, digite um número.')
            except ValueError:
                print('Opção inválida. Por favor, digite um número.')
        except ValueError:
            print('Opção inválida. Por favor, digite um número.')
            op = 0


# principal
menu()