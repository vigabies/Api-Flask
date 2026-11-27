from flask import Flask, request, jsonify
from models.task import Task

# Criando uma instância da aplicação Flask
app = Flask(__name__)

# CRUD significa Create, Read, Update e Delete,
# que são as operações básicas de um banco de dados.

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control # Sempre usar a variável global para incrementar o ID da tarefa

    data = request.get_json()

    new_task = Task(
        id=task_id_control,
        title=data['title'],
        description=data.get('description', '')
    )

    task_id_control += 1 
    tasks.append(new_task)

    print(tasks)

    return jsonify({"message": "Nova tarefa criada com sucesso"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }
    return jsonify(output)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    for t in tasks:
        if t.id == task_id:
            return jsonify(t.to_dict())
    return jsonify({"message": "Tarefa não encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)