# Sistema de Gestão Acadêmica

Este projeto é um sistema de gestão acadêmica desenvolvido em Python que utiliza arquivos JSON para armazenar dados sobre estudantes, professores, disciplinas, turmas e matrículas. O sistema permite gerenciar essas entidades através de um menu interativo.

## Funcionalidades

- **Gerenciar Estudantes**: Incluir, listar, editar e excluir estudantes.
- **Gerenciar Professores**: Incluir, listar, editar e excluir professores.
- **Gerenciar Disciplinas**: Incluir, listar, editar e excluir disciplinas.
- **Gerenciar Turmas**: Incluir, listar, editar e excluir turmas.
- **Gerenciar Matrículas**: Incluir, listar, editar e excluir matrículas.

## Estrutura do Projeto

### Arquivos JSON

Os dados são armazenados em arquivos JSON:

- `lista-de-estudantes.json`
- `lista-de-professores.json`
- `lista-de-disciplinas.json`
- `lista-de-turmas.json`
- `lista-de-matriculas.json`

### Funções Principais

- **Manipulação de Arquivos**
  - `salvar_arquivo(lista, nome_arquivo)`: Salva dados em um arquivo JSON.
  - `ler_arquivo(nome_arquivo)`: Lê dados de um arquivo JSON.

- **Validação e Geração**
  - `validar_cpf(lista, estudante_cpf)`: Valida se um CPF já existe na lista.
  - `gerar_id_unico(lista)`: Gera um ID único que não está presente na lista.

- **Criação de Entidades**
  - `criar_estudante_ou_professor(nome_arquivo, pessoa_nome, pessoa_cpf)`: Cria um novo estudante ou professor.
  - `criar_disciplina(nome_arquivo, nome_disciplina)`: Cria uma nova disciplina.
  - `criar_turma(nome_turma)`: Cria uma nova turma.
  - `criar_matricula(numero_matricula)`: Cria uma nova matrícula.

- **Gerenciamento de Entidades**
  - `incluir_elemento(elemento, nome_arquivo)`: Inclui um novo elemento na lista.
  - `listar_elementos(formatar_elemento, nome_arquivo)`: Lista os elementos de um arquivo.
  - `editar_estudante_ou_professor(nome_arquivo)`: Edita um estudante ou professor.
  - `editar_disciplina(nome_arquivo)`: Edita uma disciplina.
  - `editar_turma(nome_arquivo)`: Edita uma turma.
  - `editar_matricula(nome_arquivo)`: Edita uma matrícula.
  - `excluir_elemento(formatar_elemento, nome_arquivo)`: Exclui um elemento da lista.

- **Formatadores**
  - `formatar_estudante_ou_professor(pessoa_formatar)`: Formata a saída de um estudante ou professor.
  - `formatar_disciplina(disciplina_formatar)`: Formata a saída de uma disciplina.
  - `formatar_turma(turma_formatar)`: Formata a saída de uma turma.
  - `formatar_matricula(matricula_formatar)`: Formata a saída de uma matrícula.

- **Menu**
  - `menu_principal()`: Exibe o menu principal e captura a opção do usuário.
  - `menu_secundario()`: Exibe o menu secundário e captura a opção do usuário.
  - `crud_menu_secundario(qual_menu, nome_arquivo, formatar_elemento)`: Controla as operações de inclusão, edição, listagem e exclusão baseadas na escolha do usuário.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone o repositório ou copie os arquivos para o seu diretório local.
3. Execute o script principal (o arquivo `.py` que contém a lógica do menu) usando o comando:
   ```bash
   python nome_do_arquivo.py
4. Navegue pelo menu interativo para gerenciar estudantes, professores, disciplinas, turmas e matrículas.

## Estrutura do Menu

### Menu Principal

1. Gerenciar estudantes
2. Gerenciar professores
3. Gerenciar disciplinas
4. Gerenciar turmas
5. Gerenciar matrículas
6. Sair

### Menu Secundário

1. Incluir
2. Listar
3. Editar
4. Excluir
5. Voltar ao menu principal

## Requisitos

- Python 3.x
- Biblioteca `json` (inclusa na biblioteca padrão do Python)

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou um pull request.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.

Desenvolvido por Clarice dos Santos Almeida - Análise e Desenvolvimento de Sistemas - 2024
