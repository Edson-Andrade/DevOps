import socket
from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis-db', port=6379)

@app.route('/')
def hello():
    visitas = cache.incr('contador_visitas')
    hostname = socket.gethostname()
    return f"""
    <body style="font-family: Arial; text-align: center; margin-top: 50px; background-color: #1e293b; color: #f8fafc;">
        <h1>Arquitetura Multi-Contêiner Ativa!</h1>
        <p>Esta página foi visualizada <strong>{visitas}</strong> vezes.</p>
        <p>Requisição processada pelo contêiner ID: <code>{hostname}</code></p>
    </body>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
