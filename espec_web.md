# 🤖 Automação WEB — Download Conector SAP (Thomson Reuters)

## 🎯 Objetivo

Automatizar o processo de acesso ao portal de suporte da Thomson Reuters, realizar login, navegar até o artigo Interfaces DFE, localizar a seção CONECTOR SAP, capturar as versões disponíveis e realizar o download do pacote correspondente.

---

# 🧭 Fluxo Geral da Automação

Iniciar WebDriver
↓
Abrir página de login
↓
Realizar login
↓
Acessar página Interfaces DFE
↓
Localizar seção CONECTOR SAP
↓
Capturar versões disponíveis
↓
Identificar versão mais recente
↓
Baixar pacote
↓
Validar download
↓
Encerrar automação

---

# 🚀 Etapas da Automação

## 1️⃣ Inicialização da Automação

### 📦 Bibliotecas utilizadas

A automação deverá utilizar inicialmente:

- selenium
- os
- time

Opcionalmente:

- webdriver-manager

---

### 🌐 Inicialização do WebDriver

Etapas:

1. Criar instância do WebDriver
2. Configurar diretório de download
3. Maximizar a janela do navegador
4. Definir timeout de carregamento

Fluxo:

Iniciar WebDriver  
Configurar pasta de download  
Abrir navegador  

---

# 🔐 2️⃣ Acesso ao Portal de Suporte

### 🌍 Navegar até a página de login

A automação deve acessar o seguinte link:

https://suporte.thomsonreuters.com.br/auth/v3/signin?brand_id=360003773752&locale=pt-br&return_to=https%3A%2F%2Fsuporte.thomsonreuters.com.br%2Fhc%2Fpt-br&role=end_user

Etapas:

1. Abrir URL no navegador
2. Aguardar carregamento completo da página

---

# 👤 3️⃣ Processo de Login

### 🔎 Localizar campos de login

Identificar os elementos da página:

- Campo usuário / email
- Campo senha
- Botão Entrar

---

### ✍️ Preencher credenciais

A automação deverá:

1. Inserir usuário
2. Inserir senha
3. Clicar no botão Entrar

IMPORTANTE

As credenciais não devem ficar no código.

Utilizar arquivo externo:

.venv

ou

credencial.json

---

# 📄 4️⃣ Navegação para página Interfaces DFE

Após login realizado com sucesso, acessar diretamente:

https://suporte.thomsonreuters.com.br/hc/pt-br/articles/4416108157709-Interfaces-DFE

Etapas:

1. Redirecionar para a URL
2. Aguardar carregamento da página

---

# 🔎 5️⃣ Localizar seção "CONECTOR SAP"

A automação deverá:

1. Percorrer o conteúdo da página
2. Localizar a seção contendo o texto:

CONECTOR SAP

Estratégias possíveis:

- busca por XPath
- busca por texto do elemento
- busca por classe ou ID da seção

---

# 🔢 6️⃣ Capturar numeração das versões

Dentro da seção CONECTOR SAP, a automação deverá:

1. Identificar os links de download disponíveis
2. Extrair os números das versões

Exemplo esperado:

Versão 3.4.2  
Versão 3.5.0  
Versão 3.6.1  

Armazenar as versões em:

lista_de_versoes

---

# 🧠 7️⃣ Identificar versão mais recente

Processo:

1. Comparar versões capturadas
2. Identificar versão mais recente
3. Selecionar link correspondente

---

# ⬇️ 8️⃣ Download do pacote

Após identificar a versão desejada:

1. Clicar no link de download
2. Aguardar download do arquivo
3. Garantir que o download foi iniciado

---

# ✅ 9️⃣ Validação do download

A automação deverá verificar:

- se o arquivo existe na pasta de download
- se o tamanho do arquivo é maior que 0 bytes

Caso falhe:

registrar erro no log

---

# 🛑 🔟 Encerramento da automação

Após finalização:

1. Registrar log de sucesso
2. Encerrar navegador
3. Finalizar execução do script

---

# 📁 Estrutura Sugerida do Projeto

A organização das pastas segue o princípio de separação de responsabilidades, tornando o projeto mais organizado, escalável e fácil de manter.

```
automacao-web/
│
├── src/                     # Código principal da automação
│
│   ├── driver/              # Configuração e inicialização do WebDriver
│   │                        # Responsável por iniciar o navegador, configurar
│   │                        # diretório de download e demais parâmetros.
│
│   ├── pages/               # Representação das páginas WEB (Page Objects)
│   │                        # Contém a estrutura das páginas utilizadas
│   │                        # na automação.
│   │
│   │                        # Aqui devem ser definidos:
│   │                        # - URLs das páginas
│   │                        # - localizadores de elementos (XPath, CSS, ID)
│   │                        # - métodos de interação com a interface
│   │
│   │                        # Exemplo:
│   │                        # login_page.py
│   │                        # interfaces_dfe_page.py
│
│   ├── services/            # Lógica da automação
│   │                        # Contém as funções responsáveis por executar
│   │                        # os fluxos de automação do sistema.
│   │
│   │                        # Nesta pasta ficam:
│   │                        # - funções de login
│   │                        # - navegação entre páginas
│   │                        # - captura de versões
│   │                        # - download de arquivos
│   │
│   │                        # Ou seja, aqui fica a regra de execução da automação.
│
│   └── utils/               # Funções auxiliares
│                            # Utilizado para funções reutilizáveis como:
│                            # - logs
│                            # - leitura de configuração
│                            # - utilitários diversos
│
├── downloads/               # Diretório onde os arquivos baixados serão armazenados
│
├── .env                     # Variáveis de ambiente (credenciais e configurações)
│
├── .gitignore               # Arquivos e pastas ignorados pelo Git
│
├── requirements.txt         # Dependências Python do projeto
│
└── README.md                # Documentação principal do repositório
```

## 🧠 Conceito da Arquitetura

A automação segue uma separação clara entre **estrutura da página** e **lógica de execução**.

### 📄 `pages`

Responsável por representar a estrutura das páginas WEB utilizadas na automação.

Nesta camada ficam:

- URLs das páginas
- localização de elementos da interface
- métodos de interação com botões, campos e links

Essa abordagem facilita a manutenção caso a interface do site seja alterada.

---

### ⚙️ `services`

Responsável por implementar a **lógica da automação**.

Aqui ficam funções que executam os fluxos do processo, por exemplo:

- realizar login
- acessar página de Interfaces DFE
- localizar seção CONECTOR SAP
- capturar versões disponíveis
- realizar download do pacote

Essa camada utiliza as classes definidas em `pages` para executar as ações.

---

## 🔄 Fluxo de execução da automação

```
main.py
   ↓
services (fluxo da automação)
   ↓
pages (estrutura das páginas)
   ↓
Selenium WebDriver
```

Essa separação facilita:

- manutenção do código
- reutilização de componentes
- desenvolvimento colaborativo entre múltiplos desenvolvedores
---

# 🧑‍💻 Responsáveis pelo desenvolvimento

DEV:

Pedro Veiga  
Eduardo Tomazela
