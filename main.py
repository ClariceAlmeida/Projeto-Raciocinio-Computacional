"""
Clarice dos Santos Almeida
Análise e desenvolvimento de sistemas - 2024
"""
# importa a biblioteca
import json

# define os arquivos
arquivo_estudantes = "lista-de-estudantes.json"
arquivo_professores = "lista-de-professores.json"
arquivo_disciplinas = "lista-de-disciplinas.json"
arquivo_turmas = "lista-de-turmas.json"
arquivo_matriculas = "lista-de-matriculas.json"


# cria um novo arquivo
def salvar_arquivo(lista, nome_arquivo):
    """
    Cria ou sobrescreve um arquivo com os dados de uma lista
    :param lista: lista que contêm os dados
    :param nome_arquivo: nome do arquivo a ser criado
    :return: -
    """
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_aberto:
        json.dump(lista, arquivo_aberto, ensure_ascii=False)


# lê um arquivo .json
def ler_arquivo(nome_arquivo):
    """
    lê um arquivo em .json
    :param nome_arquivo: nome do arquivo a ser lido
    :return: os dados salvos naquele arquivo
    """
    try:
        with open(nome_arquivo, 'r') as arquivo_aberto:
            lista = json.load(arquivo_aberto)
        return lista
    except:
        return []


# mostra o menu principal
def menu_principal():
    """
    Printa o menu principal
    :return: input para pegar a opção desejada
    """
    print("----- MENU PRINCIPAL ----- \n"
          "\n"
          "(1) Gerenciar estudantes.\n"
          "(2) Gerenciar professores.\n"
          "(3) Gerenciar disciplinas.\n"
          "(4) Gerenciar turmas.\n"
          "(5) Gerenciar matrículas \n"
          "(6) Sair\n")
    return input("Informe a opção desejada: \n")


# mostra o menu secundário
def menu_secundario():
    """
    Printa menu secundário
    :return: input para opção desejada
    """
    print("(1) Incluir\n"
          "(2) Listar\n"
          "(3) Editar\n"
          "(4) Excluir\n"
          "(5) Voltar ao menu principal \n")
    return input("Informe a opção desejada: \n")


# valida se o CPF digitado já existe na lista
def validar_cpf(lista, estudante_cpf: str):
    """
    Valida o CPF digitado
    :param lista: procura na lista passada
    :param estudante_cpf: input do cpf do estudante
    :return: retorna false se o cpf já existir na lista de estudantes para continuar o loop
    """
    # para cada elemento procurado na lista
    for estudante_procurado in lista:
        # se o elemento de chave cpf for igual ao digitado continua o loop até ser um diferente
        if estudante_procurado["cpf"] == estudante_cpf:
            return False
    return True


# gera um id único que servirá de código para os elementos
def gerar_id_unico(lista):
    """
    Gera um ID único que não está presente na lista de dicionários.
    :param lista: Lista de dicionários onde será verificado se o ID já existe.
    :return: Um ID único.
    """
    ids_existentes = set()
    for item in lista:
        ids_existentes.add(item["id"])

    novo_id = 1
    while novo_id in ids_existentes:
        novo_id += 1

    return novo_id


# cria um novo estudante ou professor
def criar_estudante_ou_professor(nome_arquivo, pessoa_nome: str, pessoa_cpf: str):
    """
    Cria um novo nova_pessoa ou professor válido (valida através do CPF)
    :param nome_arquivo: nome do arquivo que a nova pessoa será salva
    :param pessoa_nome: Nome do aluno ou professor
    :param pessoa_cpf: CPF do aluno ou professor
    :return: Retorna uma string formatada com os dados do nova_pessoa cadastrado
   """
    lista = ler_arquivo(nome_arquivo)
    # laço para validar o cpf, só sai quando o CPF for válido
    while not validar_cpf(lista, pessoa_cpf):
        print(f'O CPF {pessoa_cpf} já está cadastrado!\nDigite um CPF válido')
        pessoa_cpf = input('Digite um novo CPF:\n')

    # cria o código do nova_pessoa
    pessoa_codigo = gerar_id_unico(lista)

    # define uma nova_pessoa
    nova_pessoa = {
        "id": pessoa_codigo,
        "nome": pessoa_nome,
        "cpf": pessoa_cpf
    }

    # retorna o nova_pessoa foi cadastrado na lista
    return nova_pessoa


