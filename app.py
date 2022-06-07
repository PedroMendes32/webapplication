from flask import Flask, render_template, request
from uuid import uuid4

app = Flask(__name__)

agenda = [ { 'id':uuid4(),'Tarefa':'Caminhar com o cachorro','Status':'Realizada','Horário':"18:40",'Tipo':'Lazer'}]
           
@app.route('/inicio')
def inicio():
    return render_template('index.html',agenda = agenda )
    
@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods = ['POST'])
def save():
    tarefa = request.form['Tarefa']
    horario = request.form['Horário']
    tipo = request.form['Tipo']
    agenda.append({'id':uuid4(),'Tarefa':tarefa,'Status':'Não realizada','Horário':horario,'Tipo':tipo})
    return render_template('index.html', agenda = agenda )

@app.route('/edit/<id>')
def edit(id):
    return render_template('update.html')

app.run(debug=True)