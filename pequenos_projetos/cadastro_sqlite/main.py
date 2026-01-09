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

#
Base = declarative_base()