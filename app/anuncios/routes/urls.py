from flask import  request 
from flask import  jsonify
from flask import  Blueprint
 
#from  ...app import app
from app.anuncios.services.controllers import remover  
from app.anuncios.services.controllers import listar_todos
from app.anuncios.services.controllers import listar
from app.anuncios.services.controllers import criar
from app.anuncios.services.controllers import actualizar
from app.anuncios.services.controllers import pesquisa_principal
from app.anuncios.services.controllers import filtragem

bp = Blueprint("anuncio", __name__)



@bp.route("/anuncio", methods=['GET', 'POST'])
def criar_listar_anuncio():
    if request.method == 'GET': return listar_todos()
    if request.method == 'POST': return criar()    
#end-def

@bp.route("/anuncio/<id_anuncio>", methods=['GET', 'DELETE', 'PUT'])
def listar_actualizar_apagar_anuncio(id_anuncio):
    if request.method == 'GET': return listar(id_anuncio) 
    elif request.method == 'DELETE': return remover(id_anuncio)
    elif  request.method == 'PUT': return actualizar(id_anuncio)

@bp.route("/pesquisa_principal_inicio", methods=['GET', 'DELETE', 'PUT'])
def pesquisa_veiculo_carro():
    if request.method == 'GET': return pesquisa_principal()

@bp.route("/filtragem", methods=['GET', 'DELETE', 'PUT'])
def pesquisa_filtrada():
    if request.method == 'GET': return filtragem()

@bp.route("/ping")
def resposta():
    return jsonify({"status":"Funciona e funciona mesmo"}),200
#end-def