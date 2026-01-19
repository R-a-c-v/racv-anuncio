from flask import  request 
from flask import  jsonify
 
from  ...app import app
from app.anuncios.services.controllers import remover  
from app.anuncios.services.controllers import listar_todos
from app.anuncios.services.controllers import listar
from app.anuncios.services.controllers import criar
from app.anuncios.services.controllers import actualizar
from app.anuncios.services.controllers import pesquisa_principal
from app.anuncios.services.controllers import filtragem

@app.route("/anuncio", methods=['GET', 'POST'])
def criar_listar_anuncio():
    if request.method == 'GET': return listar_todos()
    if request.method == 'POST': return criar()    
#end-def

@app.route("/anuncio/<id_anuncio>", methods=['GET', 'DELETE', 'PUT'])
def listar_actualizar_apagar_anuncio(id_anuncio):
    if request.method == 'GET': return listar(id_anuncio) 
    elif request.method == 'DELETE': return remover(id_anuncio)
    elif  request.method == 'PUT': return actualizar(id_anuncio)

@app.route("/pesquisa_principal_inicio", methods=['GET', 'DELETE', 'PUT'])
def pesquisa_veiculo_carro():
    if request.method == 'GET': return pesquisa_principal()

@app.route("/filtragem", methods=['GET', 'DELETE', 'PUT'])
def pesquisa_filtrada():
    if request.method == 'GET': return filtragem()

@app.get("/ping")
def ping():
    return jsonify({"status": "ok"}), 200
#end-def