from turtle import onclick
from config import *
from models import *


@app.route("/")
def inicio():
    return 'Sistema de cadastro de uma escola: <br> <br>' +\
        '<a href="/listar_aluno">Operação listar alunos</a>  <br>' +\
        '<a href="/listar_disciplina">Operação listar disciplinas</a> <br>' +\
        '<a href="/listar_professor">Operação listar Professores</a> <br>' +\
        '<a href="/listar_aluno_disciplina">Operação listar Aluno-Disciplina</a> <br>' +\
        '<a href="/listar_professor_disciplina">Operação listar Professor-Disciplina</a> <br>' +\
        '<a href="/boletim">Boletim</a> <br>'

@app.route("/listar_aluno")
def listar_aluno():
    # obter os alunos do cadastro
    aluno = db.session.query(Aluno).all()
    # aplicar o método json que a classe Aluno possui a cada elemento da lista
    aluno_em_json = [ x.json() for x in aluno ]
    # converter a lista do python para json
    resposta = jsonify(aluno_em_json)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...

# teste da rota: curl -d '{"nome":"James Kirk", "telefone":"92212-1212", "email":"jakirk@gmail.com"}' -X POST -H "Content-Type:application/json" localhost:5000/incluir_aluno
@app.route("/incluir_aluno", methods=['post'])
def incluir_aluno():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações da nova pessoa
    dados = request.get_json() #(force=True) dispensa Content-Type na requisição
    try: # tentar executar a operação
      nova = Aluno(**dados) # criar a nova pessoa
      db.session.add(nova) # adicionar no BD
      db.session.commit() # efetivar a operação de gravação
    except Exception as e: # em caso de erro...
      # informar mensagem de erro
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!

@app.route("/incluir_professor_disciplina", methods=['post'])
def incluir_professor_disciplina():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações da nova pessoa
    dados = request.get_json() #(force=True) dispensa Content-Type na requisição
    try: # tentar executar a operação
      nova = ProfessorDisciplina(**dados) # criar a nova pessoa
      db.session.add(nova) # adicionar no BD
      db.session.commit() # efetivar a operação de gravação
    except Exception as e: # em caso de erro...
      # informar mensagem de erro
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!


@app.route("/listar_professor")
def listar_professor():
    # obter os professores do cadastro
    professor = db.session.query(Professor).all()
    # aplicar o método json que a classe Professor possui a cada elemento da lista
    professor_em_json = [ x.json() for x in professor ]
    # converter a lista do python para json
    resposta = jsonify(professor_em_json)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...

@app.route("/listar_disciplina")
def listar_disciplina():
    # obter as disciplinas do cadastro
    disciplina = db.session.query(Disciplina).all()
    # aplicar o método json que a classe Professor possui a cada elemento da lista
    disciplina_em_json = [ x.json() for x in disciplina ]
    # converter a lista do python para json
    resposta = jsonify(disciplina_em_json)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...

@app.route("/listar_professor_disciplina")
def listar_professor_disciplina():
    # obter os professores do cadastro
    professpr_disciplina = db.session.query(ProfessorDisciplina).all()
    # aplicar o método json que a classe Aluno possui a cada elemento da lista
    professor_disciplina_em_json = [ x.json() for x in professpr_disciplina ]
    # converter a lista do python para json
    resposta = jsonify(professor_disciplina_em_json)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...

@app.route("/listar_aluno_disciplina")
def listar_aluno_disciplina():
    # obter os alunos do cadastro
    aluno_disciplina = db.session.query(EstudanteDisciplina).all()
    # aplicar o método json que a classe Aluno possui a cada elemento da lista
    aluno_disciplina_em_json = [ x.json() for x in aluno_disciplina ]
    # converter a lista do python para json
    resposta = jsonify(aluno_disciplina_em_json)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...

@app.route("/boletim")
def boletim():
    # obter os alunos do cadastro
    boletim = db.session.query(Notas).all()
    # aplicar o método json que a classe Aluno possui a cada elemento da lista
    boletim_em_json = [ x.json() for x in boletim ]
    # converter a lista do python para json
    resposta = jsonify(boletim_em_json)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...

app.run(debug=True)