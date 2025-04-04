# Core Intuitive - Testes de Sistema

Este repositório contém os testes realizados para o projeto da **Core Intuitive**. O projeto envolve diversas tarefas, como **web scraping**, **extração e transformação de dados de PDF**, **integração com banco de dados** e **desenvolvimento de API**. 

Os testes e tarefas são descritos abaixo, e este repositório contém os códigos que validam e implementam essas funcionalidades. 

## Objetivo do Projeto

Este projeto tem como objetivo a automação da coleta de dados de PDFs, transformação desses dados, integração com banco de dados e a criação de uma interface web que interaja com um servidor em Python.

O projeto é dividido nas seguintes etapas:

1. **Web Scraping** - Coleta dos arquivos e dados da web.
2. **Transformação de Dados** - Extração e processamento dos dados.
3. **Banco de Dados** - Estruturação e consulta dos dados em banco de dados.
4. **API e Interface Web** - Criação de um servidor API e interface para interação com os dados.

## Estrutura do Repositório

Abaixo você encontra a descrição das tarefas realizadas em cada uma das etapas.

---

## 1. TESTE DE WEB SCRAPING

Este teste valida a execução do processo de **web scraping** utilizando Python ou Java.

### Tarefas:
1. **Acesso ao site**:
   - Acesse o site: [https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos)
   
2. **Download dos Anexos I e II**:
   - Baixe os arquivos **Anexo I** e **Anexo II** no formato PDF.
   
3. **Compactação dos anexos**:
   - Compacte os arquivos PDF em um único arquivo no formato ZIP, RAR, ou outro.

**Ferramentas utilizadas:**
- Python
- Selenium
- Requests

---

## 2. TESTE DE TRANSFORMAÇÃO DE DADOS

Este teste valida a **extração e transformação de dados** dos arquivos PDF, bem como a criação de um arquivo CSV compactado.

### Tarefas:
1. **Extração dos dados**:
   - Extraia os dados da tabela **Rol de Procedimentos e Eventos em Saúde** do PDF do **Anexo I** (todas as páginas).
   
2. **Salvamento em formato CSV**:
   - Salve os dados extraídos em uma tabela estruturada no formato **CSV**.
   
3. **Compactação do CSV**:
   - Compacte o arquivo CSV em um arquivo ZIP denominado `Teste_{seu_nome}.zip`.
   
4. **Substituição de abreviações**:
   - Substitua as abreviações nas colunas **OD** e **AMB** pelas descrições completas, conforme a legenda no rodapé.

**Ferramentas utilizadas:**
- Python
- Pandas
- PDFPlumber
- Zipfile

---

## 3. TESTE DE BANCO DE DADOS

Este teste valida a execução de **consultas SQL** para manipulação de dados de um banco de dados MySQL ou Postgres.

### Tarefas de Preparação:
1. **Download dos arquivos**:
   - Baixe os arquivos dos últimos 2 anos do repositório público [dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis](https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/).
   - Baixe os dados cadastrais das Operadoras Ativas na ANS em formato CSV de [operadoras_de_plano_de_saude_ativas](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/).
   
### Tarefas de Código:
1. **Estruturação das tabelas**:
   - Crie queries SQL para estruturar as tabelas necessárias para armazenar os dados CSV.
   
2. **Importação dos dados**:
   - Elabore queries para importar o conteúdo dos arquivos preparados, garantindo o **encoding correto**.
   
3. **Query analítica**:
   - Crie uma query para identificar as **10 operadoras com maiores despesas em "EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR"** no último trimestre.
   - Crie uma query para identificar as **10 operadoras com maiores despesas nesta categoria no último ano**.

**Ferramentas utilizadas:**
- MySQL 8.0 ou Postgres > 10.0
- SQL

---

## 4. TESTE DE API

Este teste envolve o desenvolvimento de uma **API** e uma **interface web** para interação com os dados das operadoras de planos de saúde.

### Tarefas de Preparação:
1. **Utilização do CSV**:
   - Utilize o CSV do item **3.2** (dados cadastrais das operadoras) para alimentar o sistema.

### Tarefas de Código:
1. **Criação da rota da API**:
   - Crie uma rota na API para realizar uma **busca textual** na lista de cadastros das operadoras e retornar os registros mais relevantes.
   
2. **Criação da interface web**:
   - Desenvolva uma interface web utilizando **Vue.js** para permitir que os usuários realizem buscas e visualizem os resultados.

3. **Coleção no Postman**:
   - Elabore uma **coleção no Postman** para demonstrar o resultado da busca da API.

**Ferramentas utilizadas:**
- Python (Flask ou Django)
- Vue.js
- Postman

---

## Como Rodar os Testes

### 1. **Clone o repositório**:

   ```bash
   git clone https://github.com/Tailansant/Core_intuitive