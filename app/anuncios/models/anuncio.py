from flask import Flask ,jsonify
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import validates 

from app import dbt

class Anuncio(dbt.Model): #anuncio
    __tablename__='t_anuncio'
    
    id_anuncio = dbt.Column(dbt.Integer, primary_key=True, nullable=False, unique=True , autoincrement=True)
    modelo  = dbt.Column(dbt.String(45))
    marca = dbt.Column(dbt.String(45))
    numero_passageiro = dbt.Column(dbt.String(45))
    combustivel = dbt.Column(dbt.String(45))
    preco = dbt.Column(dbt.String(45))
    ano = dbt.Column(dbt.String(45))
    condicoes = dbt.Column(dbt.String(150))
    caucao = dbt.Column(dbt.String(45))
    fotografia = dbt.Column(dbt.String(45))
    transmissao = dbt.Column(dbt.String(45))
    link = dbt.Column(dbt.String(500))
    ar_condicionado = dbt.Column(dbt.String(45))
    data = dbt.Column(dbt.String(45))
    gps = dbt.Column(dbt.String(45))
    disponibilidade = dbt.Column(dbt.String(45))
    audit_user = dbt.Column(dbt.String(45))
    audit_timestamp = dbt.Column(dbt.String(45))
    id_anunciante = dbt.Column(dbt.Integer, dbt.ForeignKey("t_anunciante.id_anunciante") )
    
    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
    