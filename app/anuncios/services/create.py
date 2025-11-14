from datetime import datetime

from flask import request 
from flask import jsonify
import traceback

from app import  dbt 
from  app.listing.models.anuncio import Anuncio
from  app.listing.models.anunciante import Anunciante

def safe_str(value):
    if isinstance(value, list):
        return " | ".join([str(v).strip() for v in value if v])
    if value is None:
        return ""
    return str(value).strip()

def create( ):
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
                id_anunciante =safe_str(request_data['id_anunciante'])
            ) 
            dbt.session.add(anuncio)
            dbt.session.commit()
        
        return jsonify(anuncio.to_dict()), 200
    
    except Exception as e:
        #traceback.print_exc()
        return jsonify({"error":str(e)})
    return anuncio
    #end-try
#end-def