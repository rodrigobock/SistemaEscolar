from ast import Not
from config import *


class Aluno(db.Model):
    # atributos do Aluno
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    cpf = db.Column(db.String(254))

    # método para expressar o aluno em forma de texto
    def __str__(self):
        return str(self.id)+") " + self.nome + ", " + self.email + ", " + self.cpf
    # expressao da classe no formato json

    def json(self):
        return {
            "matricula": self.id,
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf
        }


class Disciplina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    ementa = db.Column(db.String(254))
    ch = db.Column(db.String(254))

    # método para expressar as disciplinas em forma de texto
    def __str__(self):
        return str(self.id)+") " + self.nome + ", " + self.ementa + ", " + self.ch
    # expressao da classe no formato json

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "ementa": self.ementa,
            "ch": self.ch
        }


class Professor(db.Model):
    # atributos do professor
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    cpf = db.Column(db.String(254))
    disciplina = db.Column(db.String(254))

    # método para expressar o professor em forma de texto
    def __str__(self):
        return str(self.id)+") " + self.nome + ", " + self.email + ", " + self.cpf + ", " + self.disciplina
    # expressao da classe no formato json

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf,
            "disciplina": self.disciplina,
        }


class ProfessorDisciplina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer, db.ForeignKey(Professor.id), nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey(Disciplina.id), nullable=False)

    professor = db.relationship("Professor")
    disciplina = db.relationship("Disciplina")

    # método para expressar os carros em forma de texto
    def __str__(self):
        return str(self.id)+") " + self.professor + ", " + self.disciplina
    # expressao da classe no formato json

    def json(self):
        return {
            "id": self.id,
            "professor_id": self.professor_id,
            "disciplina_id": self.disciplina_id,
            "professor": self.professor.json(),
            "disciplina": self.disciplina.json()
        }


class EstudanteDisciplina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    semestre = db.Column(db.String(254))
    aluno_id = db.Column(db.Integer, db.ForeignKey(Aluno.id), nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey(Disciplina.id), nullable=False)
    frequencia = db.Column(db.String(254))

    aluno = db.relationship("Aluno")
    disciplina = db.relationship("Disciplina")

    # método para expressar os carros em forma de texto
    def __str__(self):
        return str(self.id)+") " + self.semestre + ", " + self.aluno + ", " + self.disciplina + ", " + self.frequencia
    # expressao da classe no formato json

    def json(self):
        return {
            "id": self.id,
            "semestre": self.semestre,
            "aluno_id": self.aluno_id,
            "disciplina_id": self.disciplina_id,
            "frequencia": self.frequencia,
            "aluno": self.aluno.json(),
            "disciplina": self.disciplina.json()
        }


class Notas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey(Aluno.id), nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey(Disciplina.id), nullable=False)
    av1 = db.Column(db.Float)
    av2 = db.Column(db.Float)
    av3 = db.Column(db.Float)
    mediaFinal = db.Column(db.Float)

    aluno = db.relationship("Aluno")
    disciplina = db.relationship("Disciplina")

    # método para expressar os alunos e notas em forma de texto
    def __str__(self):
        return str(self.id)+") " + self.aluno + ", " + self.disciplina + ", " + self.av1 + ", " + self.av2 + ", " + self.av3 + ", " + self.mediaFinal

    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "aluno_id": self.aluno_id,
            "disciplina_id": self.disciplina_id,
            "av1": self.av1,
            "av2": self.av2,
            "av3": self.av3,
            "mediaFinal": self.mediaFinal,
            "aluno": self.aluno.json(),
            "disciplina": self.disciplina.json()
        }


# teste
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    a1 = Aluno(nome="Rodrigo", email="rodrigo@gmail.com", cpf="1234567890")

    p1 = Professor(nome="Hylson", email="hylson@gmail.com",cpf="0987654321", disciplina = 1)
    p2 = Professor(nome="Bruce", email="bruce@gmail.com",cpf="0123456789", disciplina = 2)

    d1 = Disciplina(nome="Matematica", ementa="equacoes de 1 grau", ch="40")
    d2 = Disciplina(nome="Portugues", ementa="Verbos no infinitivo", ch="70")

    ad1 = EstudanteDisciplina(semestre="Primeiro", aluno_id=1,disciplina_id=1, frequencia="100%")

    #pd1 = ProfessorDisciplina(professor_id=1, disciplina_id=2)
    
    n1 = Notas(aluno_id = 1, disciplina_id = 1, av1 = 8, av2 = 9, av3 = 4, mediaFinal = 7)
    n2 = Notas(aluno_id = 1, disciplina_id = 2, av1 = 9, av2 = 7, av3 = 5, mediaFinal = 7)

    db.session.add(d1)
    db.session.add(d2)
    db.session.add(a1)
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(ad1)
    #db.session.add(pd1)
    db.session.add(n1)
    db.session.add(n2)

    db.session.commit()
