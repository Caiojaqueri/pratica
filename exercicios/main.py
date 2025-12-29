from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()

usuarios = []

class Usuario(BaseModel):
    nome: str
    idade: int
    email: str

@app.post("/usuarios")

def cadastrar_usuario(usuarios: Usuario):
    usuarios.append(Usuario)
    return {"mensagem": "Usuário cadastrado com sucesso!", "usuario": Usuario}

@app.get("/usuarios")

def listar_usuarios():
    return usuarios
