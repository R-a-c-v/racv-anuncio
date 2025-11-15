import traceback
from datetime import datetime

from flask import request 
from flask import jsonify


from app import  dbt 
from  app.anuncios.models.anunciante import Anunciante
from  app.anuncios.models.anuncio import Anuncio

def remover(id_anuncio):
    try:
        Anuncio.query.filter( Anuncio.id_anuncio == id_anuncio).delete()
        dbt.session.commit()  
        return jsonify({'Response': "DONE "}),200
    except AttributeError as e:
        return jsonify({'Respose':"DATA NOT FOUND FOR DELETE"}),404
    #end-try
#end-def
         
def listar_todos():
    form = []
    try:    
        anuncios = Anuncio.query.all()
    
        for anuncio in anuncios:
            form.append(anuncio.to_dict()) 
        
        return jsonify(form)
            
    except AttributeError  as e :
        return jsonify ({"Response": "DATA NOT FOUND"}),404

def listar(id_anuncio):    
    try:    
        response = Anuncio.query.get(id_anuncio).to_dict()
        return jsonify (response)
            
    except AttributeError  as e :
        return jsonify ({"Response": "DATA NOT FOUND"}),404

def safe_str(value):
    if isinstance(value, list):
        return " | ".join([str(v).strip() for v in value if v])
    if value is None:
        return ""
    return str(value).strip()

def criar ():
    try:
        anuncios = request.get_json() 
        for request_data in anuncios: 
            anuncio = Anuncio( 
                modelo = safe_str(request_data['modelo']),
                marca = safe_str(request_data['marca']),
                numero_passageiro =safe_str( request_data['numero_passageiro']),  
                combustivel = safe_str(request_data['combustivel']),
                preco = safe_str(request_data['preco']),
                ano = safe_str(request_data['ano']),
                caucao = safe_str(request_data['caucao']),
                fotografia = safe_str(request_data['fotografia']),
                transmissao = safe_str(request_data['transmissao']),
                link = safe_str(request_data['link']),
                ar_condicionado = safe_str(request_data['ar_condicionado']),
                data = safe_str(request_data['data']),
                gps = safe_str(request_data['gps']),
                disponibilidade = safe_str(request_data['disponibilidade']),
                audit_user = safe_str(request_data['audit_user']),
                audit_timestamp = safe_str(request_data['audit_timestamp']),
                id_anunciante =request_data['id_anunciante']
            ) 
            dbt.session.add(anuncio)
            dbt.session.commit()
        
        return jsonify(anuncio.to_dict())   
    
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error":str(e)})

def actualizar(id_anuncio):
    try:
        resquest = request.get_json()
        
        anuncio = Anuncio.query.get(id_anuncio)
        
        anuncio.modelo = resquest['modelo']
        anuncio.numero_passageiro = resquest['numero_passageiro']
        anuncio.combustivel = resquest['combustivel']
        anuncio.preco = resquest['preco']
        anuncio.ano = resquest['ano']
        anuncio.caucao = resquest['caucao']
        anuncio.fotografia = resquest['fotografia']
        anuncio.caixa_velocidade = resquest['caixa_velocidade']
        anuncio.ar_condicionado = resquest['ar_condicionado']
        anuncio.data = resquest['data']
        anuncio.gps = resquest['gps']
        anuncio.disponibilidade = resquest['disponibilidade']
        anuncio.audit_user = resquest['audit_user']
        anuncio.audit_timestamp = resquest['audit_timestamp']

        dbt.session.commit()
      
        response = Anuncio.query.get(id_anuncio).to_dict()
      
        return jsonify(response)
   
    except ValueError as e :
        return jsonify({"error":str(e)})
    #end-try
#end-def
  