# cria nova disciplina
def criar_disciplina(nome_arquivo, nome_disciplina):
    """
    Criar uma nova disciplina
    :param nome_arquivo: arquivo base para salvar a nova disciplina
    :param nome_disciplina: input para o usuário
    :return: o elemento nova_disciplina
    """
    lista = ler_arquivo(nome_arquivo)
    codigo_disciplina = gerar_id_unico(lista)

    nova_disciplina = {
        "id": codigo_disciplina,
        "nome": nome_disciplina,
    }

    return nova_disciplina


# cria nova turma
def criar_turma(nome_turma):
    """
    Cria nova turma
    :param nome_turma: input do usuário
    :return: o elemento nova_turma
    """
    lista_turmas = ler_arquivo(arquivo_turmas)
    lista_professores = ler_arquivo(arquivo_professores)
    lista_disciplinas = ler_arquivo(arquivo_disciplinas)

    id_professor = int
    id_disciplina = int

    if not lista_professores or not lista_disciplinas:
        id_professor = 0
        id_disciplina = 0

    print("Listando professores disponíveis")
    listar_elementos(formatar_estudante_ou_professor, arquivo_professores)

    while True:
        try:
            # pede ID para o usuário
            id_selecionado = int(input("Para selecionar um professor para a turma selecione seu ID: "))
            # atribui o elemento fruto da função para a variável
            professor_selecionado = validar_id(lista_professores, id_selecionado)
        except ValueError:
            print("Selecione um ID válido:")
            continue

        # se o elemento_selecionado for válido
        if professor_selecionado is not None:
            # mostra qual estudante vai ser editado
            print("Professor selecionado é:")
            print(formatar_estudante_ou_professor(professor_selecionado))
            id_professor = professor_selecionado['id']
            break
        else:
            print("Selecione um Id válido!")
            pass

    print("Listando disciplinas disponíveis")
    listar_elementos(formatar_disciplina, arquivo_disciplinas)

    while True:
        try:
            # pede ID para o usuário
            id_selecionado = int(input("Para selecionar uma disciplina para a turma selecione seu ID: "))
            # atribui o elemento fruto da função para a variável
            disciplina_selecionada = validar_id(lista_professores, id_selecionado)
        except ValueError:
            print("Selecione um ID válido:")
            continue

        # se o elemento_selecionado for válido
        if disciplina_selecionada is not None:
            # mostra qual estudante vai ser editado
            print("A disciplina selecionada é:")
            print(formatar_disciplina(disciplina_selecionada))
            id_disciplina = disciplina_selecionada['id']
            break
        else:
            print("Selecione um Id válido!")
            pass

    id_turma = gerar_id_unico(lista_turmas)
    nova_turma = {
        "nome": nome_turma,
        "id": id_turma,
        "id_professor": id_professor,
        "id_disciplina": id_disciplina
    }
    return nova_turma


# cria nova matricula
def criar_matricula(numero_matricula):
    """
    Cria nova matricula
    :param numero_matricula: Input do usuário
    :return: elemento nova_matricula
    """
    lista_matriculas = ler_arquivo(arquivo_matriculas)
    lista_estudantes = ler_arquivo(arquivo_estudantes)

    id_estudante = int

    if not lista_estudantes:
        id_estudante = 0

    print("Listando estudantes disponíveis")
    listar_elementos(formatar_estudante_ou_professor, arquivo_estudantes)

    while True:
        try:
            # pede ID para o usuário
            id_selecionado = int(input("Para selecionar um estudante para esse número de matricula selecione o ID: "))
            # atribui o elemento fruto da função para a variável
            estudante_selecionado = validar_id(lista_estudantes, id_selecionado)
        except ValueError:
            print("Selecione um ID válido:")
            continue

        # se o elemento_selecionado for válido
        if estudante_selecionado is not None:
            # mostra qual estudante vai ser editado
            print("O Estudante selecionado é:")
            print(formatar_estudante_ou_professor(estudante_selecionado))
            id_estudante = estudante_selecionado['id']
            break
        else:
            print("Selecione um Id válido!")
            pass

    id_matricula = gerar_id_unico(lista_matriculas)
    nova_matricula = {
        "numero": numero_matricula,
        "id": id_matricula,
        "id_estudante": id_estudante,
    }
    return nova_matricula


# inclui elemento
def incluir_elemento(elemento, nome_arquivo):
    """
    Inclui qualquer elemento em uma lista
    :param nome_arquivo: arquivo base no qual o elemento sera inserido
    :param elemento: elemento qualquer
    :return: mensagem "Sucesso!"
    """
    lista = ler_arquivo(nome_arquivo)
    lista.append(elemento)
    print("Sucesso!")
    salvar_arquivo(lista, nome_arquivo)


