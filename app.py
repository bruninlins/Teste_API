from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import json  # Para manipular JSON corretamente

app = Flask(__name__)

# Configuração do MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Zx29573030!'
app.config['MYSQL_DB'] = 'teste_api'

mysql = MySQL(app)

@app.route('/buscar', methods=['GET'])
def buscar_operadora():
    # Obtendo o termo de busca via parâmetro da URL
    termo_busca = request.args.get('q', '')

    # Conectando ao banco de dados e realizando a consulta
    cursor = mysql.connection.cursor()
    query = "SELECT CNPJ, Razao_Social, Nome_Fantasia, Modalidade FROM relatorio_cadop WHERE Nome_Fantasia LIKE %s"
    cursor.execute(query, ('%' + termo_busca + '%',))

    # Obtendo os resultados
    resultados = cursor.fetchall()

    # Fechando a conexão
    cursor.close()

    # Formatando os resultados corretamente
    relatorio_cadop = [
        {
            'CNPJ': row[0],
            'Razao_Social': row[1],
            'Nome_Fantasia': row[2],
            'Modalidade': row[3]
        }
        for row in resultados
    ]

    # Retornando os dados como JSON formatado
    return app.response_class(
        response=json.dumps(relatorio_cadop, ensure_ascii=False, indent=4),  # Indentação para melhor leitura
        status=200,
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(debug=True)
