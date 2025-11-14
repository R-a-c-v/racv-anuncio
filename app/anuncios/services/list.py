from datetime import datetime

from flask import request 
from flask import jsonify


from app import  dbt 

from  app.listing.models.anuncio import Anuncio

def  list():
    form = []
    anuncios = Anuncio.query.all()

    for anuncio in anuncios:
      form.append(anuncio.to_dict()) 
    
    return jsonify(form)
  