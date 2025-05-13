from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from models import db, Usuario, Paciente, Medico, Consulta
from auth import gerar_hash_senha, verificar_senha
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['JWT_SECRET_KEY'] = 'segredo'
db.init_app(app)
jwt = JWTManager(app)

# Criar banco logo ao iniciar
with app.app_context():
    db.create_all()

@app.route('/signup', methods=['POST'])
def signup():
    dados = request.json
    email = dados['email']
    senha = gerar_hash_senha(dados['senha'])
    usuario = Usuario(email=email, senha=senha)
    db.session.add(usuario)
    db.session.commit()
    return jsonify(mensagem="Usuario criado com sucesso"), 201

@app.route('/login', methods=['POST'])
def login():
    dados = request.json
    usuario = Usuario.query.filter_by(email=dados['email']).first()
    if usuario and bcrypt.checkpw(dados['senha'].encode('utf-8'), usuario.senha):
        token = create_access_token(identity=usuario.id)
        return jsonify(token=token)
    return jsonify(erro="Credenciais inválidas"), 401

@app.route('/pacientes', methods=['POST'])
@jwt_required()
def cadastrar_paciente():
    dados = request.json
    paciente = Paciente(nome=dados['nome'], cpf=dados['cpf'])
    db.session.add(paciente)
    db.session.commit()
    return jsonify(mensagem="Paciente cadastrado com sucesso")

@app.route('/pacientes', methods=['GET'])
@jwt_required()
def listar_pacientes():
    pacientes = Paciente.query.all()
    return jsonify([{'id': p.id, 'nome': p.nome, 'cpf': p.cpf} for p in pacientes])

@app.route('/medicos', methods=['POST'])
@jwt_required()
def cadastrar_medico():
    dados = request.json
    medico = Medico(nome=dados['nome'], especialidade=dados['especialidade'])
    db.session.add(medico)
    db.session.commit()
    return jsonify(mensagem="Médico cadastrado com sucesso")

@app.route('/medicos', methods=['GET'])
@jwt_required()
def listar_medicos():
    medicos = Medico.query.all()
    return jsonify([{'id': m.id, 'nome': m.nome, 'especialidade': m.especialidade} for m in medicos])

@app.route('/consultas', methods=['POST'])
@jwt_required()
def agendar_consulta():
    dados = request.json
    consulta = Consulta(paciente_id=dados['paciente_id'], medico_id=dados['medico_id'], data=dados['data'])
    db.session.add(consulta)
    db.session.commit()
    return jsonify(mensagem="Consulta agendada com sucesso")

@app.route('/consultas', methods=['GET'])
@jwt_required()
def listar_consultas():
    consultas = Consulta.query.all()
    return jsonify([{'id': c.id, 'paciente_id': c.paciente_id, 'medico_id': c.medico_id, 'data da consulta': c.data} for c in consultas])

if __name__ == '__main__':
    app.run(debug=True)
