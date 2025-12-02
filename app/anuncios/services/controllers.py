import traceback
from datetime import datetime

import requests
from flask import request 
from flask import jsonify
from sqlalchemy import or_



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
                link = "link",
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
        print(f'Anuncios criado é', anuncio.to_dict())
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
def pesquisa_principal():
    lista_pesquisa_marca = []
    lista_pesquisa_local_anunciante = []
    veiculo = request.args.get("veiculo")
    local = request.args.get("locais")
    print(F'{veiculo, local}')

    if (veiculo ==''  and local=='')  or  (veiculo ==''  and local =='Santo Antão'):
        print(f'entrou')
        veiculos = Anuncio.query.all()    
        print(len(veiculos))
        for veiculo in veiculos:
            id_anunciante = veiculo.to_dict()["id_anunciante"]

            lista_pesquisa_marca.append( veiculo.to_dict()) 
    
            resposta = requests.get(f"http://127.0.0.1:5000/anunciante/{id_anunciante}")
            lista_pesquisa_local_anunciante.append(resposta.json())  
        
        return jsonify({"marca":lista_pesquisa_marca,"localizacao":lista_pesquisa_local_anunciante})

    else:
        param={
            "ilha":local
        }
        veiculos = Anuncio.query.filter(Anuncio.marca == veiculo ).all()    
        
        for veiculo in veiculos:
            id_anunciante = veiculo.to_dict()["id_anunciante"]
            print(id_anunciante , type(id_anunciante))
            resposta = requests.get(f"http://127.0.0.1:5000/pesquisa_principal_inicio/{id_anunciante}",params=param)
            
            if resposta:
                lista_pesquisa_local_anunciante.append(resposta.json())  
                lista_pesquisa_marca.append( veiculo.to_dict())

        return jsonify({"marca":lista_pesquisa_marca,"localizacao":lista_pesquisa_local_anunciante})

def filtragem():
    lista_pesquisa_marca = []
    lista_pesquisa_local_anunciante = []
    local = request.args.get("local")
    automatico = request.args.get("automatico")
    manual = request.args.get("manual")
    passageiro_um = request.args.get("passageiro_um")
    passageiro_quatro = request.args.get("passageiro_quatro")
    ar_condicionado = request.args.get("ar_condicionado") 
    preco_min = request.args.get("preco_min") 
    preco_max = request.args.get("preco_max") 
    
    
    # Montagem das listas de filtros
    if automatico == "true":
        automatico="automatico"
    if manual == "true":
        manual= "manual"
    if passageiro_um == "true":
        passageiro_um = "1"
    if passageiro_quatro == "true":
        passageiro_quatro = "4"
    if ar_condicionado == "true":
        ar_condicionado = "Sim" 
    #print ("Manual:", manual)
    #print ("Automatico:", automatico)
    #print ("Passageiro Um:", passageiro_um)
    #print ("Passageiro quatro:", passageiro_quatro)
    #print ("Ar condicionado:", ar_condicionado)
    #print ("Preco minimo:", preco_min)
    #print ("Preco maximo:", preco_max)

    
    if all(v in ("false", "") for v in [manual, automatico, passageiro_um, passageiro_quatro, ar_condicionado]):
        
        veiculos = Anuncio.query.all()    
        for veiculo in veiculos:
            id_anunciante = veiculo.to_dict()["id_anunciante"]

            lista_pesquisa_marca.append( veiculo.to_dict()) 
    
            resposta = requests.get(f"http://127.0.0.1:5000/anunciante/{id_anunciante}")
            lista_pesquisa_local_anunciante.append(resposta.json())  
        
        return jsonify({"marca":lista_pesquisa_marca,"localizacao":lista_pesquisa_local_anunciante})
    
    else:    
        param={
            "ilha":local
        }
        
        respostas = requests.get(f"http://127.0.0.1:5000/pesquisa_filtragem_inicio/",params=param)
        
        #print("olimmeeeeee",respostas.json()[0]["ilha"])     
        dados = respostas.json()     
        
        for dado in dados:
            id_anunciante = dado["id_anunciante"]   
            print(id_anunciante)
            if dado:        
                pesquisas_filtradas = Anuncio.query.filter(
                    Anuncio.id_anunciante == id_anunciante,
                    or_(
                        Anuncio.transmissao == manual,
                        Anuncio.transmissao == automatico,                  
                        Anuncio.ar_condicionado == ar_condicionado
                    ),

                ).all()          
                for pesquisa in pesquisas_filtradas:        
                    lista_pesquisa_local_anunciante.append(dado)  
                    lista_pesquisa_marca.append( pesquisa.to_dict())
        
        print("Lista final anunciante",len(lista_pesquisa_local_anunciante))
        print("Lista final marca    ",len(lista_pesquisa_local_anunciante))
        
        return jsonify({"marca":lista_pesquisa_marca,"localizacao":lista_pesquisa_local_anunciante}),201

    