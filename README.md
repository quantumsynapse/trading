Especificação Técnica para Sistema de Trading de Criptoativos

1.0 Introdução

Este documento fornece uma especificação técnica detalhada para o desenvolvimento de um sistema de software de trading de criptoativos. A especificação será organizada no formato de sprints, uma abordagem comum no desenvolvimento ágil de software.


Sprint 1: Configuração Inicial e Integração com Exchanges

1. Configuração do Ambiente:

a. Escolha da Linguagem de Programação e Framework:

Justificativa: A escolha da linguagem e do framework será baseada nas necessidades de desempenho, facilidade de integração com APIs externas e escalabilidade.

Escolhida: Python: Por sua versatilidade e vasta gama de bibliotecas. Frameworks como Django ou Flask podem ser considerados.

b. Configuração de Repositório GIT:

Justificativa: O controle de versão é essencial para o desenvolvimento colaborativo e para manter um histórico das mudanças.

Passos:
Criação de um repositório no GitHub, GitLab ou similar.
Definição de uma estrutura de branches (ex.: main, development, feature/<nome-da-feature>).
Definição de regras para merge e pull requests, incluindo revisões de código.

c. Setup Inicial do Banco de Dados:
Justificativa: O armazenamento de dados é crucial, seja para manter informações sobre usuários, históricos de transações ou configurações do sistema.

Opções:
Relacionais: PostgreSQL, MySQL, Oracle. (SQL)
* Não-relacionais: MongoDB, Cassandra. (NoSQL)

Passos:
Escolha do SGBD (Sistema de Gerenciamento de Banco de Dados) baseado nas necessidades do projeto.
Configuração inicial, incluindo criação de tabelas, índices e relacionamentos (se aplicável).
Definição de políticas de backup e recuperação.

2. Integração com Exchanges:
   
a. Escolha das Exchanges:
Justificativa: Diversificar as fontes de dados pode trazer maior robustez ao sistema e oferecer mais opções aos usuários.

Passos:
Pesquisa das principais exchanges do mercado em termos de volume, confiabilidade e facilidade de integração.
Seleção de, pelo menos, três delas para integração inicial.

b. Integração com APIs:
Justificativa: Para obter dados de mercado em tempo real e executar operações, é necessário integrar-se às APIs das exchanges.

Passos:
Estudo da documentação das APIs das exchanges escolhidas.
Implementação de chamadas para obter dados de mercado (ex.: preços, volumes).
Implementação de funcionalidades para enviar ordens de compra e venda.
Tratamento de possíveis erros e limitações das APIs (ex.: limites de requisições por minuto).
   
######################################################################################################################################################################################################################################

3. Ferramentas e Tecnologias:
Linguagem de programação: Python
Framework de desenvolvimento web: Flask ou Django
Banco de dados: PostgreSQL ou SQLite (dependendo da escala)
Biblioteca para integração com exchanges: CCXT
Biblioteca para análise técnica: TA-Lib
Sistema de versionamento: Git
Ferramenta de CI/CD: Jenkins ou GitHub Actions

#####################################################################################################################################################################################################################################


4 Aćao: Criar o esqueleto da aplicação e integração básica com uma exchange de criptoativos.

Configuração do ambiente de desenvolvimento:

Instalação de dependências
Configuração do repositório Git
Configuração do ambiente virtual Python
Desenvolvimento da integração básica com uma exchange (por exemplo, Binance) utilizando a biblioteca CCXT:

Autenticação
Recuperação de saldo
Listagem de pares de negociação
Execução de ordens
Interface básica para visualização do saldo e execução de ordens.

Use o comando pwd no $ do linux para verificar se estar na pasta de usuario local, em geral /home/<nome_de_usuario/ (área do projeto) 
Note: Observe que todo o codigo abaixo deve rodar dentro da pasta /home/<nome_de_usuario>/trading/trading. 

Etapa 1: 
1.1. Instalação de dependências:

Crie um ambiente virtual para isolar as dependências do projeto.

pip install virtualenv
virtualenv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate


