# função para cadastrar/editar/excluir quantos elementos quiser de uma vez
def cadastrar_de_novo(novo_cadastro: str):
    """
    Define saídas para o novo cadastro, sim ou não? se sim continua o cadastro de mais itens, se não sai do laço
    :param novo_cadastro: input do usuário
    :return: True ou False | True continua no processo, False sai
    """
    if novo_cadastro == 's' or novo_cadastro == 'S':
        return True
    elif novo_cadastro == 'n' or novo_cadastro == 'N':
        print("Voltando ao menu...\n")
        return False
    else:
        print("Digite S para sim ou N para não")
        return False


# lista elementos
def listar_elementos(formatar_elemento, nome_arquivo):
    """
    Lista os elementos e retorna eles formatados
    :param nome_arquivo: arquivo base que se3rá usado para listar os elementos
    :param formatar_elemento: formato em que os elementos vão sair
    :return: Os elementos listados de forma formatada ou informa que não existe nada cadastrado
    """
    lista = ler_arquivo(nome_arquivo)
    # valida se existe algum estudante cadastrado, se não:
    if len(lista) == 0:
        print("----------------------------")
        print("Nada cadastrado!")
    # se sim, printa a lista de estudantes
    else:
        print("Presentes no cadastro:")
        print("----------------------------")
        for elemento in lista:
            print(formatar_elemento(elemento))
    print("----------------------------\n")


# formata uma string para o elemento do estudante
def formatar_estudante_ou_professor(pessoa_formatar: dict):
    """
    Formata o estudante ou professor
    :param pessoa_formatar: o elemento da lista
    :return: Retorna uma string formatada com os dados da pessoa
    """
    return f"ID: {pessoa_formatar['id']} - Nome: {pessoa_formatar['nome']}, CPF: {pessoa_formatar['cpf']};"


# formata disciplina
def formatar_disciplina(disciplina_formatar: dict):
    """
    retorna string formatada da disciplina
    :param disciplina_formatar: pega o elemento para formatar
    :return: string formatada da disciplina
    """
    return f"ID: {disciplina_formatar['id']} - Nome: {disciplina_formatar['nome']};"


# formata turma
def formatar_turma(turma_formatar: dict):
    """
    retorna string formatada da turma
    :param turma_formatar: pega o elemento para formatar
    :return: string formatada da turma
    """
    return (f"ID: {turma_formatar['id']} - Nome: {turma_formatar['nome']},"
            f" ID do Professor: {turma_formatar['id_professor']},"
            f" ID da disciplina: { turma_formatar['id_disciplina']};")


# formata matricula
def formatar_matricula(matricula_formatar: dict):
    """
    formata elemento matricula
    :param matricula_formatar: elemento a ser formatado
    :return: elemento formatado em string
    """
    return (f"ID: {matricula_formatar['id']} - Número: {matricula_formatar['numero']}, "
            f"ID do estudante: {matricula_formatar['id_estudante']};")


# valida o ID selecionado pelo usuário
def validar_id(lista, id_selecionado):
    """
    Valida o ID selecionado
    :param lista: passado com o nome do arquivo
    :param id_selecionado: ID fornecido pelo usuário
    :return: Retorna o elemento correspondente ao ID ou vazio
    """
    for elemento_procurado in lista:
        if elemento_procurado['id'] == id_selecionado:
            return elemento_procurado
    return None


# edita estudante ou professor
def editar_estudante_ou_professor(nome_arquivo):
    """
    Edita o estudante ou professor
    :param nome_arquivo: arquivo base que sera utilizado
    :return: Uma string com a nova versão do estudante após a edição
    """
    lista = ler_arquivo(nome_arquivo)
    if len(lista) > 0:
        # Enquanto o ID não for válido
        while True:
            try:
                # pede ID para o usuário
                id_selecionado = int(input("Selecione um ID: "))
                # atribui o elemento fruto da função para a variável
                elemento_selecionado = validar_id(lista, id_selecionado)
            except ValueError:
                print("Selecione um ID válido:")
                continue

            # se o elemento_selecionado for válido
            if elemento_selecionado is not None:
                # mostra qual estudante vai ser editado
                print("Pessoa selecionada para edição:")
                print(formatar_estudante_ou_professor(elemento_selecionado))

                # pede as novas informações
                elemento_selecionado["nome"] = input("Digite o novo nome:")
                pessoa_cpf = input("Digite o novo CPF:")

                # valida novamente o CPF
                while not validar_cpf(lista, pessoa_cpf):
                    print(f'O CPF {pessoa_cpf} já está cadastrado!\nDigite um CPF válido')
                    pessoa_cpf = input('Digite o CPF do estudante\n')

                # atribui um CPF válido
                elemento_selecionado["cpf"] = pessoa_cpf

                salvar_arquivo(lista, nome_arquivo)
                # mostra que a edição foi concluída
                print("Edição concluída!")
                print(formatar_estudante_ou_professor(elemento_selecionado))
                break
            else:
                print("Selecione um Id válido!")


