<h1 align="center">API de Busca de Operadoras</h1>

<br>

Este projeto consiste em uma API desenvolvida com Flask e um frontend em Vue.js para realizar buscas em uma base de dados MySQL contendo cadastros de operadoras.

<br>

<h2>Tecnologias Utilizadas 🛠️</h2>

<img align="center" alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>  <img align="center" alt="Flask" src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>  <img align="center" alt="MySQL" src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white"/>  <img align="center" alt="Vue.js" src="https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white"/>  <img align="center" alt="Postman" src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"/>  

<br>

<h2>📌 Requisitos</h2>

Antes de começar, você precisará ter instalado:

•	Python 3 e pip

•	MySQL (Servidor e Banco de Dados)

•	Node.js e npm

<br>

<h2>🛠 Configuração do Banco de Dados</h2>

1.	Crie um banco de dados chamado teste_api no MySQL.

2.	Importe o arquivo CSV fornecido para uma tabela chamada relatorio_cadop.

<br>

<h2>🔧 Configuração do Servidor Flask</h2>

1.	Clone este repositório no seu Git Bash com o Codigo:
```
git clone "URL do repositório"
```

4.	Instale as dependências do Python:
```
pip install flask flask-mysqldb
```

 4.1. para importar o banco você precisa ter essa dependecia:
```
import MySQL
```
6.	Configure a conexão no arquivo app.py. e para importar seu banco, use esse codigo:
```
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Zx29573030!'
app.config['MYSQL_DB'] = 'teste_api'
```

7.	Inicie o servidor:
```
python app.py
```

8.	Antes de testar a API, certifique-se de que o servidor está rodando no VSCode. Depois, a API estará disponível em "http://127.0.0.1:5000/buscar".

<p>Lembre-se de que, para utilizar a API corretamente, é necessário fazer o download do banco de dados. Sem ele, a API não funcionará.</p>
<p>O arquivo do banco de dados será enviado por e-mail.
</p> <p>Após baixar o arquivo "teste_api_relatorio_cadop", crie um esquema no banco de dados chamado "teste_api" e importe o banco de dados para que tudo funcione corretamente.</p>

<br>

<h2>🎨 Configuração do Frontend Vue.js</h2>

1.	Navegue até a pasta do frontend:
```
cd api-interface
```
2.	Instale as dependências:
```
npm install
```
4.	Inicie o servidor Vue:
```
npm run serve
```
6.	Acesse a interface em http://localhost:8080/.

<br>

<h2>🧪 Testando com Postman</h2>

1.	Basta abrir uma "collection" > "add a request".
2.	Faça requisições GET para http://127.0.0.1:5000/buscar?q=operadora.
