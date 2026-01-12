# cadastro de usuários utilizando fast api e banco de dados sqlite

from fastapi import FastASPI, Depends, HTTPException
from sqlalchemy import Column, Integer, String, create_engine
from slqalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel

# Depends - injeção de dependência (usado para o banco)
# HTTÉxception - retornar erros http (400, 404 etc)
#SQLAlchemy - ORM (conversa com o banco de dados usando Python)

#banco de dados
DATABASE_URL = "sqlite:///./usuarios.db"

# criar engine do banco de dados
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# criar sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# criar base declarativa
Base = declarative_base()


# modelo do banco de dados
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nuullable=False)

Base.metadata.create_all(bind=engine)


# modelo pydantic para validação de dados
class UsuarioCreate(BaseModel):
    nome: str
    email: str

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        from_attributes = True


#fastapi app
app = FastAPI(tittle="Cadastro de Usuários")

# dependência para obter sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# rota para criar um novo usuário
@app.post("usuarios/", response_model=UsuarioResponse)
def criar_usuario(usuarios: UsuarioCreate, db: Session = Depends(get_dp)):
    existe = db.query(Usuario).filter(Usuario.email == usuarios.email).first()
    if existe:
        raise HTTPException(status_code=400, detail="Email já cadastrado")