# edita disciplina
def editar_disciplina(nome_arquivo):
    """
    Edita uma disciplina
    :param nome_arquivo: arquivo base
    :return: disciplina editada
    """
    lista = ler_arquivo(nome_arquivo)
    if len(lista) > 0:
        # Enquanto o ID não for válido
        while True:
            try:
                # pede ID para o usuário
                id_selecionado = int(input("Selecione um ID: "))
                # atribui o elemento fruto da função para a variável
                elemento_selecionado = validar_id(lista, id_selecionado)
            except ValueError:
                print("Selecione um ID válido:")
                continue

            # se o elemento_selecionado for válido
            if elemento_selecionado is not None:
                # mostra qual estudante vai ser editado
                print("Disciplina selecionada para edição:")
                print(formatar_disciplina(elemento_selecionado))

                # pede as novas informações
                elemento_selecionado["nome"] = input("Digite o novo nome:")

                salvar_arquivo(lista, nome_arquivo)
                # mostra que a edição foi concluída
                print("Edição concluída!")
                print(formatar_disciplina(elemento_selecionado))
                break
            else:
                print("Selecione um Id válido!")


# edita uma turma
def editar_turma(nome_arquivo):
    """
    Edita uma turma
    :param nome_arquivo: Arquivo base para a modificação
    :return:
    """
    lista = ler_arquivo(nome_arquivo)
    if len(lista) > 0:
        # Enquanto o ID não for válido
        while True:
            try:
                # pede ID para o usuário
                id_selecionado = int(input("Selecione um ID: "))
                # atribui o elemento fruto da função para a variável
                elemento_selecionado = validar_id(lista, id_selecionado)
            except ValueError:
                print("Selecione um ID válido:")
                continue

            # se o elemento_selecionado for válido
            if elemento_selecionado is not None:
                # mostra qual estudante vai ser editado
                print("Turma selecionada para edição:")
                print(formatar_turma(elemento_selecionado))

                elemento_selecionado['nome'] = input("Digite o novo nome:")

                salvar_arquivo(lista, nome_arquivo)
                # mostra que a edição foi concluída
                print("Edição concluída!")
                print(formatar_turma(elemento_selecionado))
                break
            else:
                print("Selecione um Id válido!")


# edita matricula
def editar_matricula(nome_arquivo):
    """
    Edita uma matricula
    :param nome_arquivo: arquivo base para a modificação
    :return: matricula editada
    """
    lista = ler_arquivo(nome_arquivo)
    if len(lista) > 0:
        # Enquanto o ID não for válido
        while True:
            try:
                # pede ID para o usuário
                id_selecionado = int(input("Selecione um ID: "))
                # atribui o elemento fruto da função para a variável
                elemento_selecionado = validar_id(lista, id_selecionado)
            except ValueError:
                print("Selecione um ID válido:")
                continue

            # se o elemento_selecionado for válido
            if elemento_selecionado is not None:
                # mostra qual estudante vai ser editado
                print("Turma selecionada para edição:")
                print(formatar_matricula(elemento_selecionado))

                elemento_selecionado['numero'] = input("Digite o novo número:")

                salvar_arquivo(lista, nome_arquivo)
                # mostra que a edição foi concluída
                print("Edição concluída!")
                print(formatar_matricula(elemento_selecionado))
                break
            else:
                print("Selecione um Id válido!")


