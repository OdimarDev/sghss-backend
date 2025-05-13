import pytest
from app import app, db
from models import Usuario

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()
        yield client

def test_signup(client):
    response = client.post('/signup', json={
        'email': 'teste@teste.com',
        'senha': '123456'
    })
    assert response.status_code == 201
    assert b'Usuario criado com sucesso' in response.data

def test_login(client):
    client.post('/signup', json={
        'email': 'teste_login@teste.com',
        'senha': '123456'
    })

    response = client.post('/login', json={
        'email': 'teste_login@teste.com',
        'senha': '123456'
    })

    assert response.status_code == 200
    token = response.get_json()['token']
    assert token is not None
    return token

def test_paciente(client):
    # cria usuário único
    client.post('/signup', json={
        'email': 'paciente@teste.com',
        'senha': '123456'
    })

    response = client.post('/login', json={
        'email': 'paciente@teste.com',
        'senha': '123456'
    })

    token = response.get_json()['token']

    response = client.post('/pacientes', json={
        'nome': 'Paciente Teste',
        'cpf': '12345678900'
    }, headers={'Authorization': f'Bearer {token}'})

    assert response.status_code == 200

    response = client.get('/pacientes', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    assert len(response.get_json()) == 1

def test_medico_consulta(client):
    client.post('/signup', json={
        'email': 'medico@teste.com',
        'senha': '123456'
    })

    response = client.post('/login', json={
        'email': 'medico@teste.com',
        'senha': '123456'
    })
    token = response.get_json()['token']

    client.post('/medicos', json={
        'nome': 'Dr. Teste',
        'especialidade': 'Clínico Geral'
    }, headers={'Authorization': f'Bearer {token}'})

    client.post('/pacientes', json={
        'nome': 'Paciente Consulta',
        'cpf': '99988877766'
    }, headers={'Authorization': f'Bearer {token}'})

    response = client.post('/consultas', json={
        'paciente_id': 1,
        'medico_id': 1,
        'data': '2025-04-07'
    }, headers={'Authorization': f'Bearer {token}'})
    
    assert response.status_code == 200
    assert b'Consulta agendada com sucesso' in response.data

