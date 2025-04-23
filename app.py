from flask import Flask
app = Flask(__devops-inicial__)

@app.route('/')
def home():
    return 'Olá, DevOps! Seu app está rodando!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