# exclui um elemento
def excluir_elemento(formatar_elemento, nome_arquivo):
    """
    Função para excluir um elemento
    :param nome_arquivo: arquivo base para a modificação
    :param formatar_elemento: QUal será o formato de saída dos elementos da lista atualizada
    :return: lista atualizada após a exlusão
    """
    lista = ler_arquivo(nome_arquivo)
    if len(lista) > 0:
        while True:
            try:
                # pede ID para o usuário
                id_selecionado = int(input("Selecione um ID: "))
                # atribui o elemento fruto da função para a variável
                elemento_selecionado = validar_id(lista, id_selecionado)
            except ValueError:
                print("Selecione um ID válido:")
                continue

            if elemento_selecionado is not None:
                print("Sua seleção:")
                print(formatar_elemento(elemento_selecionado))

                # valida se o usuário tem certeza que quer excluir
                excluir = input("Tem certeza que deseja excluir? (S/N)\n")

                # se sim exclui o estudante da lista de estudante
                if excluir == "S" or excluir == "s":

                    lista.remove(elemento_selecionado)
                    salvar_arquivo(lista, nome_arquivo)

                    # printa a lista de estudantes atualizada
                    print("Lista de cadastrado atualizada:")
                    listar_elementos(formatar_elemento, nome_arquivo)
                    break

                # se ele quer cancelar a exclusão
                elif excluir == "n" or excluir == "N":
                    print("Voltando...")
                    break
                # se digitou errado
                else:
                    print("Selecione 'S' para sim ou 'N' para não")
                    continue
            else:
                print("Selecione um Id válido!")


# verifica lista
def lista_vazia(nome_arquivo):
    """
    retorna se a lista é vazia
    :param nome_arquivo: arquivo que vai ser checado
    :return: se for vazia retorna True
    """
    lista = ler_arquivo(nome_arquivo)
    if len(lista) == 0:
        return True


# crud do menu secundário
def crud_menu_secundario(qual_menu, nome_arquivo, formatar_elemento):
    """
    Crud do menu secundário onde estão as funcionalidades incluir, editar, apagar e listar
    :param qual_menu: especifica qual menu foi selecionado
    :param nome_arquivo: qual é o arquivo de base do menu selecionado
    :param formatar_elemento: como o elemeno deverá ser exibido
    :return: True
    """
    # pede ação do usuário
    opcao_desejada2 = menu_secundario()
    # abre as opções
    match opcao_desejada2:
        # incluir
        case "1":
            while True:
                if qual_menu == 1 or qual_menu == 2:
                    print("===== INCLUIR =====\n")
                    novo_estudante_ou_professor = criar_estudante_ou_professor(nome_arquivo,
                                                                               pessoa_nome=input('Digite o nome:\n'),
                                                                               pessoa_cpf=input('Digite o CPF:\n'))

                    incluir_elemento(novo_estudante_ou_professor, nome_arquivo)

                    print(formatar_estudante_ou_professor(novo_estudante_ou_professor))

                    # se quiser sair o laço quebra
                    if not cadastrar_de_novo(
                            novo_cadastro=input("Deseja realizar um novo cadastro?\nS/N\n")):
                        break

                elif qual_menu == 3:
                    print("===== INCLUIR =====\n")

                    nova_disciplina = criar_disciplina(arquivo_disciplinas, nome_disciplina=input("Nova disciplina:"))

                    incluir_elemento(nova_disciplina, nome_arquivo)

                    print(formatar_disciplina(nova_disciplina))
                    # se quiser sair o laço quebra
                    if not cadastrar_de_novo(
                            novo_cadastro=input("Deseja realizar um novo cadastro?\nS/N\n")):
                        break
                elif qual_menu == 4:
                    print("===== INCLUIR =====\n")

                    nova_turma = criar_turma(nome_turma=input("Qual é o nome da turma?\n"))
                    incluir_elemento(nova_turma, arquivo_turmas)

                    print(formatar_turma(nova_turma))

                    # se quiser sair o laço quebra
                    if not cadastrar_de_novo(
                            novo_cadastro=input("Deseja realizar um novo cadastro?\nS/N\n")):
                        break

                elif qual_menu == 5:
                    print("===== INCLUIR =====\n")

                    nova_matricula = criar_matricula(numero_matricula=input("Digite o número da mátricula:\n"))
                    incluir_elemento(nova_matricula, arquivo_matriculas)

                    print(formatar_matricula(nova_matricula))

                    # se quiser sair o laço quebra
                    if not cadastrar_de_novo(
                            novo_cadastro=input("Deseja realizar um novo cadastro?\nS/N\n")):
                        break

        # listar
        case "2":
            print("===== LISTANDO =====\n")

            listar_elementos(formatar_elemento, nome_arquivo)

        # editar dados do estudante
        case "3":
            # edita quantos estudantes o usuário quiser
            while True:
                print("===== EDITAR =====\n")

                # lista os elementos
                listar_elementos(formatar_elemento, nome_arquivo)

                if qual_menu == 1 or qual_menu == 2:
                    # chama a função para editar
                    editar_estudante_ou_professor(nome_arquivo)

                    # verifica se lista é vazia
                    if lista_vazia(nome_arquivo):
                        break

                    # se quiser sair o laço quebra
                    if not cadastrar_de_novo(novo_cadastro=input("Deseja realizar uma nova edição?\nS/N\n")):
                        break
                elif qual_menu == 3:
                    editar_disciplina(nome_arquivo)

                    # verifica se lista é vazia
                    if lista_vazia(nome_arquivo):
                        break

                    # se quiser sair o laço quebra
                    if not cadastrar_de_novo(novo_cadastro=input("Deseja realizar uma nova edição?\nS/N\n")):
                        break
                elif qual_menu == 4:
                    editar_turma(nome_arquivo)

                    # verifica se lista é vazia
                    if lista_vazia(nome_arquivo):
                        break

                    # se quiser sair o laço quebra
                    if not cadastrar_de_novo(novo_cadastro=input("Deseja realizar uma nova edição?\nS/N\n")):
                        break
                elif qual_menu == 5:
                    editar_matricula(nome_arquivo)

                    # verifica se lista é vazia
                    if lista_vazia(nome_arquivo):
                        break

                    # se quiser sair o laço quebra
                    if not cadastrar_de_novo(novo_cadastro=input("Deseja realizar uma nova edição?\nS/N\n")):
                        break

        # excluir um estudante
        case "4":
            while True:
                print("===== EXCLUIR =====\n")
                # lista os elementos (no caso os estudantes formatados)
                listar_elementos(formatar_elemento, nome_arquivo)

                # chama a função para excluir
                excluir_elemento(formatar_elemento, nome_arquivo)

                # verifica se lista é vazia
                if lista_vazia(nome_arquivo):
                    break

                # se quiser sair o laço quebra
                if not cadastrar_de_novo(novo_cadastro=input("Deseja excluir novamente?\nS/N\n")):
                    break

        # volta ao menu principal
        case "5":
            print("===== VOLTANDO AO MENU PRINCIPAL =====\n")
            return False
        # trata outras entradas que não são oções do menu
        case _:
            print("Selecione uma opção válida")
    return True


