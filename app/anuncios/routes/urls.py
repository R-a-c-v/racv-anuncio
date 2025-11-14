from flask import  request
 
from  ...app import app
from app.anuncios.services.controllers import remover  
from app.anuncios.services.controllers import listar_anuncio
from app.anuncios.services.controllers import criar
from app.anuncios.services.controllers import actualizar

@app.route("/anuncio", methods=['GET', 'POST'])
def criar_listar_anuncio():
    if request.method == 'GET': return listar_anuncio()
    if request.method == 'POST': return criar()    
#end-def

@app.route("/anuncio/<id_anuncio>", methods=['GET', 'DELETE', 'PUT'])
def listar_actualizar_apagar_anuncio(id_anuncio):
    if request.method == 'GET': return actualizar(id_anuncio) 
    elif request.method == 'DELETE': return remover(id_anuncio)
    elif  request.method == 'PUT': return actualizar(id_anuncio)
#end-def