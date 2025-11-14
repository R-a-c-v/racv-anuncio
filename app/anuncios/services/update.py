from datetime import datetime

from flask import request 
from flask import jsonify


from app import  dbt 
from  app.listing.models.anuncio import Anuncio

def update(anuncio_id):
    try:
        resquest = request.get_json()
        
        anuncio = Anuncio.query.get(anuncio_id)
        
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
      
        response = Anuncio.query.get(anuncio_id).to_dict()
      
        return jsonify(response)
   
    except ValueError as e :
        return jsonify({"error":str(e)})
    #end-try
#end-def
