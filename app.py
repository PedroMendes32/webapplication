from flask import Flask, render_template
from uuid import uuid4

app = Flask(__name__)

agenda = [ { 'id':uuid4(),'Tarefa':'Caminhar com o cachorro','Status':'Realizada','Horário':"18:40",'Tipo':'Lazer'}]
           
@app.route('/inicio')
def inicio():
    return render_template('index.html',agenda = agenda )
    
@app.route('/create')
def create():
    return render_template()

app.run(debug=True)