# cadastro de usuários utilizando fast api e banco de dados sqlite

from fastapi import FastASPI, Depends, HTTPException
from sqlalchemy import Column, Integer, String, create_engine
from slqalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel