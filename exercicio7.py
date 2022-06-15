from flask import Flask

app = Flask(__name__)

@app.route("/<int:x>/<int:y>/<int:z>")

def hello_world(x,y,z):
    media=(x+y+z)/3
    if(media>=60):
        return "Você foi aprovado!"
    else: 
        return "Você foi reprovado"