# Menu Principal
while True:
    # pede uma opção para o usuário
    opcao_desejada = menu_principal()

    # opções do menu
    match opcao_desejada:
        # se 1 - entra no menu de estudantes
        case "1":
            print("***** [ESTUDANTES] MENU DE OPERAÇÕES *****\n")
            while True:
                if not crud_menu_secundario(1, arquivo_estudantes, formatar_estudante_ou_professor):
                    break

        case "2":
            print("***** [PROFESSORES] MENU DE OPERAÇÕES  *****\n")
            while True:
                if not crud_menu_secundario(2, arquivo_professores, formatar_estudante_ou_professor):
                    break

        case "3":
            print("***** [DISCIPLINAS] MENU DE OPERAÇÕES *****\n")
            while True:
                if not crud_menu_secundario(3, arquivo_disciplinas, formatar_disciplina):
                    break
        case "4":
            print("***** [TURMAS] MENU DE OPERAÇÕES *****\n")
            while True:
                if not crud_menu_secundario(4, arquivo_turmas, formatar_turma):
                    break
        case "5":
            print("***** [MATRICULAS] MENU DE OPERAÇÕES *****\n")
            while True:
                if not crud_menu_secundario(5, arquivo_matriculas, formatar_matricula):
                    break
        case "6":
            print("Você está saindo...\nTchau :)")
            break
        case _:
            print("Selecione uma opção válida")
            continue



"""
Ideias para implementar/melhorias
- poder cancelar a operação em qualquer momento (mesmo no meio de inserir ou editar algo, por exemplo)
- verificar o cadastrar novamente para ver se não cabe entrar nas principais funções? - não tenho certeza

"""

"""
Melhorias feitas:
- validação dos nomes (se tem nome repetido) - feito através do CPF (semana 5)
- validar a existencia do cpf na hora da edição (semana 6)
- implementar loops quando existem validações, para voltar de onde parou e nao voltar pro menu principal (semana 6)
- verificar a consistencia dos códigos: pode ser que eles se repitam: criar lógica para não acontecer (semana 8)

"""
