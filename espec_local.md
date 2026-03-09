# 🖥️ Automação LOCAL — Atualização do Conector SAP

## 🎯 Objetivo

Automatizar o processo de atualização da pasta **lib** do Conector SAP utilizado na integração entre o **SAP** e o sistema **DFe (emissão de notas fiscais)**.

A atualização consiste em substituir a pasta **lib** do conector atualmente em execução por uma versão mais recente disponível em um novo pacote do Conector SAP.

---

# 📦 Contexto do Cenário de Execução

No cenário normal de execução existe uma pasta chamada:

ConectorSAP

Essa pasta contém arquivos **Java responsáveis pela integração entre o SAP e o sistema DFe**.

Dentro dessa pasta existe um diretório importante:

lib

Essa pasta contém as bibliotecas necessárias para o funcionamento do conector.

O objetivo da automação será:

- Atualizar a pasta **lib** do conector atual
- Utilizar a pasta **lib** da versão mais recente do conector

---

# 🔄 Convenção de nomes utilizada

Para facilitar a descrição do processo, utilizaremos os seguintes nomes:

| Nome | Descrição |
|-----|------|
ConectorSAP-Atual | Conector atualmente em execução no ambiente |
ConectorSAP-Novo | Nova versão do conector que será utilizada para atualização |

---

# 🧭 Fluxo Geral da Atualização

Processo de atualização do conector:

Descompactar ConectorSAP-Novo  
↓  
Descompactar ZIP interno  
↓  
Identificar nome do serviço Windows  
↓  
Parar serviço do Conector  
↓  
Mover arquivos SAPJCO para nova lib  
↓  
Substituir lib atual pela nova lib  
↓  
Iniciar serviço novamente  

---

# 🚀 Etapas do Processo

## 1️⃣ Descompactar o novo conector

A automação deve iniciar realizando a extração do pacote do novo conector.

Passos:

1. Descompactar o arquivo ZIP do **ConectorSAP-Novo**
2. Após a extração será encontrado **um segundo ZIP dentro da pasta**

---

## 2️⃣ Descompactar o ZIP interno

O pacote do conector possui **um ZIP dentro de outro ZIP**.

Portanto:

1. Navegar até o diretório descompactado
2. Localizar o arquivo ZIP interno
3. Realizar a segunda extração

Após essa etapa teremos acesso completo à estrutura do **ConectorSAP-Novo**.

---

# 🔎 3️⃣ Identificar o nome do serviço Windows

Antes de atualizar o conector atual, é necessário identificar **qual serviço Windows está executando o conector**.

Esse nome está definido no arquivo:

bin/wrapper.config

Localização:

ConectorSAP-Atual/bin/wrapper.config

Dentro desse arquivo devemos localizar o elemento:

wrapper.netservice.displayname

Exemplo:

wrapper.netservice.displayname=Conector SAP DFe

O valor desse campo representa **o nome do serviço Windows que está executando o conector**.

Esse nome será utilizado posteriormente para parar e iniciar o serviço.

---

# ⛔ 4️⃣ Parar o serviço do Conector

IMPORTANTE:

O conector **não pode ser atualizado enquanto o serviço Windows estiver em execução**.

Após identificar o nome do serviço:

1. Parar o serviço Windows correspondente ao conector.

Exemplo de comando executado pelo Python:

net stop "Nome do Serviço"

Somente após o serviço estar completamente parado o processo de atualização pode continuar.

---

# 📂 5️⃣ Mover arquivos obrigatórios do Conector Atual

Antes de substituir a pasta **lib**, precisamos preservar dois arquivos do conector atual.

Arquivos:

sapjco3.dll  
sapjco3.jar  

Localização:

ConectorSAP-Atual/lib

Esses arquivos devem ser:

1. Copiados da pasta **lib do ConectorSAP-Atual**
2. Movidos para a pasta **lib do ConectorSAP-Novo**

Após essa etapa, a nova pasta **lib** passará a conter também os arquivos necessários para integração SAP.

---

# 🔁 6️⃣ Substituir a pasta lib

Agora devemos realizar a atualização da pasta **lib**.

Passos:

1. Remover ou renomear a pasta

ConectorSAP-Atual/lib

2. Copiar a pasta

ConectorSAP-Novo/lib

3. Colar no diretório

ConectorSAP-Atual

Resultado esperado:

ConectorSAP-Atual/lib contendo a nova versão das bibliotecas.

---

# ▶️ 7️⃣ Iniciar novamente o serviço

Após finalizar a atualização da pasta **lib**, o serviço do conector pode ser iniciado novamente.

Exemplo de comando:

net start "Nome do Serviço"

---

# 🧰 Bibliotecas Python Utilizadas

Para implementar essa automação serão utilizadas **apenas bibliotecas nativas do Python**, evitando dependências externas.

| Biblioteca | Finalidade |
|-----------|-----------|
os | Manipulação de diretórios |
shutil | Cópia e movimentação de arquivos |
zipfile | Extração de arquivos ZIP |
pathlib | Manipulação de caminhos |
subprocess | Execução de comandos do sistema |
logging | Registro de logs |
time | Controle de tempo e espera |

---

# 🚀 Aplicação das Bibliotecas no Processo

### Extração do Conector

Biblioteca:

zipfile

Responsável por:

- extrair ZIP principal
- extrair ZIP interno

---

### Navegação de diretórios

Bibliotecas:

pathlib  
os  

Responsável por:

- navegar pelas pastas
- localizar arquivos
- construir caminhos de forma segura

---

### Leitura do wrapper.config

Biblioteca:

pathlib

Responsável por:

- abrir o arquivo
- localizar o campo wrapper.netservice.displayname

---

### Controle do serviço Windows

Biblioteca:

subprocess

Responsável por:

- executar comando net stop
- executar comando net start

---

### Movimentação de arquivos

Biblioteca:

shutil

Responsável por:

- copiar arquivos
- mover arquivos
- substituir diretórios

---

# 📊 Resumo das Bibliotecas por Etapa

| Etapa | Biblioteca |
|------|-----------|
Extração do conector | zipfile |
Manipulação de caminhos | pathlib / os |
Leitura de configuração | pathlib |
Controle do serviço | subprocess |
Movimentação de arquivos | shutil |
Logs e controle | logging / time |

---

# 📁 Estrutura esperada do ambiente

Exemplo de estrutura do conector atual:

ConectorSAP-Atual/

bin/  
wrapper.config  

lib/  
sapjco3.dll  
sapjco3.jar  
outras bibliotecas  

logs/

---

Nova versão:

ConectorSAP-Novo/

bin/  
lib/  
outros arquivos

---

# 🎯 Resultado Esperado

Após a execução completa da automação:

- A pasta **lib** do conector atual estará atualizada
- Os arquivos **sapjco3.dll** e **sapjco3.jar** serão preservados
- O serviço Windows do conector estará novamente em execução
- O sistema SAP continuará operando normalmente
