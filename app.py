from flask import Flask, request
from models.task import Task

# Criando uma instância da aplicação Flask
app = Flask(__name__)

# Crud significa Create, Read, Update e Delete, que são as operações básicas de um banco de dados.

tasks = []

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()


if __name__ == '__main__':
    app.run(debug=True)  # Executando a aplicação em modo de depuração