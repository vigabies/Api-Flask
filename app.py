from flask import Flask

# Criando uma instância da aplicação Flask
app = Flask(__name__)

@app .route('/') # Rota para a página inicial
def home():
    return "Bem-vindo à minha aplicação Flask!"

@app.route('/about') # Rota para a página "Sobre"
def about():   
    return "Esta é uma aplicação de exemplo usando Flask."

if __name__ == '__main__':
    app.run(debug=True)  # Executando a aplicação em modo de depuração