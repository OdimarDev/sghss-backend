import bcrypt
from flask_jwt_extended import create_access_token

def gerar_hash_senha(senha):
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

def verificar_senha(senha, hash_senha):
    return bcrypt.checkpw(senha.encode('utf-8'), hash_senha)

def gerar_token(usuario):
    return create_access_token(identity=usuario.id)
